from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

app = Dash(__name__)

df=pd.read_csv("/Users/lokeshreddy/Desktop/datavis/facilities.csv")
df.dropna(subset=["facility_state"],inplace=True)
df.at[1667,'facility_state']="Kentucky"


app.layout=html.Div(children=[dcc.Dropdown(id="facility_state",clearable=False,
                                           options=[
                                               {"label":"Alabama" , "value":"Alabama"},
                                               {"label":"Alaska" , "value":"Alaska"},
                                               {"label":"Arizona" , "value":"Arizona"},
                                               {"label":"Arkansas" , "value":"Arkansas"},
                                               {"label":"California" , "value":"California"},
                                               {"label":"Colorado" , "value":"Colorado"},
                                               {"label":"Connecticut" , "value":"Connecticut"},
                                               {"label":"Delware" , "value":"Delware"},
                                               {"label":"District of Columbia" , "value":"District of Columbia"},
                                               {"label":"Florida" , "value":"Florida"},
                                               {"label":"Georgia" , "value":"Georgia"},
                                               {"label":"Hawaii" , "value":"Hawaii"},
                                               {"label":"Idaho" , "value":"Idaho"},
                                               {"label":"Illinois" , "value":"Illinois"},
                                               {"label":"Indiana" , "value":"Indiana"},
                                               {"label":"Iowa" , "value":"Iowa"},
                                               {"label":"Kansas" , "value":"Kansas"},
                                               {"label":"Kentucky" , "value":"Kentucky"},
                                               {"label":"Louisiana" , "value":"Louisiana"},
                                               {"label":"Maine" , "value":"Maine"},
                                               {"label":"Maryland" , "value":"Maryland"},
                                               {"label":"Massachusetts" , "value":"Massachusetts"},
                                               {"label":"Michigan" , "value":"Michigan"},
                                               {"label":"Minnesota" , "value":"Minnesota"},
                                               {"label":"Mississippi" , "value":"Mississippi"},
                                               {"label":"Missouri" , "value":"Missouri"},
                                               {"label":"Montana" , "value":"Montana"},
                                               {"label":"Nebraska" , "value":"Nebraska"},
                                               {"label":"Nevada" , "value":"Nevada"},
                                               {"label":"New Hampshire" , "value":"New Hampshire"},
                                               {"label":"New Jersey" , "value":"New Jersey"},
                                               {"label":"New Mexico" , "value":"New Mexico"},
                                               {"label":"New York" , "value":"New York"},
                                               {"label":"North Carolina" , "value":"North Carolina"},
                                               {"label":"North Dakota" , "value":"North Dakota"},
                                               {"label":"Ohio" , "value":"Ohio"},
                                               {"label":"Oklahoma" , "value":"Oklahoma"},
                                               {"label":"Oregon" , "value":"Oregon"},
                                               {"label":"Pennsylvania" , "value":"Pennsylvania"},
                                               {"label":"Puerto Rico" , "value":"Puerto Rico"},
                                               {"label":"Rhode Island" , "value":"Rhode Island"},
                                               {"label":"South Carolina" , "value":"South Carolina"},
                                               {"label":"South Dakota" , "value":"South Dakota"},
                                               {"label":"Tennessee" , "value":"Tennessee"},
                                               {"label":"Texas" , "value":"Texas"},
                                               {"label":"Utah" , "value":"Utah"},
                                               {"label":"Vermont" , "value":"Vermont"},
                                               {"label":"Virginia" , "value":"Virginia"},
                                               {"label":"Washington" , "value":"Washington"},
                                               {"label":"West Virginia" , "value":"West Virginia"},
                                               {"label":"Wisconsin" , "value":"Wisconsin"},
                                               {"label":"Wyoming" , "value":"Wyoming"},
                                               ]),
                                           dcc.Graph(id="graph", figure={})]
                              )
@app.callback(Output('graph','figure'),
             Input('facility_state','value'))
def cb(facility_state):
    df_facility_state=df.query("facility_state==@facility_state")
    return px.bar(df_facility_state,y="total_inmate_cases",x="facility_type",hover_name="facility_county",title="Total inmate cases state wise")
if __name__ == '__main__':
    app.run_server(debug=True,port=5001)
