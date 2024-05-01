import dash
from dash import html, dcc
from dash.dependencies import Input, Output

# Create the Dash application instance
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Simple Dash App"),
    dcc.Input(id='input', value='Enter something here!', type='text'),
    html.Div(id='output')
])

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
