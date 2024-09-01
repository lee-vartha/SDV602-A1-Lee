import random
def fight_monster(game_state):
    """Fight a monster in the current room.
    
    Args:
        game_state (dict): The current state of the game.
        
    Returns:
        dict: The updated game state.
    """

    current_room = game_state['current_room']
    if game_state.get('monster', False) and random.choice([True, False]):
        game_state['health'] -= 10
        return f"You were attacked by a monster in the {current_room} and your health is at {game_state['health']}."
    else:
        return f"No monster in the {current_room}."


if __name__ == "__main__":
    test_game_state = {'current_place': 'Kitchen', 'monster': True, 'health': 100, 'inventory': set()}
    print(fight_monster(test_game_state))
    print(fight_monster(test_game_state))