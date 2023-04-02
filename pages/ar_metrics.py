import sys
sys.path.append('/Users/federico/Documents/Coding/python/interactive_kpi/dash_env/lib/python3.8/site-packages')


# import libraries
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
from dash import callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
import os
import plotly.graph_objects as go

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#server = app.server

dash.register_page(__name__, path='/pages/ar_metrics', name='Metricas de Cartera')

# Read data
df = pd.read_csv("/Users/federico/Documents/Coding/python/interactive_kpi/dash_env/lib/python3.8/site-packages/auto_KPI_app/data/kpi_platicapp.csv")
print(df[ :15])

# Layout
layout = dbc.Container([ 

    # Graph_1 Composición cartera - pie
    dbc.Row([
        dbc.Col([
            html.P("Composición Cartera", className="control_label"),
            dcc.Graph(
                id='ar_composition',
                config={"displaylogo": False},
                style={'display': 'inline-block', 'margin-left': '-5px'}
            )
        ]),                
    ]),

    # Graph_2 Macro_Data/Credito_por_periodo_cumulative
    dbc.Row([
        dbc.Col([
            html.P("Cartera por Estado", className="control_label"),
            dcc.Graph(
                id='ar_type',
                config={"displaylogo": False},
                style={'display': 'inline-block', 'margin-left': '65px', 'margin-top': '20px'}
            )
        ]),
    ]) 
])

# Callback function for graph_1
@callback(Output('ar_composition', 'figure'), [Input('ar_composition', 'id')])
def time_frame_1(term_selected):
    # Create a new column with the current days
    df['current_days'] = (datetime.now() - pd.to_datetime(df['LOANDATE'])).dt.days

    # Create a new column that categorizes the current_days column into bins
    df['days_bin'] = pd.cut(df['current_days'], bins=[120, 150, 180, 210, 240, float('inf')], 
                            labels=['120-150', '150-180', '180-210', '210-240', '240-270'])

    # Aggregate the data by the days_bin column
    agg_data = df.groupby('days_bin').size().reset_index(name='counts')

    graph_1 = px.pie(agg_data, 
        values='counts', 
        names='days_bin',
        color_discrete_sequence=px.colors.qualitative.Plotly,
    )
   
    graph_1.update_traces(
        opacity=0.75,
        textinfo="value+percent"),
    graph_1.update_layout(title_x=0.5)

    graph_1.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400,
        width=800,
        font=dict(color='black'),
        #plot_box={
        #    'border': '1px solid #d4d4d4',
        #    'border-radius': '10px',
        #    'box-shadow': '2px 2px 8px rgba(0, 0, 0, 0.3)'
        #}
    )

    return graph_1

# Callback function for graph_2
@callback(Output('ar_type', 'figure'), [Input('ar_type', 'id')])
def time_frame_2(term_selected):
    # Aggregate the data by STATE column
    agg_data = df.groupby('STATE').size().reset_index(name='counts')

    graph_2 = px.pie(agg_data,
        values='counts', 
        names='STATE',
        color_discrete_sequence=px.colors.qualitative.Plotly,
        )
    graph_2.update_layout(title_x=0.5)

    graph_2.update_layout(
        margin=dict(l=10, r=25, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400,
        width=800,
        font=dict(color='black'),
        #plot_box={
        #    'border': '1px solid #d4d4d4',
        #    'border-radius': '10px',
        #    'box-shadow': '2px 2px 8px rgba(0, 0, 0, 0.3)'
        #}
    )


    return graph_2


