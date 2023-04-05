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


# Create data
#S: stock price
S = np.linspace(50, 150, 100, 150)
#K: strike price
K = np.linspace(50, 150, 100, 150)
S, K = np.meshgrid(S, K)
#T: time to maturity (in years)
T = 2
#r: risk-free interest rate
r = 0.05
#sigma: volatility of the stock price
sigma = 0.2
#d1, d2: intermediate calculations used in the Black-Scholes option pricing formula
d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
d2 = d1 - sigma*np.sqrt(T)
#call: the value of a call option using the Black-Scholes formula
call = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
#put: the value of a put option using the Black-Scholes formula
put = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)
#Z: the value of the option (in this case, a call option) that will be plotted in the 3D graph.
Z = call  # Set Z to the call option value
# Create figure


fig = go.Figure(data=[go.Surface(x=S, y=K, z=Z)])

# Update layout
fig.update_layout(scene=dict(xaxis_title='Stock Price',
                             yaxis_title='Strike Price',
                             zaxis_title='Option Value'),
                  margin=dict(l=0, r=0, b=0, t=0),
                  )

dash.register_page(__name__, path='/pages/option_valuation', name='Valoración Opciones')

layout = html.Div([
    html.Label('Select option type:'),
    dcc.Dropdown(
        id='option-type-dropdown',
        options=[
            {'label': 'Opción Call', 'value': 'call'},
            {'label': 'Opción Put', 'value': 'put'}
        ],
        value='call',
        style={'width': '200px'}  
    ),
    dcc.Graph(id='option-valuation-plot', 
            figure=fig,
            style={'width': '100%', 'height': '100%', 'position': 'center'},
            config={"displaylogo": False},
    ),
])

@callback(
    Output('option-valuation-plot', 'figure'),
    Input('option-type-dropdown', 'value')
)

def update_graph(option_type):
    if option_type == 'call':
        Z = call
    else:
        Z = put

    fig = go.Figure(data=[go.Surface(x=S, y=K, z=Z)])

    fig.update_layout(scene=dict(xaxis_title='Precio Acción',
                                 yaxis_title='Strike Price',
                                 zaxis_title='Valor Opción'),
                      margin=dict(l=0, r=0, b=0, t=0),
                      )

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='black')
    )

    return fig
