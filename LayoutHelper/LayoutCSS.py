border_10px = {
    'margin': '10px',  # Adds margin around the container
    'padding': '10px'  # Optional: adds padding inside the container
}

def border_top(size):
    if not isinstance(size, int):
        size = 5
    return {
        'margin-top': f'{size}px',     
        'padding-top': f'{size}px',   
    }
