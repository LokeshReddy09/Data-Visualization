**Title: "HW 8, CS 625, Fall 2022"**

**Author: "LOKESH REDDY SONTIREDDY"**

**Date: Thursday, December 8, 2022 by 11:59pm**

# Homework 8: Project - Implement Final Chart

## Choosing the datasets

The COVID-19 outbreak stunned people all around the world.Numerous people were impacted, and many of them perished. This made the situation worse and had a major influence on prisoners.
I'm interested in learning how COVID-19 has affected convicts and cops in different prisons around the United States of America. The study's ultimate objective is to use information from COVID-19 to demonstrate the condition in prisons. 

Here the 2nd dataset is the deeper view of cases in various types of prisons in each state such as state prison, federal prison, jail, reservation jail etc., which describes the spread of the cases in dataset 1 in various counties and facilities across the states.

**Dataset 1**

[Coronavirus (Covid-19) Systems Data in the United States, New York Times](https://github.com/nytimes/covid-19-data/blob/master/prisons/systems.csv)

**Dataset Description**

From March 2020 until the end of March 2021, The New York Times collected data about coronavirus infections, deaths and testing for state and federal prisons; immigration detention centers; juvenile detention facilities; local, regional and reservation jails; and those in the custody of the U.S. Marshals Service.

The gathered information is about infections, deaths, facility populations and tests administered to inmates and correctional officers for 2,805 facilities, and systemwide totals for the same data.

```
state,inmate_tests,total_inmate_cases,total_inmate_deaths,latest_inmate_population,max_inmate_population_2020,total_officer_cases,total_officer_deaths
Alabama,15505,1601,64,19144,21900,1019,3
```

The following definitions apply to the fields:

**system**: The state of the prison system, or other system of detention facilities. For states, the data is reported only for state prisons, not for federal facilities or county jails within the state.

**inmate_tests**: The total number of P.C.R. tests conducted on inmates from the beginning of the pandemic through the end of March 2021.

**total_inmate_cases**: Total number of cases of Covid-19 reported among inmates in that system from the beginning of the pandemic through the end of March 2021.

**total_inmate_deaths**: Total number of inmates in that system who were reported to have died of Covid-19 from the beginning of the pandemic through the end of March 2021.

**latest_inmate_population**: The most recent total number of inmates through the system.

**max_inmate_population_2020**: The maximum number of inmates in the system from May 2020 through March 2021.

**total_officer_cases**: Total number of cases of Covid-19 reported among correctional officers working in the system from the beginning of the pandemic through the end of March 2021.

**total_officer_deaths**: Total number of correctional officers working in the system who were reported to have died of Covid-19 from the beginning of the pandemic through the end of March 2021.


**Dataset 2**


[Coronavirus (Covid-19) Facilities Data in the United States, New York Times](https://github.com/nytimes/covid-19-data/blob/master/prisons/facilities.csv)

```
nyt_id,facility_name,facility_type,facility_city,facility_county,facility_county_fips,facility_state,facility_lng,facility_lat,latest_inmate_population,max_inmate_population_2020,total_inmate_cases,total_inmate_deaths,total_officer_cases,total_officer_deaths,note
F3EFE858,Alex City Work Release prison,Low-security work release,Alex City,Coosa,01037,Alabama,-86.0090148,32.9045073,188,,77,0,17,0,
```

The following definitions apply to the fields:

**nyt_id**: A unique identifier we may use to match future data to this data set.

**facility_name**: The name of the facility.

**facility_type**: The type of facility.

**facility_city**: The city where this facility is located.

**facility_county**: The county where this facility is located.

**facility_county_fips**: The county FIPS code of the county.

**facility_state**: The state where the facility is located.

**facility_lng and facility_lat**: The longitude and latitude of the facility.

**latest_inmate_population**: The most recent number of inmates at the facility.

**max_inmate_population_2020**: The maximum number of inmates at the facility reported at any time from March 2020 through March 2021.

**total_inmate_cases**: Total number of cases of Covid-19 reported among inmates from the beginning of the pandemic through the end of March 2021.

**total_inmate_deaths**: Total number of inmates who were reported to have died of Covid-19 from the beginning of the pandemic through the end of March 2021.

**total_officer_cases**: Total number of cases of Covid-19 reported among correctional officers working at the facility from the beginning of the pandemic through the end of March 2021.

**total_officer_deaths**: Total number of correctional officers who worked at the facility who were reported to have died of Covid-19 from the beginning of the pandemic through the end of March 2021.

**Note**: Any notes important for the interpretation of data on this facility.

## Question

**How are these cases distributed over the various prisons in the state?**

I used 2 idioms for generating charts for this question. They are Stacked Bar Chart and Scatter_Mapbox.

## Stacked Bar chart: ##

| Idiom:      | Stacked Barchart                                                                                       |
|-------------|------------------------------------------------------------------------------------------------|
| What: Data  | Table: Multidmensional table: One quantitative value attribute, two categorical key attributes |
| How: Encode | Bar glyph with length-coded subcomponents of value attribute for each category of secondary key attribute. Separate bars by category of primary key attribute.                                                                                     |
| Why         | Part-to-whole relationship, lockup values, find trends                                          |

In stacked bar charts also i generated 2 charts using different libraries such as plotly express library and Dash python framework.

### Chart 1 (using Plotly express):

Plotly Express is a new high-level Python visualization library that offers a simple vocabulary for complicated charts. It is a wrapper for Plotly.py. 
Plotly Express is an easy-to-use, high-level interface to Plotly, which works with a range of data sources and generates easy-to-style figures. 

```
import plotly
import plotly.express as px
px.bar(df,color="facility_type",y="facility_state",x="total_inmate_cases",hover_data=["facility_county"],width=1000,height=1500)
```

The images of the chart are as follows:

![](https://github.com/odu-cs625-datavis/fall22-hw8-LokeshReddy09/blob/master/FINAL%20QUESTION/Question%202.png)

![](https://github.com/odu-cs625-datavis/fall22-hw8-LokeshReddy09/blob/master/FINAL%20QUESTION/Screen%20Shot%202022-11-26%20at%207.15.47%20PM.png)

![](https://github.com/odu-cs625-datavis/fall22-hw8-LokeshReddy09/blob/master/FINAL%20QUESTION/Screen%20Shot%202022-11-29%20at%207.20.07%20PM.png)

### Chart 1 (using Dash components): (My Final chart)

Dash is a Python framework developed by plotly for the development of interactive web apps. It is built on the foundations of Flask, Plotly.js, and React.js.
It is open source, and applications built using it may be seen via a web browser. 

The images of the chart are as follows:

![](https://github.com/odu-cs625-datavis/fall22-hw8-LokeshReddy09/blob/master/FINAL%20QUESTION/Screen%20Shot%202022-11-27%20at%206.46.49%20PM.png)

![](https://github.com/odu-cs625-datavis/fall22-hw8-LokeshReddy09/blob/master/FINAL%20QUESTION/newplot(1).png)

![](https://github.com/odu-cs625-datavis/fall22-hw8-LokeshReddy09/blob/master/FINAL%20QUESTION/newplot.png)

![](https://github.com/odu-cs625-datavis/fall22-hw8-LokeshReddy09/blob/master/FINAL%20QUESTION/Screen%20Shot%202022-11-29%20at%207.59.30%20PM.png)

### Chart 2 (using scatter mapbox tool):

When displaying data with geographic locations, the scatter mapbox tool is really helpful. 

```
fig = px.scatter_mapbox(df, 
                        lat="facility_lat", 
                        lon="facility_lng", 
                        hover_name="total_inmate_cases", 
                        hover_data=["facility_county","facility_state","total_officer_cases","total_inmate_deaths","total_officer_deaths"],
                        color="facility_type",
                        animation_frame="facility_state",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```
-   The plot is as follows: 

![](https://github.com/odu-cs625-datavis/fall22-hw8-LokeshReddy09/blob/master/FINAL%20QUESTION/Screen%20Shot%202022-11-27%20at%206.44.11%20PM.png)

![](https://github.com/odu-cs625-datavis/fall22-hw8-LokeshReddy09/blob/master/FINAL%20QUESTION/Screen%20Shot%202022-11-29%20at%207.55.27%20PM.png)

My final chart answers the question because it provides the information about the total inmate cases in various types of prison facilities corresponding to a particular state.
In the chart we can see the information of the county name also when we hover over the bars. When we hover over the bars we can see the other information like the total inmate cases number and also the type of facility.

My headline of **"total inmate cases state wise"** fits my chart because the chart depicts the distribution of total inmate cases in various facilities of a state along with their county names.

## Description of every element on the chart

```
px.bar(df_facility_state,y="total_inmate_cases",x="facility_type",hover_name="facility_county",title="Total inmate cases state wise")
```

I assigned facility_type to the X-axis and total_inmate_cases to the Y-axis and also assigned the hover_data with the facility_county.
There is only one color channel i.e., purple.
Here total_inmate_cases is quantitative attribute and facility_type, facility_county are categorical attributes.
The mark used here is line.
The channels used here are position and length.
There is a dropdown menu in the graph where we can select the state of our interest.
When we hover over the bars we can see the information like the total inmate cases number, facility county and also the type of facility.

## The visualization principles and learnings from the semester that were incorporated into the final visualization

1. Correct usage of data types such as categorical and quantitative for the chart generation i.e., using categorical data and generating a histogram is not correct as we should use only continuous data for histograms.
2. Not using the inclined axis names such as axis names at 45 degrees angle.
3. Idiom usage.
4. Concepts of what part of data abstraction.
5. Concepts of why part of data abstraction.
6. Concept of expressiveness principle.
7. Concepts of marks and channels.
8. Concept of making interactive visualizations.

**Apart from these i used plotly express library and the Dash python framework which are out of the syllabus.

## Final Thoughts

I almost spent 6 days for the entire process right from finding the datasets, performing exploratory data analysis, identifying the required idioms and generating the charts.
The aspect that took the most time for me is using the dash python framework because i have to learn the various components usage in it such as app layout, callback, div, dropdown etc.,

Splitting this project up into 3 separate assignments instead of 1 big project assignment was helpful because it provided me more time to do the project and also it gave me the time to learn the new things such as dash framework and also the plotly express visualization library.
I also learnt how to make the interactive plots.

## References ##

1. <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html>
2. <https://plotly.com/python/plotly-express/>
3. <https://www.youtube.com/watch?v=FpCgG85g2Hw&t=9s>
4. <https://dash.plotly.com/dash-core-components/dropdown>
5. <https://www.youtube.com/watch?v=UYH_dNSX1DM>
6. <https://cran.r-project.org/web/packages/dashCoreComponents/vignettes/dash-core-components.html>
7. <https://plotly.com/python/setting-graph-size/>
8. <https://re-thought.com/how-to-change-or-update-a-cell-value-in-python-pandas-dataframe/>
9. <https://plotly.com/python/mapbox-layers/>
10. <https://github.com/nytimes/covid-19-data/tree/master/prisons>
11. <https://plotly.github.io/plotly.py-docs/generated/plotly.express.scatter_mapbox.html>
12. <https://medium.com/analytics-vidhya/visualize-geographic-data-on-python-using-scatter-mapbox-86f54341af85>
13. <https://medium.com/plotly/introducing-plotly-express-808df010143d>
14. <https://plotly.com/python/scattermapbox/>
15. <https://towardsdatascience.com/dash-for-beginners-create-interactive-python-dashboards-338bfcb6ffa4>
