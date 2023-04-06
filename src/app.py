import sys
sys.path.append('/Users/federico/Documents/Coding/python/interactive_kpi/dash_env/lib/python3.8/site-packages')
sys.path.append('/Users/federico/Documents/Coding/python/interactive_kpi/dash_env/lib/python3.8/site-packages/auto_KPI_app')


import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import datetime
import os
import numpy as np
import pandas as pd




app = dash.Dash(__name__, 
                pages_folder='../pages',
                assets_folder='../assets',
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



#logo_wupo = app.get_asset_url('Wupo_logo.png')
logo_wupo = "../assets/wupo_logo.png"

#app_dir = os.path.dirname(os.path.abspath(__file__))
#logo_wupo = os.path.join('..', logo_dir, 'assets', 'wupo_logo.png')



app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div(
                html.A(
                    html.Div(
                        html.Img(
                            src=logo_wupo,
                            height="150px",
                            width="150px",
                        ),
                        #html.H1("Wupo"),
                        #style={
                        #    'fontSize': 30,
                        #    'textAlign': 'center', 
                        #    'color': 'gray', 
                        #    'margin-top': '0px'
                        #},
                        #className='text-center'
                    )
                ),
            style={
                'display': 'flex',
                'align-items': 'center',
                'justify-content': 'center',
                'margin-top': '-40px',
                'margin-bottom': '-25px'                                     
            }
            ),


                html.Div(
                    html.H2("Dash Board App"),
                        style={
                            'fontSize': 30,
                            'textAlign': 'center', 
                            'color': 'gray', 
                            'margin-top': '-50px'
                        },
                    className='text-center'   
                ),
                html.A(
                    html.P("https://www.wupealo.com"),
                        style={
                            'fontSize': 18,
                            'textAlign': 'center', 
                            'color': 'light-gray', 
                            'margin-top': '0px'
                           },
                      href="https://www.wupealo.com"   
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
