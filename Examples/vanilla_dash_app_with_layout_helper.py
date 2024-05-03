import dash
import dash_bootstrap_components as dbc
import pandas as pd

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

data = {
    'State': ['California', 'Arizona', 'Nevada', 'New Mexico', 'Colorado', 'Texas', 'North Carolina', 'New York'],
    'Number of Solar Plants': [289, 48, 11, 33, 20, 12, 148, 13],
    'Installed Capacity (MW)': [4395, 1078, 238, 261, 118, 187, 669, 53],
    'Average MW Per Plant': [15.3, 22.5, 21.6, 7.9, 5.9, 15.6, 4.5, 4.1],
    'Generation (GWh)': [10826, 2550, 557, 590, 235, 354, 1162, 84]
}

# Converting the dictionary to a DataFrame
df = pd.DataFrame(data)

helper.table(df)


app.layout = helper.get_layout()


# Define callback to update the output based on user input

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
