import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Create the Dash application instance
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Simple Dash App", className="text-center"), width=12)
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Input(id='input', placeholder='Enter something here!', type='text')
        )
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='output', className="text-center"), width=6)
    ])
], fluid=False, className="")  # Add padding on the left and right sides

# Define callback to update the output based on user input
@app.callback(
    Output('output', 'children'),
    [Input('input', 'value')]
)
def update_output(input_value):
    return f'You entered: {input_value}'

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
