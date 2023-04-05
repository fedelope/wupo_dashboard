import sys
sys.path.append('/Users/federico/Documents/Coding/python/interactive_kpi/dash_env/lib/python3.8/site-packages')

import plotly.graph_objects as go
import pandas as pd
import dash
from dash import dcc
from dash import html

dash.register_page(__name__, path='/pages/elevation_metrics', name='Metricas Elevación')

z_data = pd.read_csv("interactive_kpi/dash_env/lib/python3.8/site-packages/auto_KPI_app/data/elevation.csv")

fig = go.Figure(
    data=go.Surface(z=z_data.values),
    layout=go.Layout(
        title="Elevation",
        width=900, 
        height=600,
    )
)


layout = html.Div([
    dcc.Graph(
        id='Elevation Metrics', 
        figure=fig,
        style={'width': '100%', 'height': '100%', 'position': 'absolute'},
        config = {"displaylogo": False}
        )
])

fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        template='plotly_white',
        #height=400,
        #width=800,
        font=dict(color='black'),
        #    'border': '1px solid #d4d4d4',
        #    'border-radius': '10px',
        #    'box-shadow': '2px 2px 8px rgba(0, 0, 0, 0.3)'
        #}
    )

