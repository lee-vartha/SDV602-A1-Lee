# importing the necessary libraries and classes
import PySimpleGUI as sg
from command_parser import CommandParser
from monster_fight import MonsterFight 
from inventory import Inventory
from status import Status 


if __name__ == "__main__":
    #Testing the classes

    #starting game state
    game_state = 'House'
    game_places = {
        'House':{ # the house (start of the game)
            'Story':'You\'ve been wandering for hours...\nYou discover a haunted house.\nYou can see a large door ahead...\n\n\nDo you want to enter the house? \n(Yes or No)',
            'Yes':'Foyer',
            'No':'Foyer',
            'Left':'',
            'Forward':'Foyer',
            'Image':'../images/house.png'
        },
        'Foyer':{ # the foyer
            'Story':'You find yourself in a grand foyer.\nThe door locked behind you.\nThere\'s two large doors to your\nleft and right.\nIn front of you is the hallway.\n\nYou hear sounds on your right...',
            'Left':'Dining',
            'Right':'Library',
            'Behind':'Front Door',
            'Forward':'Hallway',
            'Image':'../images/foyer.png'
        },
        'Front Door': { # the front door (can be escaped out of if a key is found)
            'Story':'You are at the front door.\nIt is locked.\nYou need a key to open it.\nTurn back around.',
            'Behind':'Foyer',
            'Right':'',
            'Left':'',
            'Forward':'',
            'Image':'../images/frontdoor.png'
        },
        'Dining': { # the dining room 
            'Story':'You are in the dining room.\nA large table is in the center,\nwith a tattered table cloth.\nBehind you is the foyer\nand to your right is the kitchen.',
            'Behind':'Foyer',
            'Right':'Kitchen',
            'Left':'',
            'Forward':'',
            'Image':'../images/dining.png'
        },
        'Library': { # the library (where the monster is)
            'Story':'',
            'Behind':'',
            'Right':'',
            'Forward':'',
            'Left':'',
            'Image':'../images/library.png'
        },
        'Kitchen': { # the kitchen (with weapon item)
            'Story':'You are at the Kitchen.\n\nThe smell of rotten food fills the air.\nTo the left is the dining room.\nYou picked up a teaspoon...\nfor extra security...?\n\n(Out of anything..why that??).\n\nTo your left is the dining room.',
            'Left':'Dining',
            'Right':'',
            'Forward':'',
            'Behind':'',
            'Item':'Teaspoon',
            'Image':'../images/kitchen.png'
        },
        'Hallway': { # the hallway
            'Story':'You are at the Hallway.\nIt feels endless to walk through.\nTo the left is the bedroom.\nTo the right is the bathroom.\nIn front of you is the living room.\nYou pick up some lint for good luck...',
            'Behind':'Foyer',
            'Right':'Bathroom',
            'Forward':'Living Room',
            'Left':'Bedroom',
            'Item':'Lint',
            'Image':'../images/hallway.png'
        },
        'Living Room': { # the living room
            'Story':'You are at the Living Room, a spacious area with a worn sofa that has seen better days.\nA big window casts lights in the room.\nTo the left, the hallway stretches out.',
            'Behind':'',
            'Right':'',
            'Forward':'',
            'Left':'Hallway',
            'Image':'../images/livingroom.png'
        },
        'Bedroom': { # in the bedroom (with weapon item)
            'Story':'You are at the Bedroom.\nTo the left is the hallway.\nYou hope for a shield...\n\nYou have picked up a pillow...?',
            'Behind':'Hallway',
            'Right':'',
            'Forward':'',
            'Left':'',
            'Item':'Pillow',
            'Image':'../images/bedroom.png'
        },
        'Bathroom': { # the bathroom (with weapon items)
            'Story':'You are at the Bathroom.\nIt is dark and damp.\nYou look in the bathtub and find a rusted key.\nBehind you is the hallway.\nYou have picked up a key!.',
            'Behind':'Hallway',
            'Right':'',
            'Forward':'',
            'Left':'',
            'Item':'Key',
            'Image':'../images/bathroom.png'}
        }

    command_parser = CommandParser(game_state, game_places) # calling the command parser
    status = Status() # calling the status
    inventory = Inventory() # calling the inventory
    monster_fight = MonsterFight(status, inventory) # calling the monster fight

def show_current_place():
    """Gets the story at the game_state place
    Returns:
        string: the story at the current place
    """
    global game_state  # getting the global game state

    return game_places[game_state]['Story'] # returns the story at the current place
 

def game_play(direction):
    """
    runs the game_play
    Args:
        direction (str: Forward, Behind, Left, Right (or 'leave')
    Returns:
        str: the story at the current place
    """
    global game_state # getting the global game state
    global monster_fight # getting the global monster fight
    global has_escaped # getting the global has_escaped boolean

    direction = direction.lower() # inputs are converted to lowercase


    if direction in ['forward', 'behind', 'left', 'right']: # if the direction is one of the four directions
        game_place = game_places[game_state] # update the game state
        proposed_state = game_place[direction.capitalize()] # proposed state is the direction the player wants to go
        if proposed_state == '' :  # if the state isnt valid
            return 'You can not go that way.\n\n'+game_places[game_state]['Story'] # returns message if the state isnt valid
        else :
            game_state = proposed_state # game state reflects where the player wants to go
            story = game_places[game_state]['Story']  # the story is updated based on the new game state
            item = game_places[game_state].get('Item')  # the items are updated based on the new game state
            if item:
                 inventory.pick_up(item) # if there is an item available, then it is automatically picked up

            if game_state == 'Front Door' and 'Key' in inventory.items: # if the player has the key and is at the front door
                has_escaped = True
                return 'Congratulations!\nYou have unlocked the door and escaped the haunted house!\nSay leave to exit the game.'

        if game_state == 'Library': # if the player enters the library (where monster is)
            return "\nOh no!!\nYou woke up an angry ghost!\nDo you want to fight it or run?\n(Fight or Run)"

        return story
    
    elif direction == 'fight':
            if game_state == 'Library':
                fight_result = monster_fight.start_fight()
                return f"\n{fight_result}\n\n{show_current_place()}"
            else:
                return "You must be seeing ghosts.."
        
    # elif direction == 'attack':
    #     if game_state == 'Library':
    #         fight_result = monster_fight.continue_fight()
    #         window['-OUTPUT-'].update(fight_result + '\n\n' + show_current_place())
    #         inventory_text = inventory.show_inventory()
    #         window['-INVENTORY-'].update(inventory_text)
    #         status_text = status.show_status()
    #         window['-STATUS-'].update(status_text)
    #     else:
    #         return "You must be seeing ghosts.."

    else:
         return 'I do not understand that command.\n\n'+game_places[game_state]['Story'] # otherwise if the user inputted something different, this is printed
    
has_escaped = False # sets the escape boolean to false


def make_a_window():
    """
    creates a game window

    returns:
        window: the handle to the game window
    """
    sg.theme('LightBlue3')     

    
    prompt_input = [sg.Text('Enter your command (Forward, Left, Right, Behind)',font='Any 8'),
                    sg.Input(key='-IN-',size=(50,5),font='Any 10', do_not_clear=False)]  # the prompt input where the user enters the command
    
    buttons = [sg.Button('Enter',  bind_return_key=True), sg.Button('Exit')]  # the buttons to enter and exit

    
    command_col = sg.Column([prompt_input,buttons],element_justification='right', pad=(10, 5))  # the column that stores the prompt input and buttons
    
    story_text = sg.Text(show_current_place(), size=(50,10), font='Any 8', key='-OUTPUT-',
                         text_color='black', pad=(10, 10), justification='left') # the story text and frame (for aesthetic)
    story_frame = sg.Frame('Story', [[story_text]], title_color='black', relief=sg.RELIEF_SUNKEN, element_justification='center', pad=(10, 10)) # the story text and frame (for aesthetic)

    
    layout = [[sg.Image(r'../images/house.png',size=(180,180),key="-IMG-"),  # aligning the layout of the GUI
               story_frame], 
            
             [sg.Text('Inventory:'), sg.Text('', size=(30, 1), key='-INVENTORY-')], # inventory and health status
             [sg.Text('Health:'), sg.Text('', size=(30, 1), key='-STATUS-')], # inventory and health status
             [sg.Text('', size=(-15, 10)), command_col]]
    
    
    return  sg.Window('The Haunted House', layout, size=(420,340), resizable=True) # returning a window with the layout

if __name__ == "__main__":
    # A persisent window - stays until "Exit" is pressed
    window = make_a_window()

    inventory_text = inventory.show_inventory() # show the inventory and status
    status_text = status.show_status()

    while True: # while the window is open
        event, values = window.read()

        inventory_text = inventory.show_inventory() # show the inventory and status
        status_text = status.show_status()

        window['-INVENTORY-'].update(inventory_text) # update the inventory in the window
        window['-STATUS-'].update({status.show_status()}) # update the status in the window
        window['-OUTPUT-'].update(show_current_place()) # update the story in the window
        window['-IMG-'].update(game_places[game_state]['Image'],size=(180,180))

        if event ==  'Enter': # if the user enters a command

                direction = values['-IN-'].strip().lower()
                if game_state == 'House' and direction in ['yes', 'no']:  # the player earlier gets asked if they want to go inside the house (prompted at the start of game)

                    if direction == 'yes': # if the player says yes then they are taken to the foyer

                        game_state = 'Foyer'
                        window['-OUTPUT-'].update(game_places['Foyer']['Story']) # game window is updated to show the foyer

                        window['-IMG-'].update(game_places['Foyer']['Image'], size=(180, 180))
                    elif direction == 'no':  # if the player says no then they are still taken to the foyer (something pushes them)
                        window['-OUTPUT-'].update('You still end up here\n..Something pushed you!\n\n' + game_places['Foyer']['Story'])
                        game_state = 'Foyer'
                        window['-IMG-'].update(game_places['Foyer']['Image'], size=(180, 180))
                    continue  # Skip the rest of the loop since we handled the input


                if direction in ['forward', 'behind', 'left', 'right']: # if the player enters a direction
                    current_story = game_play(direction) # current story is then updated
                    window['-OUTPUT-'].update(current_story)  # the window reflects any changes
                    window['-IMG-'].update(game_places[game_state]['Image'], size=(180,180)) # the images in the window are changed based on direction
                    inventory_text = inventory.show_inventory() # calling the inventory to be shown
                    window['-INVENTORY-'].update(inventory_text)  # updating the inventory in the window
                    status_text = status.show_status()  # calling the inventory to be shown
                    window['-STATUS-'].update(status_text)  # updating the status in the window

                    if has_escaped and direction == 'leave': # if the user 'leaves' through the door (if they have a key)
                        break  # the game ends

                    if "Congratulations" in current_story: # if the user has escaped
                        continue #skip the rest of the loop since the game has ended


                elif direction == 'run' and game_state == 'Library': # if they go into the library (where monster is) and choose to 'run'
                    window['-OUTPUT-'].update("You run back to the foyer..\nClosing the door behind you." + game_places['Foyer']['Story']) # returns message
                    game_state = 'Foyer'  # go back to foyer
                    window['-IMG-'].update(game_places['Foyer']['Image'], size=(180, 180))
                    continue

                elif direction == 'fight' and game_state == 'Library':
                    fight_result = monster_fight.start_fight()
                    if fight_result is None:
                        fight_result = "The fight ended with no result"
                    window['-OUTPUT-'].update(fight_result + '\n\n' + show_current_place())
                    inventory_text = inventory.show_inventory()
                    window['-INVENTORY-'].update(inventory_text)
                    status_text = status.show_status()
                    window['-STATUS-'].update(status_text)

                # elif direction == 'attack' and game_state == 'Library':
                #     fight_result = monster_fight.continue_fight()
                #     window['-OUTPUT-'].update(fight_result + '\n\n' + show_current_place())
                #     inventory_text = inventory.show_inventory()
                #     window['-INVENTORY-'].update(inventory_text)
                #     status_text = status.show_status()
                #     window['-STATUS-'].update(status_text)

                else:
                    window['-OUTPUT-'].update('I do not understand that command.\n'+ show_current_place()) # otherwise if the user inputted something idfferent, this is printed
                    
        elif event == 'Exit' or event is None or direction == 'leave' or event == sg.WIN_CLOSED: # if the user exits the game
            break
        
    window.close()

                     


