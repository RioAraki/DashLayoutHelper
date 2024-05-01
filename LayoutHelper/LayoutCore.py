import collections
import dash_bootstrap_components as dbc
from dash import html
from .LayoutCSS import border_top

class LayoutHelper:

    def __init__(self):
        self.__current_row = 0
        self.__row_item_by_index = collections.defaultdict(list)
        self.__layout = []

    def input(self, id, width=None, **kwargs):
        self.__row_item_by_index[self.__current_row].append(
            (dbc.Input(id=id, **kwargs), width)
        )

    def header(self,level, text, width=None, **kwargs):
        if level not in [1,2,3,4]:
            level = 1

        self.__row_item_by_index[self.__current_row].append(
            
        )

    # def dropdown(
    #         self, 
    #         id, 
    #         options=[], 
    #         value= "", 
    #         class_name="",
    #         width=None):
    #     pass

    def new_row(self):
        self.__current_row += 1

    def get_layout(self):
        for index, row_items in self.__row_item_by_index.items():
            cur_row_list = []
            for col_index, (item, width) in enumerate(row_items): 
                cur_col = dbc.Col(children=item, width=width, id=f"row{index}col{col_index}")
                cur_row_list.append(cur_col)
            self.__layout.append(dbc.Row(cur_row_list, style=border_top(5)))
        return self.__layout
