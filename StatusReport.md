# Interim Status Report

## Task Updates
We have finalized our plan and made changes to our timeline. We will be continuing with our research question and have downloaded the necessary data. We have also completed basic analysis accounting for all variables and initial profiling. We have also cleaned the data and prepared it for exploratory analysis.

## Updated Timeline
| Action Item | Description | Deadline | Owner |
|---|---|---|---|
|1. Finalize Plan and Timeline|establish research question and finalize datasets|DONE| All|
|2. Data Acquisition|downloading the data in proper CSV format|DONE| Sri|
|3. Initial Data Analysis|accounting for all variables, data structure, and initial profiling|DONE| Sri and Belle|
|4. Cleaning and Reshaping|cleaning up missing values or incomplete data|DONE| Belle|
|6. Exploratory Analysis & Findings|drawing conclusions on each country or data subject|Week 13| Lucia|
|7. Comparative Analysis & Findings|drawing conclusions on relationships between countries|Week 14| Lucia & Yuxing|
|8. Visualization and Modeling|turning conclusions in visual aids to help see trends|Week 15| Yuxing|
|9. Final Report and Conclusion|documentation of findings and final project submission|Week 15| All|

## Project Changes
1. We initially decided to analyze the years 2000-2026 for the datasets but realized that 2026 information has not yet been updated. For this reason, we will be limiting our analysis to the latest available year which is 2025.

## Challenges

## Member Contributions
1. Sri: I downloaded the 3 indicator datasets (GDP, Unemployment, and Inflation) as CSV files and added them to the project repository. I loaded each one into a pandas DF in a Jupyter notebook and did some basic analysis. I recorded the number of rows and columns, the variables in each file, and whether all five of the countries we want to study are present. I also removed all columns except for the basic ones (country name/code and indicator name/code) as well as the years 2000-2025 columns. I displayed the first five rows of each dataset so my teammates could visualize the changes as well. I then pushed to Github so we could move forward with more cleaning and analysis.
2. Belle: I was responsible for data cleaning and preprocessing the three datasets (GDP Growth, Unemployment, and Inflation). I filtered the datasets to include the five selected countries from 2000 to 2025 and assessed data quality by checking missing values, duplicate records, and data types. I found one missing inflation value for the United States in 2025 and decided to retain it as NaN to avoid introducing bias. No duplicate records were found. I standardized the country codes and numerical data types, then reshaped the datasets from wide to long format and merged them into a single dataset. I also performed final data quality checks to ensure consistency and accuracy. The final cleaned dataset contains 130 country-year observations across five countries and 26 years. I exported the cleaned dataset as a CSV file and uploaded it to GitHub along with an updated version of the analysis notebook.
3. Yuxing:
4. Lucia:
