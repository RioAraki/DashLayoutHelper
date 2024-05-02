import collections
import dash_bootstrap_components as dbc
from dash import html
from .LayoutCSS import border_top, default_button_style

class LayoutHelper:

    def __init__(self):
        self.__current_row = 0
        self.__row_item_by_index = collections.defaultdict(list)
        self.__layout = []


    def header(self, level, text, width=None, **kwargs):
        header_dict = {
            1: 'H1',
            2: 'H2',
            3: 'H3',
            4: 'H4'
        }
        tag = header_dict.get(level, 'H1')  # Default to H1 if level is out of range
        header = getattr(html, tag)(text, **kwargs)
        self.__row_item_by_index[self.__current_row].append((header, width, None))


    def input(self, id, label, width=None, **kwargs):
        self.__row_item_by_index[self.__current_row].append(
            (dbc.Input(id=id, **kwargs), width, label)
        )


    def dropdown(self, id, label, width=None, **kwargs):
        self.__row_item_by_index[self.__current_row].append(
            (dbc.Select(id=id, **kwargs), width, label)
        )


    def radioitem(self, id, label, width=None, **kwargs):
        self.__row_item_by_index[self.__current_row].append(
            (dbc.RadioItems(id=id, **kwargs), width, label)
        )


    def checklist(self, id, label, width=None, **kwargs):
        self.__row_item_by_index[self.__current_row].append(
            (dbc.Checklist(id=id, **kwargs), width, label)
        )


    def button(self, id, text, width=None, **kwargs):
        self.__row_item_by_index[self.__current_row].append(
            (dbc.Button(text, id=id,**kwargs), width, None)
        )

    def new_row(self):
        self.__current_row += 1


    def get_layout(self):
        for index, row_items in self.__row_item_by_index.items():
            cur_row_list = []
            for col_index, item_width_label in enumerate(row_items): 
                if len(item_width_label) == 0:
                    continue
                item, width, label = item_width_label
                if label != None:
                    item = [dbc.Label(label)] + [item]

                ui_type = item.__class__.__name__
                print(ui_type)
                if ui_type == "Button":
                    cur_col = dbc.Col(children=item, width=width, id=f"row{index}col{col_index}", style=default_button_style)
                else:
                    cur_col = dbc.Col(children=item, width=width, id=f"row{index}col{col_index}")
                cur_row_list.append(cur_col)
            self.__layout.append(dbc.Row(cur_row_list, style=border_top(5)))
        return self.__layout
