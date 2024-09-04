import PySimpleGUI as sg
from command_parser import CommandParser
from monster_fight import MonsterFight 
from inventory import Inventory
from status import Status 


if __name__ == "__main__":
    game_state = 'House'
    game_places = {
        'House':{
            'Story':'You\'ve been wandering for hours...\nYou discover a haunted house.\nYou can see a large door ahead...\n\n\nDo you want to enter the house?',
            'Yes':'Foyer',
            'No':'Foyer',
            'Left':'',
            'Forward':'Foyer',
            'Image':'../images/house.png'
        },
        'Foyer':{
            'Story':'You find yourself in a grand foyer.\nThe door locked behind you.\nThere\'s two large doors to your\nleft and right.\nIn front of you is the hallway.\n\nYou hear sounds on your right...',
            'Left':'Dining',
            'Right':'Library',
            'Behind':'Front Door',
            'Forward':'Hallway',
            'Image':'../images/foyer.png'
        },
        'Front Door': {
            'Story':'You are at the front door.\nIt is locked.\nYou need a key to open it.\nTurn back around.',
            'Behind':'Foyer',
            'Right':'',
            'Left':'',
            'Forward':'',
            'Image':'../images/frontdoor.png'
        },
        'Dining': {
            'Story':'You are in the dining room.\nA large table is in the center,\nwith a tattered table cloth.\nBehind you is the foyer\nand to your right is the kitchen.',
            'Behind':'Foyer',
            'Right':'Kitchen',
            'Left':'',
            'Forward':'',
            'Image':'../images/dining.png'
        },
        'Library': {
            'Story':'',
            'Behind':'',
            'Right':'',
            'Forward':'',
            'Left':'',
            'Image':'../images/library.png'
        },
        'Kitchen': {
            'Story':'You are at the Kitchen.\n\nThe smell of rotten food fills the air.\nTo the left is the dining room.\nYou picked up a teaspoon...\nfor extra security...?\n\n(Out of anything..why that??).\n\nTo your left is the dining room.',
            'Left':'Dining',
            'Right':'',
            'Forward':'',
            'Behind':'',
            'Item':'Teaspoon',
            'Image':'../images/kitchen.png'
        },
        'Hallway': {
            'Story':'You are at the Hallway.\nIt feels endless to walk through.\nTo the left is the bedroom.\nTo the right is the bathroom.\nIn front of you is the living room.\nYou pick up some lint for good luck...',
            'Behind':'Foyer',
            'Right':'Bathroom',
            'Forward':'Living Room',
            'Left':'Bedroom',
            'Item':'Lint',
            'Image':'../images/hallway.png'
        },
        'Living Room': {
            'Story':'You are at the Living Room, a spacious area with a worn sofa that has seen better days.\nA big window casts lights in the room.\nTo the left, the hallway stretches out.',
            'Behind':'',
            'Right':'',
            'Forward':'',
            'Left':'Hallway',
            'Image':'../images/livingroom.png'
        },
        'Bedroom': {
            'Story':'You are at the Bedroom.\nTo the left is the hallway.\nYou hope for a shield...\n\nYou have picked up a pillow...?',
            'Behind':'Hallway',
            'Right':'',
            'Forward':'',
            'Left':'',
            'Item':'Pillow',
            'Image':'../images/bedroom.png'
        },
        'Bathroom': {
            'Story':'You are at the Bathroom.\nIt is dark and damp.\nYou look in the bathtub and find a rusted key.\nBehind you is the hallway.\nYou have picked up a key.',
            'Behind':'Hallway',
            'Right':'',
            'Forward':'',
            'Left':'',
            'Item':'Key',
            'Image':'../images/bathroom.png'}
        }

    command_parser = CommandParser(game_state, game_places)
    status = Status()
    inventory = Inventory()
    monster_fight = MonsterFight(status, inventory)

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
        direction string: Forward, Behind, Left, Right (or 'leave')
    Returns:
        string: the story at the current place
    """
    global game_state
    global monster_fight
    global has_escaped

    direction = direction.lower()


    if direction in ['forward', 'behind', 'left', 'right']:
        game_place = game_places[game_state]
        proposed_state = game_place[direction.capitalize()]
        if proposed_state == '' :
            return 'You can not go that way.\n\n'+game_places[game_state]['Story']
        else :
            game_state = proposed_state
            story = game_places[game_state]['Story']
            item = game_places[game_state].get('Item')
            if item:
                 inventory.pick_up(item)

            if game_state == 'Front Door' and 'Key' in inventory.items:
                has_escaped = True
                return 'Congratulations!\nYou have unlocked the door and escaped the haunted house!\nSay leave to exit the game.'

        if game_state == 'Library':
            return "\nOh no!!\nYou woke up an angry ghost!\nDo you want to fight it or run?"
    
        return story
            
        
    elif direction == 'fight':
        if game_state == 'Library':
            fight_result = monster_fight.start_fight()
            return f"\n{fight_result}\n\n{show_current_place()}"
        else:
            return "You must be seeing ghosts.."
    
    elif direction == 'attack':
        if game_state == 'Library':
            fight_result = monster_fight.continue_fight()
            window['-OUTPUT-'].update(fight_result + '\n\n' + show_current_place())
            inventory_text = inventory.show_inventory()
            window['-INVENTORY-'].update(inventory_text)
            status_text = status.show_status()
            window['-STATUS-'].update(status_text)
        else:
            return "You must be seeing ghosts.."


    else:
         return 'I do not understand that command.\n\n'+game_places[game_state]['Story']
    
has_escaped = False


def make_a_window():
    """
    Creates a game window
    Returns:
        window: the handle to the game window
    """
    sg.theme('LightBlue3')     

    prompt_input = [sg.Text('Enter your command (Forward, Left, Right, Behind)',font='Any 8'),
                    sg.Input(key='-IN-',size=(50,5),font='Any 10', do_not_clear=False)]
    buttons = [sg.Button('Enter',  bind_return_key=True), sg.Button('Exit')]
    command_col = sg.Column([prompt_input,buttons],element_justification='right', pad=(10, 5))
    story_text = sg.Text(show_current_place(), size=(50,10), font='Any 8', key='-OUTPUT-',
                         text_color='black', pad=(10, 10), justification='left')
    story_frame = sg.Frame('Story', [[story_text]], title_color='black', relief=sg.RELIEF_SUNKEN, element_justification='center', pad=(10, 10))

    layout = [[sg.Image(r'../images/house.png',size=(180,180),key="-IMG-"), 
               story_frame], 
             [sg.Text('Inventory:'), sg.Text('', size=(30, 1), key='-INVENTORY-')],
             [sg.Text('Health:'), sg.Text('', size=(30, 1), key='-STATUS-')],
             [sg.Text('', size=(-15, 10)), command_col]]
    
    return  sg.Window('The Haunted House', layout, size=(420,340), resizable=True)

if __name__ == "__main__":
    # A persisent window - stays until "Exit" is pressed
    window = make_a_window()

    inventory_text = inventory.show_inventory()
    status_text = status.show_status()


    while True:
        event, values = window.read()

        inventory_text = inventory.show_inventory()
        status_text = status.show_status()

        window['-INVENTORY-'].update(inventory_text)
        window['-STATUS-'].update({status.show_status()})
        window['-OUTPUT-'].update(show_current_place())
        window['-IMG-'].update(game_places[game_state]['Image'],size=(180,180))

        if event ==  'Enter': 
                direction = values['-IN-'].strip().lower()

                if game_state == 'House' and direction in ['yes', 'no']:
                    if direction == 'yes':
                        game_state = 'Foyer'
                        window['-OUTPUT-'].update(game_places['Foyer']['Story'])
                        window['-IMG-'].update(game_places['Foyer']['Image'], size=(180, 180))
                    elif direction == 'no':
                        window['-OUTPUT-'].update('You still end up here\n..Something pushed you!\n\n' + game_places['Foyer']['Story'])
                        game_state = 'Foyer'
                        window['-IMG-'].update(game_places['Foyer']['Image'], size=(180, 180))
                    continue  # Skip the rest of the loop since we handled the input


                if direction in ['forward', 'behind', 'left', 'right']:
                    current_story = game_play(direction)
                    window['-OUTPUT-'].update(current_story)
                    window['-IMG-'].update(game_places[game_state]['Image'], size=(180,180))
                    inventory_text = inventory.show_inventory()
                    window['-INVENTORY-'].update(inventory_text)
                    status_text = status.show_status()
                    window['-STATUS-'].update(status_text)

                    if has_escaped and direction == 'leave':
                        break

                    if "Congratulations" in current_story:
                        continue


                elif direction == 'run' and game_state == 'Library':
                    game_state = 'Foyer'
                    window['-OUTPUT-'].update("You run back to the foyer..\nClosing the door behind you." + game_places['Foyer']['Story'])
                    window['-IMG-'].update(game_places['Foyer']['Image'], size=(180, 180))

                elif direction == 'fight' and game_state == 'Library':
                    fight_result = monster_fight.start_fight()
                    window['-OUTPUT-'].update(fight_result + '\n\n' + show_current_place())
                    inventory_text = inventory.show_inventory()
                    window['-INVENTORY-'].update(inventory_text)
                    status_text = status.show_status()
                    window['-STATUS-'].update(status_text)

                else:
                    window['-OUTPUT-'].update('I do not understand that command.\n'+ show_current_place())
                    
        elif event == 'Exit' or event is None or direction == 'leave' or event == sg.WIN_CLOSED:
            break
        
    window.close()

                     


