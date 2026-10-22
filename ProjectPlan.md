# Project Plan

## Overview - Yuxing

This project will integrate three World Bank indicator datasets—annual GDP growth, total unemployment as a percentage of the labor force (modeled ILO estimate), and annual consumer price inflation—to examine economic trends and relationships. Our proposed scope covers the United States, Canada, the United Kingdom, Germany, and Japan from 2000 to 2024, with the United States as the main analytical focus. We will confirm this scope after checking data availability.

Our primary goal is to produce a reliable, documented, and reproducible integrated dataset. We will preserve the raw files, document sources and licenses, and calculate SHA-256 checksums. Before integration, we will assess accuracy, completeness, timeliness, and consistency. Cleaning will include standardizing country codes, converting years and indicator values to appropriate data types, identifying duplicate records, and documenting missing values. Using Python and pandas, we will reshape the datasets into country-year records and join them using country code and year. Post-integration checks will evaluate unmatched records, missing values, key uniqueness, and agreement with the original data.

The integrated dataset will support descriptive statistics, trend visualizations, and exploratory analysis of relationships among growth, inflation, and unemployment. We will compare U.S. patterns with the other selected countries and interpret results as associations rather than causal effects. Deliverables will include the curated dataset, a data dictionary, machine-readable metadata, quality assessment results, visualizations, and a reproducible workflow.

## Team Roles

- **Sri — Raw Data and Licensing:** Acquire the three indicator datasets, preserve raw files, document sources and licensing conditions, calculate checksums, and profile data structure and coverage.
- **Belle — Data Cleaning:** Assess data quality, standardize fields and data types, reshape the datasets, and document decisions about missing values and duplicate records.
- **Lucia — Statistical Analysis:** Document the datasets, contribute to integration and validation, calculate descriptive statistics, and analyze relationships among the indicators.
- **Yuxing — Modeling and Visualization:** Develop the project overview and research questions, create trend and comparison visualizations, and conduct exploratory modeling where supported by the available data.
- **All Members:** Review integration and quality assessment results, document their contributions, and contribute to the final report and reproducibility checks.

## Research/Business Question - Yuxing

Our main research question is:

**How are annual GDP growth and consumer price inflation associated with unemployment in the United States from 2000 to 2024, and how do these patterns compare with Canada, the United Kingdom, Germany, and Japan?**

We will address three supporting questions:

1. How have GDP growth, inflation, and unemployment changed over time in the United States?
2. Within the United States, how is GDP growth associated with the annual percentage-point change in unemployment, and how is inflation associated with the unemployment rate?
3. How do these trends and associations differ between the United States and the other four selected countries over the same period?

Each integrated record will represent one country in one year. We will use descriptive statistics, annual trend plots, scatterplots, and within-country correlations to answer these questions. Changes in unemployment will be calculated only when observations for consecutive years are available. Each analysis will report the number of usable observations and document exclusions caused by missing data.

The proposed countries and years are subject to confirmation after initial data profiling. Our analysis will describe associations and will not establish causal relationships.
## Datasets - Lucia
## Timeline - Sri
| Action Item | Description | Deadline | Owner |
|---|---|---|---|
|1. Finalize Plan and Timeline|Establish research question and finalize datasets|Week 9| All|
|2. Data Acquisition|downloading the data in proper CSV format|Week 9| Sri|
|3. Initial Data Analysis|accounting for all variables, data structure, and initial profiling|Week 10| Sri and Belle|
|4. Cleaning and Reshaping|cleaning up missing values or incomplete data|Week 10| Belle|
|6. Exploratory Analysis & Findings|drawing conclusions on each country or data subject|Week 10| Lucia|
|7. Comparative Analysis & Findings|drawing conclusions on relationships between countries|Week 11| Lucia & Yuxing|
|8. Visualization and Modeling|turning conclusions in visual aids to help see trends|Week 11| Yuxing|
|9. Final Report and Conclusion|documentation of findings and final project submission|Week 11| All|
## Constraints - Sri
One constraint may be that smaller countries could have gaps in data which would affect the cleaning process and reduce the sample size for some statistics. Additionally, some of the countries are grouped together under different regions which can cause overlap in the data and double count them when drawing conclusions. Lastly, our conclusion will only be based off of limited data since Unemployment and GDP growth is limited to 2023 onwards but Inflation data exists from the 1960s onwards. It will also be difficult to prove a causal relationship and we may only be able to conclude an association.
## Gaps - Belle
