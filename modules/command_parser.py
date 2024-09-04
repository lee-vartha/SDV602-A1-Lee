from monster_fight import MonsterFight
from inventory import Inventory 
from status import Status

class CommandParser:
    def __init__(self, game_state, game_places):
        self.game_places = game_places
        self.game_state = game_state
        self.status = Status()
        self.inventory = Inventory()
        self.monster_fight = MonsterFight(self.status, self.inventory)

    def parse_command(self, command):
        """Parse the user condition and direct the game state accordingly.
        
        Args:  
            command (str): The command entered by the user.
            
        Returns:
            dict: The updated game state."""
        command = command.lower().strip()
        if command in ['forward', 'behind', 'left', 'right']:
            return self.move_player(command.lower())
        elif command == 'inventory':
            return self.show_inventory()
        elif command == 'status':
            return self.show_status()
        elif command == 'fight':
            return self.fight_monster()
        elif command == 'attack':
            return self.attack_monster()
        elif command == 'leave':
            self.game_state['game_over'] = True
            return self.game_state
        elif command == 'quit':
            self.game_state['game_over'] = True
            return self.game_state
        elif command == 'exit':
            self.game_state['game_over'] = True
            return self.game_state
        else:
            return "I don't know what you mean"
    
    def move_player(self, direction):
        current_place = self.game_places[self.game_state]
        proposed_state = current_place.get(direction, '')
        if not proposed_state:
            return "You cannot go that way. \n + current_place['Story']"
        self.game_state = proposed_state
        return self.game_places[self.game_state]['Story']
    
    def show_inventory(self):
        return self.inventory.show_inventory()
    
    def show_status(self):
        return self.status.show_status()
    
    def fight_monster(self):
        return self.monster_fight.start_fight()
    
    def attack_monster(self):
        attack_result = self.monster_fight.attack()
        status_update = self.status.update_health()
        continue_fight_result = self.monster_fight.continue_fight()
        return f"{attack_result}\n{status_update}\n{continue_fight_result}"    

if __name__ == "__main__":
    game_state = 'House'
        
    parser = CommandParser(game_state)
    command = input("Enter a command: ")
    print(parser.parse_command(command))