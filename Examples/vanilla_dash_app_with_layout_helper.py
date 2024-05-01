import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from LayoutHelper.LayoutCore import LayoutHelper
from LayoutHelper.LayoutCSS import border_10px

# Create the Dash application instance
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

helper = LayoutHelper()

helper.header(level=4, text="This is 4 of the app")

helper.new_row()

helper.input(id="age")
helper.input(id="gender")

helper.new_row()

helper.input(id="name")

app.layout = dbc.Container(helper.get_layout(), fluid=True, style=border_10px)

# Define callback to update the output based on user input

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
