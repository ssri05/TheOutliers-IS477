# Project Plan

## Overview - Yuxing

This project will bring together World Bank data on GDP growth, unemployment, and consumer price inflation for 2023–2026. We will focus on the United States and compare it with Canada, the United Kingdom, Germany, and Japan. Looking at these indicators together will help us describe how economic conditions differ across the five countries during this period.

We will first check the available years, indicator definitions, and missing values in each dataset. Since some observations for the planned period may not be published, we will document the actual coverage and use matching years for comparisons. We will standardize country codes and years, reshape the tables, and join the three datasets using country code and year. After integration, we will check for duplicate records, unmatched records, and any changes to the original values.

Using Python and pandas, we will calculate descriptive statistics and create graphs to compare the countries and examine patterns among the three indicators. The short study period will limit what we can conclude, so our analysis will describe observed associations rather than establish causation.

Our GitHub repository will contain the raw and cleaned data, source and license information, a data dictionary, quality checks, and instructions for reproducing the workflow.

## Team Roles
#### Sri - Raw Data and Licensing: Download the three indicator datasets, document sources and licensing conditions, and profile data structure and overall coverage
#### Belle - Data Cleaning: Assess data quality, standardize fields and data types, reshape the datasets, and document decisions about missing values and duplicate records
#### Lucia - Statistical Analysis: Document the datasets, contribute to integration and validation, calculate descriptive statistics, and analyze relationships among the indicators
#### Yuxing - Modeling and Visualization: Develop the project overview and research questions, create trend and comparison visualizations, and conduct exploratory modeling where supported by the available data
#### All Members - Review assessment results, document their contributions, and contribute to the final report and conclusion


## Research/Business Question - Yuxing

Our main research question is:

**How do GDP growth, unemployment, and consumer price inflation compare across the United States, Canada, the United Kingdom, Germany, and Japan during the available years within 2000-2026, and how does the United States compare with the other four countries?**

We will address the following relevant questions as well:

1. How do GDP growth, unemployment, and inflation change in the U.S. during the available years?
2. In years with comparable data, which countries have higher or lower GDP growth, unemployment, and inflation?
3. Across the available country-year observations, what patterns appear between GDP growth and unemployment, and between inflation and unemployment?

Each integrated record will represent one country in one year. We will use descriptive statistics, annual trend plots, country comparison charts, and scatterplots to answer these questions. Each comparison will use matching years and report the number of available observations.

Because the study covers a short period, the findings will describe the selected countries and years rather than establish long-term or causal relationships. Unpublished or missing observations, including any unavailable 2026 values, will remain missing and will not be treated as zero.

## Datasets - Lucia
Data Sources 

All three datasets contain annual country-level indicators from the World Bank’s World Development Indicators (WDI) and licensed under CC BY-4.0. Each indicator comes from a different original producer. We use data for the United States, Canada, the United Kingdom, Germany, and Japan, identified by World Bank country code (USA, CAN, GBR, DEU, JPN). 


1. GDP growth (annual %)  

Source: Country official statistics from national statistical organizations and/or central banks, OECD National Accounts data files, and World Bank staff estimates. 

Definition: Percentage change over the previous year of GDP at constant prices (base year 2015) in US dollars. 

Role: Measures economic growth for the cross-country comparison and for its relationship with unemployment. 

Access: https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG 

 
2. Unemployment, total (% of total labor force)  

Source: ILO Modelled Estimates database (ILOEST), International Labour Organization, published through ILOSTAT. 

Definition: Share of the labor force that is without work but available for and seeking employment. 

Role: Measures labor-market conditions and is the common comparison variable in the relationship questions. 

Access: https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS 
 

3. Inflation, consumer prices (annual %) 

Source: International Financial Statistics database, International Monetary Fund (IMF). 

Definition: Annual percentage change in the cost to the average consumer of acquiring a basket of goods and services, as measured by the consumer price index. 

Role: Measures price pressure and is compared across countries and against unemployment. 

Access: https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG 

 

Structure: Each dataset is a CSV file with one row per country or economy (266 rows) and one column per year from 1960 to 2025. Rows are identified by Country Name, Country Code, Indicator Name, and Indicator Code, and the year columns hold the indicator values. If we were to reshape and join on country code and year, each record would represent one country in one year. 

Coverage: The files contain values from 1960 through 2025. We will use 2023-2025 for the five study countries (USA, CAN, GBR, DEU, JPN). In that window, GDP growth and unemployment each have all 15 country-year observations. Inflation has 14, because no 2025 value is published for the United States. 
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
1. Data availability and final time period: The proposed analysis covers 2000–2026, but the final time period will depend on whether all three indicators have sufficient and consistent observations across the five selected countries.
2. Missing data treatment: We still need to determine the extent of missing observations for each country and indicator. After After profiling the datasets, we will decide whether incomplete country-year records should be excluded from specific analyses or retained when the available indicators can still be used.
3. Cross-country comparability: Although the World Bank provides standardized indicators, differences in economic conditions and measurement across countries may affect direct comparisons. We need to confirm that the selected indicators and their definitions are sufficiently consistent across the five countries and over time.
4. Treatment of major economic events: Events such as financial crisis and the COVID-19 pandemic may strongly influence GDP growth, inflation, and unemployment. We need to decide whether these periods should be identified separately in the analysis or primarily discussed when interpreting unusual trends and results.
5. Modeling approach: The project will focus on associations rather than causal relationships, but the specific exploratory methods will depend on the amount and quality of usable data. After data integration, we will determine whether correlations and visual comparisons are sufficient or whether additional exploratory models would provide meaningful insights.
