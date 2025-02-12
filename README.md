# **Public Health Data Analysis: COVID-19 Trend Analysis in US Prisons**

## **Project Overview**
The COVID-19 pandemic significantly impacted people worldwide, including incarcerated individuals and correctional officers in U.S. prisons. This project aims to analyze the spread of COVID-19 in various types of prison facilities across the United States, leveraging data visualization techniques to gain insights into inmate and officer infection trends.

This analysis is based on two datasets collected by **The New York Times** from March 2020 to March 2021, covering:
1. **State and Federal Prison System Data**: COVID-19 infections, deaths, and testing among inmates and correctional officers.
2. **Facility-Level Data**: A deeper view of COVID-19 cases in different prison types, such as state prisons, federal prisons, jails, and reservation jails.

## **Datasets Used**
### **Dataset 1: Coronavirus (Covid-19) Systems Data**
- Covers infections, deaths, and testing at the system level for 2,805 facilities.
- Data fields include:
  - **State**
  - **Total Inmate Cases**
  - **Total Inmate Deaths**
  - **Total Officer Cases**
  - **Total Officer Deaths**
  - **Testing and Population Data**

### **Dataset 2: Coronavirus (Covid-19) Facilities Data**
- Provides a facility-level breakdown of cases in different prison types.
- Data fields include:
  - **Facility Name, Type, and Location**
  - **COVID-19 Cases Among Inmates and Officers**
  - **Total Deaths**
  - **Maximum and Latest Inmate Population**

## **Key Research Question**
**How are COVID-19 cases distributed across various prison types and states?**

## **Data Visualization Techniques**
To answer this question, **stacked bar charts** and **scatter map visualizations** were used.

### **1. Stacked Bar Chart**
- **Idiom Used**: Stacked Bar Chart
- **Why?** 
  - Helps visualize part-to-whole relationships.
  - Displays how COVID-19 cases are distributed across different facility types within states.
- **Tools Used**:
  - **Plotly Express**: Quick visualization using `px.bar()`
  - **Dash Python Framework**: Interactive web-based visualization.

#### **Plotly Express Code:**

```python
import plotly.express as px
px.bar(df, color="facility_type", y="facility_state", x="total_inmate_cases", hover_data=["facility_county"], width=1000, height=1500)
```

### **2. Scatter Mapbox Visualization**

 - **Idiom Used**: Scatter Mapbox
 - **Why?** 
        - Ideal for visualizing geographically distributed data.
        - Shows COVID-19 case distribution across facilities in an interactive format.
 - **Tools Used** :
        - **Plotly Express**
        - **Mapbox API (Open Street Map)**

## Scatter Mapbox Code:

```python
import plotly.express as px

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

## **Results & Insights**

  - **PLong-term trend**: The highest number of cases were reported in state prisons, followed by county jails and federal prisons.
  - **PRegional variation**: States like California, Texas, and Florida had a high concentration of infections.
  - **PFacility type impact**: Different facility types had different outbreak patterns, with long-term facilities facing more severe outbreaks.
  - **POfficer vs. Inmate Cases**: Inmate infections were significantly higher than officer infections, but officer deaths were disproportionately high.

## **Final Thoughts**

  - **PTime Spent**: Around 6 days were spent on dataset selection, data preprocessing, visualization, and learning new tools.
  - **PChallenges Faced**: Learning the Dash framework and using Mapbox for interactive mapping took the most effort.
  - **PKey Takeaways**: This project helped in:
        Understanding data abstraction and visualization principles.
        Implementing interactive charts.
        Using Python frameworks (Dash & Plotly Express) for real-time visualization.


## **Requirements**

To run this project, install the required libraries:

```bash
pip install numpy pandas plotly dash matplotlib seaborn 
```

## **Usage**

 - Open PROJECT.ipynb in Jupyter Notebook.
 - Follow the step-by-step analysis:
     -- Data preprocessing
     -- Visualization generation
 - Run plot_test.py to generate visualizations.

