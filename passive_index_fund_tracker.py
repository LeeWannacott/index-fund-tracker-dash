import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash('Passive index funds')

list_of_options = [
    {'label': 'Vanguard Emerging markets', 'value': 'VGE.AX'},
    {'label': 'Vanguard Diversified Growth', 'value': 'VDGR.AX'},
    {'label': 'Vanguard Diversified High Growth Index ETF', 'value': 'VDHG.AX'},
    {'label': 'Vanguard MSCI Index International Shares ETF ', 'value': 'VGS.AX'},
    {'label': 'Vanguard MSCI International Small Companies Index', 'value': 'VISM.AX'},
    {'label': 'Vanguard All-World ex-US Shares Index ETF ', 'value': 'VEU.AX'},
    {'label': 'Vanguard MSCI Index International Shares (Hedged)', 'value': 'VGAD.AX'},
    {'label': 'Vanguard Australian Shares Index', 'value': 'VAS.AX'},
    {'label': 'Vanguard MSCI Australian Small Companies Index', 'value': 'VSO.AX'},
    {'label': 'Vanguard U.S. Total Market Shares Index', 'value': 'VTS.AX'},
    {'label': 'Vanguard FTSE Europe Shares', 'value': 'VEQ.AX'},
    {'label': 'Vanguard FTSE Asia ex Japan Shares Index ', 'value': 'VAE.AX'}
]

app.layout = html.Div([
    html.H1('Vanguard passive index funds'),
    dcc.Dropdown(
        id='dropdown1',
        options=list_of_options,
        value=list_of_options[0]['value']
    ),
    dcc.Graph(id='graph1'),

    dcc.Dropdown(
        id='dropdown2',
        options=list_of_options,
        value=list_of_options[1]['value']
    ),
    dcc.Graph(id='graph2'),

    dcc.Dropdown(
        id='dropdown3',
        options=list_of_options,
        value=list_of_options[2]['value']
    ),
    dcc.Graph(id='graph3'),

    dcc.Dropdown(
        id='dropdown4',
        options=list_of_options,
        value=list_of_options[3]['value']
    ),
    dcc.Graph(id='graph4'),

    dcc.Dropdown(
        id='dropdown5',
        options=list_of_options,
        value=list_of_options[4]['value']
    ),
    dcc.Graph(id='graph5'),

    dcc.Dropdown(
        id='dropdown6',
        options=list_of_options,
        value=list_of_options[5]['value']
    ),
    dcc.Graph(id='graph6'),

    dcc.Dropdown(
        id='dropdown7',
        options=list_of_options,
        value=list_of_options[6]['value']
    ),
    dcc.Graph(id='graph7'),

    dcc.Dropdown(
        id='dropdown8',
        options=list_of_options,
        value=list_of_options[7]['value']
    ),
    dcc.Graph(id='graph8'),

    dcc.Dropdown(
        id='dropdown9',
        options=list_of_options,
        value=list_of_options[8]['value']
    ),
    dcc.Graph(id='graph9'),

    dcc.Dropdown(
        id='dropdown10',
        options=list_of_options,
        value=list_of_options[9]['value']
    ),
    dcc.Graph(id='graph10'),

    dcc.Dropdown(
        id='dropdown11',
        options=list_of_options,
        value=list_of_options[10]['value']
    ),
    dcc.Graph(id='graph11'),

    dcc.Dropdown(
        id='dropdown12',
        options=list_of_options,
        value=list_of_options[11]['value']
    ),
    dcc.Graph(id='graph12')],


    style={'width': '500', 'display': 'block'})



@app.callback(Output('graph1', 'figure'), [Input('dropdown1', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2010, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 50,'r': -100, 't': 20, 'b': 30}}
    }

@app.callback(Output('graph2', 'figure'), [Input('dropdown2', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2010, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 50,'r': -100, 't': 20, 'b': 30}}
    }

@app.callback(Output('graph3', 'figure'), [Input('dropdown3', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2010, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 50,'r': -100, 't': 20, 'b': 30}}
    }

@app.callback(Output('graph4', 'figure'), [Input('dropdown4', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2010, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 50,'r': -100, 't': 20, 'b': 30}}
    }

@app.callback(Output('graph5', 'figure'), [Input('dropdown5', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2010, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 50,'r': -100, 't': 20, 'b': 30}}
    }

@app.callback(Output('graph6', 'figure'), [Input('dropdown6', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2010, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 50,'r': -100, 't': 20, 'b': 30}}
    }

@app.callback(Output('graph7', 'figure'), [Input('dropdown7', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2010, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 50,'r': -100, 't': 20, 'b': 30}}
    }

@app.callback(Output('graph8', 'figure'), [Input('dropdown8', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2010, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 50,'r': -100, 't': 20, 'b': 30}}
    }

@app.callback(Output('graph9', 'figure'), [Input('dropdown9', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2010, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 50,'r': -100, 't': 20, 'b': 30}}
    }

@app.callback(Output('graph10', 'figure'), [Input('dropdown10', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2010, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 50,'r': -100, 't': 20, 'b': 30}}
    }

@app.callback(Output('graph11', 'figure'), [Input('dropdown11', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2010, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 50,'r': -100, 't': 20, 'b': 30}}
    }

@app.callback(Output('graph12', 'figure'), [Input('dropdown12', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2010, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 50,'r': -100, 't': 20, 'b': 30}}
    }


app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(debug=True)
