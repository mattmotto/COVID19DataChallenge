# CUEPID Data Challenge, April 2020
## Team: The Gang Gets Quarantined
Codebase for Columbia's[ COVID-19 Data Challenge team](https://datascience.columbia.edu/dsis-center-health-analytics-launches-covid-19-data-challenge " COVID-19 Data Challenge team") made up of Matthew Otto (SEAS'21), Jason Mohabir (SEAS'21), Trey Gililand (SEAS'22), and Tommy Gomez (CC'22).

Check out our visualization page [here!](https://mattmotto.github.io/COVID19DataChallenge/)

Check out our results presentation [here!](https://drive.google.com/file/d/17VLfUkkGQxszKJHhVe05uqlDDwnBc5-c/view?usp=sharing)

## Empirical Visualization
Using [NYC Department of Health and Mental Hygiene (DOHMH) Incident Command System for COVID-19 Response Data](https://github.com/nychealth/coronavirus-data), we compiled the source data to determine the rate of spread in each of NYC's zipcodes. 

Outerboroughs tends to have faster rates of spread than than Manhattan implying there may be underlying contribute to disproportional rates in these communities.

## Simulated Data
Using a basic SIR model, we generated a stochoastic model of the infection's spread. We utilized this model to discern what the R-naught *(the number of new infections estimated to stem from a single case)* would be in a stochastic scenario. 

## City Similarity Metric
While NYC is currrently at the epicenter of the epidemic, COVID-19 can be expected to spread to our cities in the United States. We sought to figure out which other cities would also be heavily impacted by an outbreak by comparing inequality attributes between cities. Our intuition came from the paper, ["Mobility, Economic Opportunity and New York City Neighborhoodsand New York City Neighborhoods"](https://wagner.nyu.edu/files/faculty/publications/JobAccessNov2015.pdf) from **The Rudin Center for Transportation at the NYU Wagner School** which led us to to believe a communities' access to public transportation would impact COVID-19's spread rate. We selected Chicago and Los Angeles as susceptible cities given their similar urban environment to New York City. We compiled transportation data for these cities and correlated NYC zipcodes to LA neighborhoods. 

## Demographic Model

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
