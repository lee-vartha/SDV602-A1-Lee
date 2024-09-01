""" 
A comment describing the game module
"""
import PySimpleGUI as sg

# Brief comment about how the following lines work
game_state = 'Foyer'
game_places = {'Foyer':{'Story':'You are in the foyer.\nTo the north is a dining room.\nTo the south is a library',
                        'North':'Dining','South':'Library','Image':'foyer.png'},
              'Dining':{'Story':'You are in the dining room.\nTo the south is the foyer.',
                        'North':'','South':'Foyer','Image':'dining.png'},
              'Library':{'Story':'You are at the Library.\nTo the north is foyer.',
                        'North':'Foyer','South':'','Image':'library.png'},
                }

def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state
    
    return game_places[game_state]['Story']

def game_play(direction):
    """
    Runs the game_play

    Args:
        direction string: _North or South

    Returns:
        string: the story at the current place
    """
    global game_state
    
    if direction.lower() in 'northsouth': # is this a nasty check?
        game_place = game_places[game_state]
        proposed_state = game_place[direction]
        if proposed_state == '' :
            return 'You can not go that way.\n'+game_places[game_state]['Story']
        else :
            game_state = proposed_state
            return game_places[game_state]['Story']
        
    
def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """
    
    
    sg.theme('LightBlue4')  # please make your windows 
    prompt_input = [sg.Text('Enter your command',font='Any 10'),sg.Input(key='-IN-',size=(16,1),font='Any 10')]
    buttons = [sg.Button('Enter',  bind_return_key=True), sg.Button('Exit')]
    command_col = sg.Column([prompt_input,buttons],element_justification='r')
    layout = [[sg.Image(r'foyer.png',size=(150,150),key="-IMG-"), sg.Text(show_current_place(),size=(100,4), font='Any 12', key='-OUTPUT-')],
             [command_col]]
    
    [sg.Text('Inventory:'),
     sg.Text('', size=(30, 2), key='-INVENTORY-')],
    

    return  sg.Window('The Haunted House', layout, size=(400,250))
    

if __name__ == "__main__":
    #testing for now
    # print(show_current_place())
    # current_story = game_play('North')
    # print(show_current_place())
    
    # A persisent window - stays until "Exit" is pressed
    window = make_a_window()

    while True:
        event, values = window.read()
        print(event)
        if event ==  'Enter': 
                if 'North'.lower() in values['-IN-'].lower():
                    current_story = game_play('North')
                    window['-OUTPUT-'].update(current_story)
                elif 'South'.lower() in values['-IN-'].lower():
                    current_story = game_play('South')
                    window['-OUTPUT-'].update(current_story)
                
                window['-IMG-'].update(game_places[game_state]['Image'],size=(120,120))
                pass
        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
                break
        else :
                pass
             
    window.close()