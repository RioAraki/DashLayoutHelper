border_10px = {
    'margin': '10px',  # Adds margin around the container
    'padding': '10px'  # Optional: adds padding inside the container
}

col_style_for_button = {
    "display": "flex",
    "align-items": "flex-end",
    "justify-content": "center",
}

def border_top(size):
    if not isinstance(size, int):
        size = 5
    return {
        'marginTop': f'{size}px',     
        'paddingTop': f'{size}px',   
    }
