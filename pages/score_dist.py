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
import datetime
import os
import plotly.graph_objects as go
import numpy as np
from dash_bootstrap_templates import load_figure_template
#It is used to calculate the cumulative distribution function (CDF) of the normal distribution in the Black-Scholes option pricing model.
from scipy.stats import norm
import plotly.figure_factory as ff

# Read data
#df = pd.read_csv("interactive_kpi/dash_env/lib/python3.8/site-packages/auto_KPI_app/data/kpi_platicapp.csv")
df = pd.read_csv("https://github.com/fedelope/wupo_dashboard/blob/3bb81a3d76630665621e19dd5f58bf196db6f9b5/data/kpi_platicapp.csv")
print(df[ :15])

dash.register_page(__name__, path='/pages/score_dist', name='Distribución SCORE')


# Define the layout
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#server = app.server
load_figure_template('SANDSTONE')

layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.P("Credit Score - Distribución Estadística", className="control_label"),
            dcc.Graph(
                id='score',
                config={"displaylogo": False},
                style={'display': 'inline-block', 'margin-left': '-5px'}
            )
        ])
    ])
])

# Callback function for graph_1
@callback(Output('score', 'figure'), [Input('score', 'id')])
def time_frame_1(term_selected):
    
    df['score_data'] = df['SCORE']
    # Create a new column that categorizes the current_days column into bins
    df['score_calc'] = pd.cut(df['score_data'], bins=[500, 600, 700, 800, 900, float('inf')], 
                            labels=['0-500', '500-600', '600-700', '700-800', '900+'])

    # Aggregate the data by the days_bin column
    agg_data = df.groupby('score_calc').size().reset_index(name='counts')

    # Create histogram plot
    graph_1 = px.histogram(agg_data, 
                           x='score_calc', 
                           y='counts', 
                           color='score_calc', 
                           nbins=5, 
                           color_discrete_sequence=px.colors.qualitative.Pastel, 
                           labels={'score_calc': 'Score range', 'counts': 'Frequency'})

    
    graph_1.update_traces(
        opacity=0.75),
    graph_1.update_layout(
        #title='Distribution of Score',
        xaxis_title='Score range',
        yaxis_title='Frequency',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=True,
        #height=400,
        #width=800,
        font=dict(color='black'),
    )

    return graph_1

