# importing the necessary modules and classes
from monster_fight import MonsterFight
from inventory import Inventory 
from status import Status

class CommandParser:
    
    def __init__(self, game_state, game_places):
        """initialize the CommandParser class with the game state, game places, status, inventory, and monster fight.
        
        Args:
            game_state (dict): the current state of the game
            game_places (dict): the places in the game
            status (object): the status object of the player
            inventory (object): the inventory object of the player
            monster_fight (object): the monster fight object of the player
        """
        self.game_places = game_places
        self.game_state = game_state
        self.status = Status()
        self.inventory = Inventory()
        self.monster_fight = MonsterFight(self.status, self.inventory)

    def parse_command(self, command):
        """parse the user condition and direct the game state accordingly
        
        Args:  
            command (str): the command entered by the user
            
        Returns:
            dict: the updated game state
        """
        command = command.lower().strip()
        if command in ['forward', 'behind', 'left', 'right']: # if this is a movement command
            return self.move_player(command.lower())
        elif command == 'inventory': # if this is an inventory command
            return self.show_inventory() 
        elif command == 'status': # if this is a status command
            return self.show_status() 
        elif command == 'fight': # if this is a fight command
            return self.fight_monster()
        elif command == 'attack': # if this is an attack command
            return self.attack_monster()
        elif command == 'leave': # if this is a leave command
            self.game_state['game_over'] = True
            return self.game_state
        elif command == 'quit': # if this is a quit command
            self.game_state['game_over'] = True
            return self.game_state
        elif command == 'exit': # if this is an exit command
            self.game_state['game_over'] = True
            return self.game_state
        else:
            return "I don't know what you mean" # otherwise, return error
    
    def move_player(self, direction):
        """ move the player in the game
        
        Args:
            direction (str): the direction to move the player
            
        Returns:
            str: the story of the current place
        """
        current_place = self.game_places[self.game_state] # determining the current place
        proposed_state = current_place.get(direction, '') # determining the players proposed state
        if not proposed_state: # if the state doesnt align as expected
            return "You cannot go that way. \n + current_place['Story']"
        self.game_state = proposed_state
        return self.game_places[self.game_state]['Story']
    
    def show_inventory(self):
        """ showing the players inventory 
        
        Returns:
            str: the items in the player's inventory
        """
        return self.inventory.show_inventory()
    
    def show_status(self):
        """ showing the players status
        
        Returns:
            str: the status of the player
        """
        return self.status.show_status()
    
    def fight_monster(self):
        """ starting the fight with the monster
        
        Returns:
            str: the result of the fight
        """
        return self.monster_fight.start_fight()
    
    def attack_monster(self):
        """ attacking the monster

        Returns:
            str: the result of the attack
        """
        return self.monster_fight.continue_fight()

if __name__ == "__main__":
    # testing the class of CommandParser
    game_state = 'House'
        
    parser = CommandParser(game_state)
    command = input("Enter a command: ")
    print(parser.parse_command(command))