def add_item(game_state, item):
    """Add an item to the player's inventory.
    
    Args:
        game_state (dict): The current state of the game.
        item (str): The item to add to the inventory.
        
        Returns:
            dict: The updated game state.
    """

    game_state['inventory'].add(item)


def show_inventory(game_state):
    """Display the player's inventory.

    Args:
        game_state (dict): The current state of the game.

    Returns:
        dict: The updated game state.
    """

    if game_state['inventory']:
        return f"Inventory: {', '.join(game_state['inventory'])}"
    else:
        return "Inventory is empty."