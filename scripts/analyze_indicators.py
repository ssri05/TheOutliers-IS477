"""Descriptive and exploratory analysis of the integrated indicator table.

Input : data/cleaned_data.csv   (one row per country-year: GDP_Growth, Unemployment, Inflation)
Output: results/*.csv           (tables cited in the README findings)

Run from anywhere:  python scripts/analyze_indicators.py
All paths are resolved relative to the repository root.
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "cleaned_data.csv"
OUT = ROOT / "results"

COUNTRIES = ["USA", "CAN", "GBR", "DEU", "JPN"]
PEERS = [c for c in COUNTRIES if c != "USA"]
INDICATORS = ["GDP_Growth", "Unemployment", "Inflation"]
COVID_YEARS = [2020, 2021]
PERIODS = {
    "2000-2007 pre-crisis": (2000, 2007),
    "2008-2010 financial crisis": (2008, 2010),
    "2011-2019 recovery": (2011, 2019),
    "2020-2021 COVID-19": (2020, 2021),
    "2022-2025 post-COVID": (2022, 2025),
}


def load(data=DATA) -> pd.DataFrame:
    df = pd.read_csv(data)
    df = df.sort_values(["Country_Code", "Year"]).reset_index(drop=True)
    assert not df.duplicated(["Country_Code", "Year"]).any(), "duplicate country-year rows"
    # Change in the unemployment rate (percentage points), within each country.
    df["Unemployment_Change"] = df.groupby("Country_Code")["Unemployment"].diff()
    return df


def descriptive_stats(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for code, g in df.groupby("Country_Code"):
        for ind in INDICATORS:
            s = g.set_index("Year")[ind].dropna()
            rows.append({
                "country_code": code, "indicator": ind, "n": len(s),
                "mean": s.mean(), "std": s.std(), "median": s.median(),
                "min": s.min(), "min_year": s.idxmin(),
                "max": s.max(), "max_year": s.idxmax(),
            })
    out = pd.DataFrame(rows)
    out["country_code"] = pd.Categorical(out["country_code"], COUNTRIES, ordered=True)
    return out.sort_values(["indicator", "country_code"]).reset_index(drop=True)


def period_means(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for label, (a, b) in PERIODS.items():
        sub = df[df["Year"].between(a, b)]
        for code in COUNTRIES:
            g = sub[sub["Country_Code"] == code]
            for ind in INDICATORS:
                rows.append({"period": label, "country_code": code, "indicator": ind,
                             "n_years": int(g[ind].notna().sum()), "mean": g[ind].mean()})
    return pd.DataFrame(rows)


def us_vs_peers(df: pd.DataFrame):
    """US value minus the unweighted mean of the four peer countries, by year."""
    wide = df.pivot(index="Year", columns="Country_Code", values=INDICATORS)
    by_year = {}
    for ind in INDICATORS:
        w = wide[ind]
        # Peer mean requires all four peers to be observed in that year.
        peer = w[PEERS].mean(axis=1, skipna=False)
        by_year[ind] = pd.DataFrame({"usa": w["USA"], "peer_mean": peer, "gap": w["USA"] - peer})
    yearly = pd.concat(by_year, names=["indicator"]).reset_index()

    rows = []
    for label, (a, b) in {**PERIODS, "2000-2025 all years": (2000, 2025)}.items():
        for ind in INDICATORS:
            s = yearly[(yearly["indicator"] == ind) & yearly["Year"].between(a, b)].dropna(subset=["gap"])
            rows.append({"period": label, "indicator": ind, "n_years": len(s),
                         "usa_mean": s["usa"].mean(), "peer_mean": s["peer_mean"].mean(),
                         "mean_gap": s["gap"].mean(),
                         "years_usa_higher": int((s["gap"] > 0).sum())})
    return yearly, pd.DataFrame(rows)


def _corr_row(label, sample, d, x, y, fe_demean=True):
    d = d.dropna(subset=[x, y])
    pr = stats.pearsonr(d[x], d[y])
    sr = stats.spearmanr(d[x], d[y])
    within = np.nan
    if fe_demean:
        xd = d[x] - d.groupby("Country_Code")[x].transform("mean")
        yd = d[y] - d.groupby("Country_Code")[y].transform("mean")
        within = stats.pearsonr(xd, yd)[0]
    return {"relationship": label, "sample": sample, "n": len(d),
            "pearson_r": pr[0], "pearson_p": pr[1], "spearman_rho": sr[0], "within_country_r": within}


def correlations(df: pd.DataFrame) -> pd.DataFrame:
    pairs = [
        ("GDP growth vs unemployment rate (levels)", "GDP_Growth", "Unemployment"),
        ("GDP growth vs change in unemployment rate", "GDP_Growth", "Unemployment_Change"),
        ("Inflation vs unemployment rate (levels)", "Inflation", "Unemployment"),
        ("Inflation vs change in unemployment rate", "Inflation", "Unemployment_Change"),
        ("GDP growth vs inflation", "GDP_Growth", "Inflation"),
    ]
    rows = []
    for label, x, y in pairs:
        rows.append(_corr_row(label, "all years", df, x, y))
        rows.append(_corr_row(label, "excluding 2020-2021", df[~df["Year"].isin(COVID_YEARS)], x, y))
    return pd.DataFrame(rows)


def ols(y, X, names):
    """Plain OLS with classical standard errors and t-based 95% CIs."""
    X = np.asarray(X, float)
    y = np.asarray(y, float)
    n, k = X.shape
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    df_resid = n - k
    sigma2 = resid @ resid / df_resid
    se = np.sqrt(np.diag(sigma2 * np.linalg.inv(X.T @ X)))
    tcrit = stats.t.ppf(0.975, df_resid)
    ss_tot = ((y - y.mean()) ** 2).sum()
    r2 = 1 - (resid @ resid) / ss_tot
    return {nm: (b, s, b - tcrit * s, b + tcrit * s) for nm, b, s in zip(names, beta, se)}, r2, n


def okun(df: pd.DataFrame) -> pd.DataFrame:
    """Okun-style regression: change in unemployment (pp) on GDP growth (%)."""
    d = df.dropna(subset=["GDP_Growth", "Unemployment_Change"])
    specs = [("pooled", d), ("pooled, excluding 2020-2021", d[~d["Year"].isin(COVID_YEARS)])]
    rows = []

    def add(label, sub, fe):
        if fe:  # country fixed effects via dummies
            dummies = pd.get_dummies(sub["Country_Code"], dtype=float)
            X = np.column_stack([sub["GDP_Growth"].values, dummies.values])
            names = ["slope"] + list(dummies.columns)
        else:
            X = np.column_stack([sub["GDP_Growth"].values, np.ones(len(sub))])
            names = ["slope", "intercept"]
        res, r2, n = ols(sub["Unemployment_Change"], X, names)
        b, s, lo, hi = res["slope"]
        rows.append({"model": label, "country_fixed_effects": fe, "n": n, "slope_pp_per_1pct_growth": b,
                     "std_err": s, "ci95_low": lo, "ci95_high": hi, "r_squared": r2})

    for label, sub in specs:
        add(label, sub, fe=False)
        add(label + " + country fixed effects", sub, fe=True)
    for code in COUNTRIES:
        add(f"{code} only", d[d["Country_Code"] == code], fe=False)
    return pd.DataFrame(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DATA, help="Integrated country-year CSV.")
    args = parser.parse_args()
    OUT.mkdir(exist_ok=True)
    df = load(args.data)
    yearly, summary = us_vs_peers(df)
    tables = {
        "descriptive_stats.csv": descriptive_stats(df),
        "period_means.csv": period_means(df),
        "us_vs_peers_by_year.csv": yearly,
        "us_vs_peers_summary.csv": summary,
        "correlations.csv": correlations(df),
        "okun_regression.csv": okun(df),
    }
    for name, t in tables.items():
        t.round(4).to_csv(OUT / name, index=False)
        print(f"wrote results/{name}  ({len(t)} rows)")

    pd.set_option("display.width", 200, "display.max_columns", 20)
    print("\nUS minus peer mean, 2000-2025 (percentage points):")
    print(summary[summary["period"] == "2000-2025 all years"].round(2).to_string(index=False))
    print("\nCorrelations:")
    print(tables["correlations.csv"].round(3).to_string(index=False))
    print("\nOkun regressions:")
    print(tables["okun_regression.csv"].round(3).to_string(index=False))


if __name__ == "__main__":
    main()
