from src import game_data
from src.monster_fight import MonsterFight
from src.inventory import add_item, show_inventory
from src.status import show_status

def parse_command(command, game_state):
    """Parse the command and direct the game state accordingly.
    
    Args:  
        command (str): The command entered by the user.
        game_state (dict): The current state of the game.

    Returns:
        dict: The updated game state.
    """

    command = command.lower().strip();

    if command in ['north', 'south', 'east', 'west']:
        return move_player(command, game_state)
    elif command == 'inventory':
        return show_inventory(game_state)
    elif command == 'status':
        return show_status(game_state)
    elif command == 'fight':
        return MonsterFight(game_state)
    elif command == 'quit':
        game_state['game_over'] = True
        return game_state
    else:
        return game_state 
    
def move_player(direction, game_state):
    """Move the player in the specified direction.
    
    Args:
        direction (str): The direction in which to move the player.
        game_state (dict): The current state of the game.

    Returns:
        dict: The updated game state.
    """

    player = game_state['player']
    current_room = game_state['current_room']
    next_room = game_data.rooms[current_room][direction]

    if next_room is None:
        print("You can't go that way.")
        return game_state
    else:
        player['current_room'] = next_room
        game_state['current_room'] = next_room
        return game_state


if __name__ == "__main__":

    test_game_state = game_data.initial_game_state.copy()
    print(parse_command('north', test_game_state))
    print(parse_command('inventory', test_game_state))
    print(parse_command('status', test_game_state))