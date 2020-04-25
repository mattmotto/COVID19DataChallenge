
# CUEPID Data Challenge, April 2020
## Team: The Gang Gets Quarantined
### Project: COVID19’s Relationship to Different Demographics
Codebase for Columbia's[ COVID-19 Data Challenge team](https://datascience.columbia.edu/dsis-center-health-analytics-launches-covid-19-data-challenge " COVID-19 Data Challenge team") made up of Matthew Otto (SEAS'21), Jason Mohabir (SEAS'21), Trey Gililand (SEAS'22), and Tommy Gomez (CC'22).

Check out our visualization page [here!](https://mattmotto.github.io/COVID19DataChallenge/)

Check out our results presentation [here!](https://drive.google.com/file/d/17VLfUkkGQxszKJHhVe05uqlDDwnBc5-c/view?usp=sharing)

## Empirical Visualization
Using [NYC Department of Health and Mental Hygiene (DOHMH) Incident Command System for COVID-19 Response Data](https://github.com/nychealth/coronavirus-data), we compiled the source data to determine the rate of spread in each of NYC's zipcodes. 

Outerboroughs tends to have faster rates of spread than Manhattan implying there may be underlying population features that contribute to disproportional spread rates in these communities.

## Simulated Data
Using a basic SIR model, we generated a stochastic model of the infection's spread. We utilized this model to discern what the R-naught *(the number of new infections estimated to stem from a single case)* would be in a stochastic scenario. 

## City Similarity Metric
While NYC is currrently at the epicenter of the epidemic, COVID-19 can be expected to spread to or cities in the United States. We sought to figure out which other cities would also be heavily impacted by an outbreak by comparing inequality attributes between cities. Our intuition came from the paper, ["Mobility, Economic Opportunity and New York City Neighborhoodsand New York City Neighborhoods"](https://wagner.nyu.edu/files/faculty/publications/JobAccessNov2015.pdf) from **The Rudin Center for Transportation at the NYU Wagner School** which led us to to believe a communities' access to public transportation would impact COVID-19's spread rate. We selected *(Chicago and Los Angeles)* as susceptible cities given their similar urban environment to New York City. We compiled transportation data for these cities and correlated NYC zipcodes to LA neighborhoods. 

## Population Data Model
Given the infection's spread throughout NYC and the abundance of publicly available, we developed a XGBoost machine learning model to understand which features played a non-neglible role in the infection rate of a zipcode. We gathered features from various modalities including **Census, Demographic, Social, Economic, and Housing** from ["NYC Planning Population FactFinder"](https://github.com/NYCPlanning/labs-factfinder) (in total 1300+ features for 119 zipcodes). Our target was the average rate of change in positive COVID-19 cases for each zipcode.

We believe a **population data** model will be crucial in understanding why COVID-19 differentially impacts certain communities, specifically low-income and minority communities. 

To explore the code for the model and the preprocessing utilized, check out **population_data_model.ipynb** in our [**model branch**](https://github.com/mattmotto/COVID19DataChallenge/tree/model). 

Our accomplishments and recommendations with the model:

 1. *Curated Population Data*: We pulled down data files for each **Neighborhood Tabulation Area** and mapped NTAs to **Zipcodes**, allowing for further research into how varying population features can account for COVID-19's differential impact. 
 2. *Dimensionality Reduction / Feature Selection*: We suggest that feature selection be employed using L1 regularization (Lasso) and recursive feature removal to reduce the feature space and create a more parsimonious model
 3. *Aggregating Categories of Features*: Each of the 1300+ features is associated with a `category` such as `sex_and_age` and `occupation`, thus a further explorations of this model should group these features together to theoretically strengthen the correlation. 
 4. *Models for each Modality*: Given the five existing modalities, `Census`, `Demographic`, `Social`, `Economic`, and `Housing`  a model should be attempted to be created for each of them instead of the current *all-in-one* in order to elucidate important features in modality. 

## Next Steps
Due to time constraints, the full vision of our suite of visualization tools could not be realized. Each component allows to interrogate the notion of **differential spread rates caused by underlying population features**. 

*Empirical Visualization* enables us to see the varying spread rates for each zip code in NYC. Next steps would be overlaying population data and attempting to correlate spread rate with population features. 

*Simulated Data* enables us to have a null model that provides insight into how COVID-19 would have spread had no governmental intervention taken plan. Deviations from the null model thus inform us about which policies are effective. Next steps would be quantifying the difference in the simulated and empirical data and overlaying the dates of governmental actions to determine which policies were most effective in R-naught reduction in which zipcodes. 

*City Similarity Metric* enables us to extend our findings to the rest of the United States by providing a framework to quantify similarities between different cities by looking at metrics such as public transportation usage and population density. Next steps would be formalizing this metric, aggregating population data for other cities like NYC, and trying to predict which neighborhoods given their population features would likely see similar rates of spread. 

*Population Data Model* enables us to build a model based on census data to both understand which population features are most important in spread rate and potentially predict the spread rates for similar neighborhoods. Next steps would be testing out different models to create a baseline expectation, applying regularization to the current model to ensure the model can be effective to new data, and exploring methods to extract important features.

## Files:
1. **city_comparison** contains data comparing NYC neighborhood demographics to neighborhoods in Chicago and Los Angeles
2. **machine_learning_model** contains data generated and used by our machine learning model predicting most imporant demographic factors to spread rate
3. **national_data** contains data matching COVID-19 cases and deaths to geographic regions of the U.S. ([source](https://www.nytimes.com/interactive/2020/world/coronavirus-maps.html))
4. **nyc_planner_data** contains demographic, economic, housing, etc. data in various regions of NYC
5. **population_factfinder** contains demographic, economic, housing, etc. data of NYC
6. **random_simulation** contains code used to generate our visualization of randomized spread of COVID-19
7. **zipcode_data** contains data matching positive, total cases and deaths to zipcodes in NYC throughout the month of April

## Create your own visualizations!
To create your own NYC-based visualizations, check out **visualization-code.ipynb** in our [**gh-pages branch**](https://github.com/mattmotto/COVID19DataChallenge/tree/gh-pages). 
