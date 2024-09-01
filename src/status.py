def show_status(game_state):
    """Display the player's status.
    
    Args:
        game_state (dict): The current state of the game.
        
    Returns:
        dict: The updated game state.
    """

    return f"Health: {game_state['health']}, Current Room: {game_state['current_room']}"

if __name__ == "__main__":
    test_game_state = {'health': 100, 'inventory': {'key', 'book'}}
    print(show_status(test_game_state))