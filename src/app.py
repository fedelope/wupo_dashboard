import sys
sys.path.append('/Users/federico/Documents/Coding/python/interactive_kpi/dash_env/lib/python3.8/site-packages')
sys.path.append('/Users/federico/Documents/Coding/python/interactive_kpi/dash_env/lib/python3.8/site-packages/auto_KPI_app')

#export PYTHONPATH=$PYTHONPATH:/dash_env/python3.8/site-packages

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import datetime
import os
import numpy as np
import pandas as pd


#exportPYTHONPATH=$PYTHONPATH:dash_env/lib/python3.8/site-packages

colors = {
    'back': '#111111',
    'card_color': '#FFFFFF',
    'text': '#7FDBFF',
    'color_1': '#FFFFFF',
    'color_2': '#FFFFFF',
    'color_3': '#FFFFFF',
    'color_4': '#FFFFFF'
}

back_color=colors['back'],
card_color=colors['card_color'],
font_color=colors['text']


app = dash.Dash(__name__, 
                pages_folder='../pages',
                use_pages=True, 
                external_stylesheets=[dbc.themes.SPACELAB],#SUPERHERO], #SPACELAB, #SOLAR                
                suppress_callback_exceptions=True,
# Needs this code for movile responsive.
    meta_tags=[{'name': 'viewport',
                'content': 'width=device-width, initial-scale=1.0'
    }]
)

#deploy to servet 
server = app.server

sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",                
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="me-1",        
)

logo_wupo = 'wupo_logo.png'

#app_dir = os.path.dirname(os.path.abspath(__file__))
#logo_wupo = os.path.join(app_dir, 'assets', 'wupo_logo.png')


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div(
                html.A(
                    html.Div(
                        #html.Img(
                        #    src=app.get_asset_url(logo_wupo),
                        #    height="150px",
                        #    width="150px",
                        #),
                        html.H1("Wupo"),
                        style={
                            'fontSize': 30,
                            'textAlign': 'center', 
                            'color': 'gray', 
                            'margin-top': '0px'
                        },
                        className='text-center'
                    ),
                href="https://www.wupealo.com"
                ),
            #style={
            #    'display': 'flex',
            #    'align-items': 'center',
            #    'justify-content': 'center',
            #    'margin-top': '20px'                    
            #}
            ),


                html.Div(
                    html.H2("Dash Board App"),
                        style={
                            'fontSize': 30,
                            'textAlign': 'center', 
                            'color': 'gray', 
                            'margin-top': '0px'
                        },
                    className='text-center'   
                )
            
        ],
        style={ 'justify-content': 'center', 'align-items': 'center'}
        )
    ]),

    html.Hr(
    style={
        'margin': '0 auto',
        'width': '40%',
        'border-top': '3px complete sion',
        'opacity': '0.5',
    }
    ),


    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ],
        style={
                'margin-top': '20px'
        }
    )
], fluid=True)


if __name__ == "__main__":
    app.run_server(debug=True, port=2000)
