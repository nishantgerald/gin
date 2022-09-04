#!/usr/bin/env python3
from datetime import datetime
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
from subprocess import run
import flask

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Pre-defined functions

def bash(command):
        run(command.split())

def quickadd_gitlab(n_clicks,user_ids):
    if n_clicks:
        bash(f"./quickadd-modules/quickadd-gitlab {user_ids}")

def quickadd_rstudio(n_clicks,user_ids):
    if n_clicks:
        bash(f"./quickadd-modules/quickadd-rstudio {user_ids}")

def quickadd_cluster(n_clicks,user_ids):
    if n_clicks:
        bash(f"./quickadd-modules/quickadd-cluster {user_ids}")

def quick_add_logs(n_clicks,user_ids,service_name):
    if n_clicks:
        with open('quickadd-modules/quickadd.log', mode='a+') as log_file:
            for user in user_ids.split():
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                message=f"{dt_string}\t{user} was added to {service_name}"
                print(message,file=log_file)

#Dash App
#server = flask.Flask(__name__)

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = 'Gin Scorekeeper'

app.layout = html.Div([
    html.H4("Gin Scorekeeper", style={'color':'#fff' ,'backgroundColor':'#005EAA','borderRadius': '5px',"padding":"6px"}),

    # GETTING PLAYER 1 NAME
    html.P("Add name for Player 1",style={"text-decoration": "underline"}),
    html.Div(dcc.Input(id='FNAME1-input', type='text',placeholder="Jane Doe",)),
    html.Div(id='FNAME1-output'),

    html.Br(),

    # GETTING PLAYER 2 NAME
    html.P("Add name for Player 2",style={"text-decoration": "underline"}),
    html.Div(dcc.Input(id='FNAME2-input', type='text',placeholder="John Doe",)),
    html.Div(id='FNAME2-output'),
    html.Br(),
    html.Button('Onboard!', id='button',style={'backgroundColor': '#005EAA', 'color':'white'}),
])

@app.callback(
    Output(component_id="dd-output", component_property='children'),
    Input(component_id='dd-input', component_property='value')
)
def update_output_div(service_name):
    return (f"Service: {service_name}")

#This is the callback for when the onboard button is clicked
@app.callback(
    Output(component_id="text-output", component_property='children'),
    Input('button', 'n_clicks'),
    State(component_id='text-input', component_property='value'),
    State(component_id='dd-input', component_property='value')
)
def update_output_div(n_clicks,user_ids,service_name):
    if (service_name=="ldap"):
        quickadd_ldap(n_clicks,user_ids)
        quick_add_logs(n_clicks,user_ids,service_name)
    elif (service_name=="rstudio"):
        quickadd_rstudio(n_clicks,user_ids)
        quick_add_logs(n_clicks,user_ids,service_name)
    elif (service_name=="gitlab"):
        quickadd_gitlab(n_clicks,user_ids)
        quick_add_logs(n_clicks,user_ids,service_name)
    elif (service_name=="cluster"):
        quickadd_cluster(n_clicks,user_ids)
        quick_add_logs(n_clicks,user_ids,service_name)
    return (f"Users: {user_ids}")

if __name__ == '__main__':
    context = ('/etc/pki/tls/certs/scbs-automate-dev-01.biotech.cdc.gov.crt','/etc/pki/tls/private/scbs-automate-dev-01.biotech.cdc.gov.key')
    app.run_server(host='localhost',debug=True)
    #app.run_server(debug=True)