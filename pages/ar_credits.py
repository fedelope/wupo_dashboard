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




dash.register_page(__name__, path='/pages/ar_credits', name='Créditos') # '/' is home page

# page_1 - Macro data
df = pd.read_csv("/Users/federico/Documents/Coding/python/interactive_kpi/dash_env/lib/python3.8/site-packages/auto_KPI_app/data/kpi_platicapp.csv")
print(df[:15])

# converts date_data into pandas format 
df['LOANDATE'] = pd.to_datetime(df['LOANDATE'], format='%d/%m/%y')

min_date = df['LOANDATE'].min()
max_date = df['LOANDATE'].max()

# create rows and columns
layout = dbc.Container([ 

    # Graph_1 Macro_Data/Credito_por_periodo

    dbc.Row([
        dbc.Col([
            html.P("Créditos por Periodo", className="control_label"),
          # graph_1 'count' creditos
            dcc.Graph(
                id = 'count_credits',
                figure = {
                'layout': {
                    'xaxis': {'range': [min_date, max_date]},
                    'yaxis': {'title': 'Conteo Créditos'}
                }}, 
                config = {"displaylogo": False},
                style={'display': 'inline-block', 'margin-left': '-5px'},       
            )
        ]),            
        dbc.Col([
            # check list para periodos de tiempo
            html.P("Periodo créditos: ", style={'textAlign': 'start'}),            
            dcc.Checklist(                        
                options = [{"label": str(val), "value": val} for val in [8, 14, 16, 21]], 
                value=[8, 14, 16, 21],
                id = 'periodo_credito',
                style={'display': 'inline-block'}    
            ),
        dbc.Row([
            html.P("\n\n\n")
        ]),
            # radio item para time frame
            html.P("Agregar data: ", style={'textAlign': 'start'}),            
            dcc.RadioItems(                        
                options = [
                    {"label": "Día" , "value": "D"},
                    {"label": "Mes" , "value": "M"}    
                ], 
                value='D',
                id = 'time_frame'
                #inputStyle={'margin-left': '0px'},
                #style={'display': 'inline-block', 'margin-left': '0px}'},
                #labelStyle={'display': 'inline-block'}
            )
                # ], width={'size': 6}, style={"display": 'inline-block', 'margin-left': '10px'}
        ])                    
    ]), #, style={"display": 'inline-block', "align": 'start'})


    # Graph_2 Macro_Data/Credito_por_periodo_cumulative
    dbc.Row([
        dbc.Col([
            html.P("Créditos por Periodo - Acumulado", className="control_label"),
          # graph_2 'count' creditos - cumulative
            dcc.Graph(
                id = 'count_credits_cumulative',
                config = {"displaylogo": False},
                figure = {}, 
                style={'display': 'inline-block', 'margin-left': '-5px'}               
            )
        ]),            
        dbc.Col([
            # check list para periodos de tiempo
            html.P("Periodo créditos: ", style={'textAlign': 'start'}),            
            dcc.Checklist(                        
                options = [{"label": str(val), "value": val} for val in [8, 14, 16, 21]], 
                value=[8, 14, 16, 21],
                id = 'periodo_credito_cumulative',
                style={'display': 'inline-block'}    
            ),
        dbc.Row([
            html.P("\n\n\n")
        ]),
            # radio item para time frame
            html.P("Agregar data: ", style={'textAlign': 'start'}),            
            dcc.RadioItems(                        
                options = [
                    {"label": "Día" , "value": "D"},
                    {"label": "Mes" , "value": "M"}    
                ], 
                value='D',
                id = 'time_frame_cumulative'
                #inputStyle={'margin-left': '0px'},
                #style={'display': 'inline-block', 'margin-left': '0px}'},
                #labelStyle={'display': 'inline-block'}
            )
                # ], width={'size': 6}, style={"display": 'inline-block', 'margin-left': '10px'}
        ])                    
    ]) #, style={"display": 'inline-block', "align": 'start'})
])

        
# Chart_1 - Credit quantity histogram 
@callback(
    # TERM callback
    Output('count_credits', 'figure'),
    Input('periodo_credito', 'value'),
    # time_frame callback
    Input('time_frame', 'value')
)


#define Callback function
def time_frame_1(term_selected, aggregation_type):
        # extract data to data_frame
    df_term_date = df[['TERM', 'LOANDATE']]
    #print(type(df))
    
    # make a copy of the data
    df_term_date_c = df_term_date.copy()
    # converts date_data into pandas format 
    df_term_date_c['LOANDATE'] = pd.to_datetime(df_term_date['LOANDATE'], format='%d/%m/%y')
    # takes date information to first colum as index
    df_term_date_index = df_term_date_c.set_index('LOANDATE')
    #print(df_term_date_index)
    
    #df_date = df_term_date_index.groupby(['TERM', pd.Grouper(freq=aggregation_type)]).size()
    df_date = df_term_date_index[df_term_date_index['TERM'].isin(term_selected)].groupby(['TERM', pd.Grouper(freq=aggregation_type)]).size()
    #print("1: ")
    #print(df_date)
    df_date = df_date.reset_index(name='creditos')
    #print("2: ")
    #print(df_date)
    # takes date information to first colum as index
    df_date_index = df_date.set_index(['TERM','LOANDATE'])

    
    # Identify start and end date, an total days. 
    min_date = df_date['LOANDATE'].min()
    max_date = df_date['LOANDATE'].max()
    num_days = int((max_date - min_date).days)
    num_months = int(num_days/30)
    #print("months: " + str(num_months))
    
    print("min_date: " + str(min_date))
    print("max_date: " + str(max_date))
    print("total days: " + str(num_days))
    print("total months: " + str(num_months))
    #print(df_date)
    #print(df_date)
    #print("total months: " + str(num_months))
    #print(df_date)
    #print(df_date)

    #print("Este es term selected" + str(term_selected))
    #print("term_selected: " + str(term_selected))
    if aggregation_type == 'D':
        #print("if_check_D: " + str(num_days))
        num_bins=num_days
    if aggregation_type == 'M':
        #print("if_check_M: " + str(num_days))
        num_bins=num_months


    graph_1 = px.histogram(df_date, 
        x='LOANDATE', 
        y='creditos',
        color='TERM',
        histfunc='sum',
        barmode='stack',        
        nbins=num_bins,
        color_discrete_sequence=px.colors.qualitative.Plotly, 
        #facet_col='TERM',
        #facet_col_spacing='0.2'
        #title='Periodos Créditos'
        )
    
    graph_1.update_traces(
        opacity=0.75)
    
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


# Chart_2 - Credit quantity histogram - cumulative
@callback(
    # TERM callback
    Output('count_credits_cumulative', 'figure'),
    Input('periodo_credito_cumulative', 'value'),
    # time_frame callback
    Input('time_frame_cumulative', 'value')
)


#define Callback function
def time_frame_2(term_selected, aggregation_type):
        # extract data to data_frame
    df_term_date = df[['TERM', 'LOANDATE']]
    #print(type(df))
    
    # make a copy of the data
    df_term_date_c = df_term_date.copy()
    # converts date_data into pandas format 
    df_term_date_c['LOANDATE'] = pd.to_datetime(df_term_date['LOANDATE'], format='%d/%m/%y')
    # takes date information to first colum as index
    df_term_date_index = df_term_date_c.set_index('LOANDATE')
    #print(df_term_date_index)
    
    #df_date = df_term_date_index.groupby(['TERM', pd.Grouper(freq=aggregation_type)]).size()
    df_date = df_term_date_index[df_term_date_index['TERM'].isin(term_selected)].groupby(['TERM', pd.Grouper(freq=aggregation_type)]).size()
    #print("1: ")
    #print(df_date)
    df_date = df_date.reset_index(name='creditos')
    #print("2: ")
    #print(df_date)
    # takes date information to first colum as index
    df_date_index = df_date.set_index(['TERM','LOANDATE'])
    
    # Identify start and end date, an total days. 
    min_date = df_date['LOANDATE'].min()
    max_date = df_date['LOANDATE'].max()

    num_days = int((max_date - min_date).days)
    num_months = int(num_days/30)
    #print("months: " + str(num_months))
    

    print("total days: " + str(num_days))
    print("total months: " + str(num_months))
    #print(df_date)
    #print(df_date)
    #print("total months: " + str(num_months))
    #print(df_date)
    #print(df_date)

    #print("Este es term selected" + str(term_selected))
    #print("term_selected: " + str(term_selected))
    if aggregation_type == 'D':
        #print("if_check_D: " + str(num_days))
        num_bins=num_days
    if aggregation_type == 'M':
        #print("if_check_M: " + str(num_days))
        num_bins=num_months


    graph_2 = px.histogram(df_date, 
        x='LOANDATE', 
        y='creditos',
        color='TERM',
        histfunc='sum',
        barmode='stack',        
        nbins=num_bins,
        cumulative=True,
        color_discrete_sequence=px.colors.qualitative.Set3,
        #facet_col='TERM',
        #facet_col_spacing='0.2'
        #title='Periodos Créditos'
        )
    graph_2.update_traces(
        opacity=0.75)
    
    graph_2.update_layout(
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

    return graph_2