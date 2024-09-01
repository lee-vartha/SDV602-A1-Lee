import PySimpleGUI as sg
from src import game_data
from src.command import parse_command
from src.utils import load_image

    
def make_a_window(game_state):
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """
    
    
    sg.theme('LightBlue4')  # please make your windows 
    layout = [
         [sg.Image(load_image('foyer.png'), size=(150, 150), key="-IMG-"),
          sg.Text(game_data.rooms[game_state['current_room']]['description'],
                  size=(100, 4), font='Any 12', key='-OUTPUT-')],
            [sg.Text('Enter command:', font='Any 10'), sg.Input(key='-IN-', size=(16, 1), font='Any 10')],
            [sg.Button('Enter', bind_return_key=True), sg.Button('Quit')],
            [sg.Text('Inventory:'), sg.Text('', size=(30, 2), key='-INVENTORY-')],
            [sg.Text('Health:'), sg.Text(game_state['health'], key='-HEALTH-')],
        ]
    return  sg.Window('The Haunted House', layout, size=(400,250))
    

if __name__ == "__main__":
    game_state = game_data.initial_game_state.copy()
    window = make_a_window(game_state)    

    while True:
        event, values = window.read()
        if event ==  'Enter': 
                command_result = parse_command(values['-IN-'], game_state)
                window['-OUTPUT-'].update(command_result)
                window['-IMG-'].update(load_image[game_state['current_room']]['description'])
                break
             
    window.close()