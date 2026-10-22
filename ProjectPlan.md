# Project Plan

## Overview - Yuxing

GDP growth, unemployment, and inflation describe different aspects of an economy. Looking at them together can help us understand how economic conditions change over time. This project will bring together three World Bank indicator datasets to examine these relationships, focusing on the United States and comparing it with Canada, the United Kingdom, Germany, and Japan. We plan to study 2000–2024, depending on data availability.

Much of our work will involve preparing the datasets for analysis. We will first check their coverage, definitions, missing values, and consistency. We will then standardize country codes and years, reshape the tables, and combine the three indicators using country code and year. We will document our cleaning decisions and check that the integration preserves the original values without introducing duplicate or unmatched records.

Using the combined data, we will create graphs showing changes over time and examine how GDP growth and inflation are associated with unemployment. The country comparisons will help us see whether patterns observed in the United States also appear elsewhere. These results will describe associations rather than demonstrate causation.

We will use Python and pandas for data preparation and analysis. Our GitHub repository will include the raw and cleaned data, source and license information, a data dictionary, quality checks, and instructions for reproducing the workflow.

## Team Roles

- **Sri — Raw Data and Licensing** 
- **Belle — Data Cleaning** 
- **Lucia — Statistical Analysis** 
- **Yuxing — Modeling and Visualization** 

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
|1. Finalize Plan and Timeline|establish research question and finalize datasets|Week 9| All|
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
There are several areas in our research plan that require additional input:
1. Data availability and final time period: The proposed analysis covers 2000–2024, but the final time period will depend on whether all three indicators have sufficient and consistent observations across the five selected countries.
2. Missing data treatment: We still need to determine the extent of missing observations for each country and indicator. After After profiling the datasets, we will decide whether incomplete country-year records should be excluded from specific analyses or retained when the available indicators can still be used.
3. Cross-country comparability: Although the World Bank provides standardized indicators, differences in economic conditions and measurement across countries may affect direct comparisons. We need to confirm that the selected indicators and their definitions are sufficiently consistent across the five countries and over time.
4. Treatment of major economic events: Events such as financial crisis and the COVID-19 pandemic may strongly influence GDP growth, inflation, and unemployment. We need to decide whether these periods should be identified separately in the analysis or primarily discussed when interpreting unusual trends and results.
5. Modeling approach: The project will focus on associations rather than causal relationships, but the specific exploratory methods will depend on the amount and quality of usable data. After data integration, we will determine whether correlations and visual comparisons are sufficient or whether additional exploratory models would provide meaningful insights.
