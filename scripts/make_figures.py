"""Create the report figures from the integrated indicator table.

Input : data/cleaned_data.csv
Output: figures/fig1_trends.png, fig2_us_vs_peers.png, fig3_period_means.png, fig4_relationships.png

Run from anywhere:  python scripts/make_figures.py
"""
import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "cleaned_data.csv"
FIGS = ROOT / "figures"

COUNTRIES = ["USA", "CAN", "GBR", "DEU", "JPN"]
PEERS = COUNTRIES[1:]
NAMES = {"USA": "United States", "CAN": "Canada", "GBR": "United Kingdom", "DEU": "Germany", "JPN": "Japan"}
LABELS = {"GDP_Growth": "GDP growth (annual %)", "Unemployment": "Unemployment (% of labor force)",
          "Inflation": "Inflation, consumer prices (annual %)"}
INDICATORS = list(LABELS)

# Validated categorical slots 1-5 (see dataviz palette), fixed per country.
COLOR = {"USA": "#2a78d6", "CAN": "#eb6834", "GBR": "#1baf7a", "DEU": "#eda100", "JPN": "#e87ba4"}
MARKER = {"USA": "o", "CAN": "s", "GBR": "^", "DEU": "D", "JPN": "v"}
SURFACE, INK, INK2, GRID, NEUTRAL = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df", "#8d8c87"
SOURCE = ("Source: World Bank World Development Indicators, export revised 2026-11-11 (CC BY 4.0). "
          "US inflation for 2025 is not published.")

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "text.color": INK, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "axes.edgecolor": GRID, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8, "axes.axisbelow": True,
    "font.size": 10, "axes.titlesize": 11, "axes.titleweight": "bold", "axes.titlelocation": "left",
    "legend.frameon": False,
})


def load(data=DATA) -> pd.DataFrame:
    df = pd.read_csv(data).sort_values(["Country_Code", "Year"]).reset_index(drop=True)
    df["Unemployment_Change"] = df.groupby("Country_Code")["Unemployment"].diff()
    return df


def finish(fig, name, note=SOURCE):
    fig.text(0.01, 0.005, note, fontsize=8, color=INK2, ha="left", va="bottom", wrap=True)
    FIGS.mkdir(exist_ok=True)
    fig.savefig(FIGS / name, dpi=200)
    plt.close(fig)
    print(f"wrote figures/{name}")


def shade_events(ax, label=False):
    for (a, b, text) in [(2008, 2009, "Financial crisis"), (2020, 2020, "COVID-19")]:
        ax.axvspan(a - 0.5, b + 0.5, color=GRID, alpha=0.55, lw=0, zorder=0)
        if label:
            ax.text((a + b) / 2, 1.02, text, transform=ax.get_xaxis_transform(), fontsize=8,
                    color=INK2, ha="center", va="bottom")


def fig_trends(df):
    fig, axes = plt.subplots(3, 1, figsize=(10, 9.2), sharex=True)
    for i, (ax, ind) in enumerate(zip(axes, INDICATORS)):
        shade_events(ax, label=(i == 0))
        for c in COUNTRIES[::-1]:  # draw the US last so it sits on top
            g = df[df["Country_Code"] == c]
            ax.plot(g["Year"], g[ind], color=COLOR[c], marker=MARKER[c], ms=3.5 if c != "USA" else 4.5,
                    lw=2.6 if c == "USA" else 1.5, alpha=1 if c == "USA" else 0.9, label=NAMES[c],
                    mec=SURFACE, mew=0.8, zorder=3 if c == "USA" else 2)
        if ind != "Unemployment":
            ax.axhline(0, color=INK2, lw=0.8, zorder=1)
        ax.set_title(LABELS[ind], pad=14 if i == 0 else 6)
        ax.set_ylabel("%")
    axes[-1].set_xlim(1999.5, 2025.5)
    axes[-1].set_xticks(range(2000, 2026, 5))
    axes[-1].set_xlabel("Year")
    h, l = axes[0].get_legend_handles_labels()
    order = [l.index(NAMES[c]) for c in COUNTRIES]
    fig.legend([h[i] for i in order], [l[i] for i in order], loc="upper center", ncol=5,
               bbox_to_anchor=(0.5, 0.995), fontsize=10)
    fig.suptitle("")
    fig.tight_layout(rect=(0, 0.025, 1, 0.955), h_pad=2.0)
    finish(fig, "fig1_trends.png")


def fig_us_gap(df):
    wide = df.pivot(index="Year", columns="Country_Code", values=INDICATORS)
    fig, axes = plt.subplots(3, 1, figsize=(10, 8.6), sharex=True)
    for i, (ax, ind) in enumerate(zip(axes, INDICATORS)):
        w = wide[ind]
        gap = (w["USA"] - w[PEERS].mean(axis=1, skipna=False)).dropna()
        shade_events(ax, label=(i == 0))
        ax.bar(gap.index, gap.values, width=0.62, color=COLOR["USA"], zorder=3)
        ax.axhline(0, color=INK2, lw=1, zorder=4)
        name = LABELS[ind].split(" (")[0].replace(", consumer prices", "")
        ax.set_title(f"{name}: US minus peer mean. Average {gap.mean():+.2f} pp, US higher in {int((gap > 0).sum())} of {len(gap)} years",
                     pad=14 if i == 0 else 6)
        ax.set_ylabel("percentage points")
    axes[-1].set_xlim(1999.5, 2025.5)
    axes[-1].set_xticks(range(2000, 2026, 5))
    axes[-1].set_xlabel("Year")
    fig.tight_layout(rect=(0, 0.05, 1, 1), h_pad=2.0)
    finish(fig, "fig2_us_vs_peers.png",
           SOURCE + " Peers: Canada, United Kingdom, Germany, Japan (unweighted mean).")


def fig_period_means(df):
    periods = [("2000-2019 (pre-COVID)", 2000, 2019, "#2a78d6"), ("2022-2025 (post-COVID)", 2022, 2025, "#eb6834")]
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.4))
    x = np.arange(len(COUNTRIES))
    for ax, ind in zip(axes, INDICATORS):
        for j, (lab, a, b, col) in enumerate(periods):
            vals = [df[(df["Country_Code"] == c) & df["Year"].between(a, b)][ind].mean() for c in COUNTRIES]
            ax.bar(x + (j - 0.5) * 0.38, vals, width=0.34, color=col, label=lab, zorder=3)
        ax.set_xticks(x)
        ax.set_xticklabels(COUNTRIES)
        ax.axhline(0, color=INK2, lw=0.8)
        ax.set_title(LABELS[ind].split(" (")[0])
        ax.set_ylabel("period mean, %")
        ax.grid(axis="x", visible=False)
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.0))
    fig.tight_layout(rect=(0, 0.04, 1, 0.92))
    finish(fig, "fig3_period_means.png", SOURCE + " 2020-2021 omitted from both periods.")


def fig_relationships(df):
    panels = [("Unemployment", "GDP_Growth", "GDP growth vs unemployment rate", "GDP growth (%)", "Unemployment rate (%)", False),
              ("Unemployment_Change", "GDP_Growth", "GDP growth vs change in unemployment", "GDP growth (%)", "Change in unemployment rate (pp)", True),
              ("Unemployment", "Inflation", "Inflation vs unemployment rate", "Inflation (%)", "Unemployment rate (%)", False)]
    fig, axes = plt.subplots(1, 3, figsize=(12.5, 4.8))
    for ax, (yv, xv, title, xl, yl, fit) in zip(axes, panels):
        d = df.dropna(subset=[xv, yv])
        r = np.corrcoef(d[xv], d[yv])[0, 1]
        for is_us in (False, True):
            for covid in (False, True):
                s = d[((d["Country_Code"] == "USA") == is_us) & (d["Year"].isin([2020, 2021]) == covid)]
                col = COLOR["USA"] if is_us else NEUTRAL
                ax.scatter(s[xv], s[yv], s=46 if covid else 30, marker="D" if covid else "o",
                           facecolor=col, edgecolor=SURFACE if not covid else INK2, linewidth=0.9 if covid else 0.7,
                           alpha=0.95, zorder=3 if is_us else 2)
        if fit:
            b, a0 = np.polyfit(d[xv], d[yv], 1)
            xs = np.linspace(d[xv].min(), d[xv].max(), 50)
            ax.plot(xs, a0 + b * xs, color=INK, lw=1.4, ls="--", zorder=4)
            ann = f"slope {b:.2f} pp per 1 pt growth; r = {r:.2f}, n = {len(d)}"
        else:
            ann = f"r = {r:.2f}, n = {len(d)}"
        ax.set_title(title)
        ax.set_xlabel(f"{xl}\n{ann}")
        ax.set_ylabel(yl)
    handles = [
        plt.Line2D([], [], marker="o", ls="", color=COLOR["USA"], label="United States"),
        plt.Line2D([], [], marker="o", ls="", color=NEUTRAL, label="Canada, UK, Germany, Japan"),
        plt.Line2D([], [], marker="D", ls="", mfc="white", mec=INK2, label="2020-2021 (diamond)"),
    ]
    fig.legend(handles=handles, loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.0))
    fig.tight_layout(rect=(0, 0.05, 1, 0.92))
    finish(fig, "fig4_relationships.png", SOURCE + " Country-year observations, 2000-2025.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DATA, help="Integrated country-year CSV.")
    args = parser.parse_args()
    df = load(args.data)
    fig_trends(df)
    fig_us_gap(df)
    fig_period_means(df)
    fig_relationships(df)


if __name__ == "__main__":
    main()
