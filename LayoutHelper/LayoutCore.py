import collections
import dash_bootstrap_components as dbc

from dash import html, dcc, dash_table, Input, Output, State
from dash.exceptions import PreventUpdate
from .LayoutCSS import border_top, col_style_for_button, group_input_border_style, group_input_button_style


class LayoutHelper:
    _current_row = 0
    # key: row_index
    # value: (actual content, width, label above it if applicable)
    _row_item_by_index = collections.defaultdict(list)
    _layout = []

    class GroupInput:
        def __init__(self, app, id):
            self.app = app
            self.id = id
            self._current_row = 0
            self._single_group = collections.defaultdict(list)
            self.addButton = dbc.Button(f"Add {id}", id=f"add_{id}", style=group_input_button_style)
            self.removeButton = dbc.Button(f"Remove {id}", id=f"remove_{id}", color="danger", style=group_input_button_style)

            self._final_layout = html.Div(id=f"input_group_{id}", children = [self.addButton, self.removeButton], style=group_input_border_style)
            
            LayoutHelper._row_item_by_index[LayoutHelper._current_row].append(
                (self._final_layout, None, None)
            )

            self.add_button_callback()

        def add_button_callback(self):
            @self.app.callback(
                Output(f"input_group_{self.id}", "children"),
                Input(f"add_{self.id}", "n_clicks"),
                State(f"input_group_{self.id}", "children"),
                prevent_initial_call = True
            )
            def add_single_group(n_clicks, layout):
                if n_clicks is None:
                    raise PreventUpdate
                print("triggered")
                return layout

    def __init__(self, app):
        self.app = app

    def group_input(self, id):
        return self.GroupInput(self.app, id)


    def header(self, level, text, width=None, **kwargs):
        header_dict = {
            1: 'H1',
            2: 'H2',
            3: 'H3',
            4: 'H4'
        }
        tag = header_dict.get(level, 'H1')  # Default to H1 if level is out of range
        header = getattr(html, tag)(text, **kwargs)
        self._row_item_by_index[self._current_row].append((header, width, None))


    def input(self, id, label=None, width=None, group_input=None, **kwargs):
        if group_input:
            group_input._single_group[group_input._current_row].append(
                (dbc.Input(id=id, **kwargs), width, label)
            )
        else:
            self._row_item_by_index[self._current_row].append(
                (dbc.Input(id=id, **kwargs), width, label)
            )


    def dropdown(self, id, label=None, width=None, **kwargs):
        self._row_item_by_index[self._current_row].append(
            (dcc.Dropdown(id=id, **kwargs), width, label)
        )


    def radioitem(self, id, label=None, width=None, **kwargs):
        self._row_item_by_index[self._current_row].append(
            (dbc.RadioItems(id=id, **kwargs), width, label)
        )


    def checklist(self, id, label=None, width=None, **kwargs):
        self._row_item_by_index[self._current_row].append(
            (dbc.Checklist(id=id, **kwargs), width, label)
        )


    def button(self, id, text, width=None, **kwargs):
        self._row_item_by_index[self._current_row].append(
            (dbc.Button(text, id=id,**kwargs), width, None)
        )

    def new_row(self):
        self._current_row += 1


    def separator(self):
        self.new_row()
        self._row_item_by_index[self._current_row].append(
            (html.Hr(), 12, None)
        )
        self.new_row()


    def table(self, df, label=None, width=None, **kwargs):
        self._row_item_by_index[self._current_row].append(
            (dash_table.DataTable(df.to_dict("records"), **kwargs), width, label)
        )

        
    def graph(self):
        pass

    def get_layout(self):
        for index, row_items in self._row_item_by_index.items():
            cur_row_list = []
            for col_index, item_width_label in enumerate(row_items):
                # print(f"index, col_index, item_width_label: {index},{col_index},{item_width_label}") 
                if len(item_width_label) == 0:
                    continue
                item, width, label = item_width_label
                ui_type = item.__class__.__name__

                if label != None:
                    item = [dbc.Label(label)] + [item]
                else:
                    item = [html.Br()] + [item]
                # print(ui_type)
                if ui_type == "Button":
                    cur_col = dbc.Col(children=item, width=width, id=f"row{index}col{col_index}", style=col_style_for_button)
                else:
                    cur_col = dbc.Col(children=item, width=width, id=f"row{index}col{col_index}")
                cur_row_list.append(cur_col)
            self._layout.append(dbc.Row(cur_row_list, style=border_top(5)))

        self._layout = dbc.Container(
            children=self._layout,
            fluid=False,
        )

        return self._layout
