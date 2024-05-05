border_10px = {
    'margin': '10px',  # Adds margin around the container
    'padding': '10px'  # Optional: adds padding inside the container
}

col_style_for_button = {
    "display": "flex",
    "align-items": "flex-end",
    "justify-content": "center",
}


group_input_border_style = {
    'border': '1px solid #ccc',  # Adds a light gray border
    'border-radius': '10px',  # Rounds the corners of the border
    'box-shadow': '0 2px 4px 0 rgba(0, 0, 0, 0.2)',  # Adds a shadow
    'padding': '10px',  # Adds space inside the div around the content
    'margin': '10px'  # Adds space outside the div
}

group_input_button_style = {
    'margin-right': '10px'
}

def border_top(size):
    if not isinstance(size, int):
        size = 5
    return {
        'marginTop': f'{size}px',     
        'paddingTop': f'{size}px',   
    }
