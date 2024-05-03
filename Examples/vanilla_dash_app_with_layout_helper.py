import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from  LayoutHelper.LayoutCore import LayoutHelper
from LayoutHelper.LayoutCSS import border_10px

# Create the Dash application instance
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

helper = LayoutHelper()

helper.header(level=4, text="This is H4")

helper.new_row()

helper.input(id="age", label="input age")
helper.input(id="gender", label="gender")
helper.radioitem(
    id="radio", 
    label="select", 
    options=[
        {"label": "option1", "value": 1},
        {"label": "option2", "value": 2},
        {"label": "option3", "value": 3},
    ],
    inline=True
)
helper.checklist(
    id="checklist", 
    label="this is a checklist", 
    options=[
        {"label": "option1", "value": 1},
        {"label": "option2", "value": 2},
    ],
    value=[1],
    switch=True,
    inline=True
)

helper.new_row()

helper.input(id="name", label="name")
helper.dropdown(id="dropdown", label="dropdown", options=["choose", "anything"], multi=True)
helper.button(id="button", text="Submit Graph")

helper.separator()


app.layout = helper.get_layout()


# Define callback to update the output based on user input

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
