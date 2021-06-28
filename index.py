import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc 
import dash_html_components as html
import dash_table

from pandas_datareader import data as web 
from datetime import datetime as dt



app = dash.Dash('Hello World',
                external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([

    html.H1("Aktienkurs-Analyse",style={ # in HTML kann direkt mit CSS gearbeitet werden
        'textAlign': 'center'
    }),

    # dcc.Dropdown(
    #     id='my-dropdown',
    #     options=[
    #         {'label': 'Coke', 'value': 'COKE'},
    #         {'label': 'Tesla', 'value': 'TSLA'},
    #         {'label': 'Apple', 'value': 'AAPL'},
    #         {'label': 'Amazon', 'value':'AMZN'}
    #     ],  
    #     value='COKE'
    # ),

    html.Div(["Aktien-Tickersymbol: ",
              dcc.Input(id='my-input', value='AMZN', type='text')]),
    
    html.Button('Update', id='update-button', style={
        'margin-bottom': '0rem',
        'position': 'relative',
        'left': '380px',
        'bottom': '38px'
}),

    dcc.Graph(id='my-graph')

    
], style={'width': '500'})

# Callback Graph
@app.callback(Output('my-graph', 'figure'),[Input('update-button', 'n_clicks')], state=[State(component_id='my-input', component_property='value')])
def update_graph(n_clicks, input_value): # n_clicks wird trotzdem übergeben, ka warum -> nachgehen
    df = web.DataReader(
        input_value,
        'yahoo',
        dt(2015, 1, 1),
        dt.now()
    )
      
    return {
        'data': [{ # entspricht den Komponenten von 'figure' -> Graph
            'x': df.index,
            'y': df.Close
        }]
        ,
        'layout': {'title': input_value + '-Close','margin': {'l': 40, 'r': 0, 't': 80, 'b': 30}}
    } 

if __name__ == '__main__':
    app.run_server(debug=True)