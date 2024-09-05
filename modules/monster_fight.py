import random
from inventory import Inventory
from status import Status

class MonsterFight:   
    """ a class to simulate a fight between the player and a monster
    
    Args:
        game_state (dict): the current state of the game
        monster (str): the monster that the player is fighting
        player_health (int): the health of the player
        monster_health (int): the health of the monster
        status (object): the status object of the player
        inventory (object): the inventory object of the player
        player_attack (int): the attack value of the player
        monster_attack (int): the attack value of the monster
    """ 

    def __init__(self, status, inventory):
        """ initialize the MonsterFight class with the player and monster health, status, inventory, and attack values
        
        Args:
            game_state (dict): the current state of the game
            status (object): the status object of the player
            inventory (object): the inventory object of the player
        
        """

        # initializing MonsterFight with objects like health/status and inventory
        self.monster = 'monster'
        self.player_health = 50
        self.monster_health = 50
        self.status = status
        self.inventory = inventory
        self.monster_attack = 15
        self.player_attack = 10
        

    def has_item(self, item):
        """ check if player has an item in their inventory to fight with
        Args:
            game_state (dict): the current state of the game
            item (str): the item to check in the player's inventory
            
        """
        # checks if player has a specific item in their inventory for fighting
        return item in self.inventory.items
    
    def get_random_item(self):
        """ equips a random item from the players inventory for fighting 
        
        Returns:
            str: the random item from the player's inventory

            None: if the player has no items in their inventory
            """
        # returns a random item from the inventory to use for fighting - 'None' for if theres nothing in the inventory (theres logic for that when fighting later)
        items = [item for item in ['Teaspoon', 'Pillow', 'Lint'] if item in self.inventory.items]
        return random.choice(items) if items else None

    def calculate_player_attack(self):
        """ calculate and return an attack value (at random) for the player
         
          Returns:
            int: the attack value of the player
        """
        # returns a 'random' int
        return random.randint(1, self.player_attack)
    
    def calculate_monster_attack(self):
        """ calculate and returns an attack value (at random) for the monster
        
            Returns:
                int: the attack value of the monster
        """
        # returns a 'random' int
        return random.randint(1, self.monster_attack)
    

    def player_defend(self):
        return random.randint(1, self.player_attack)
    
    def monster_defend(self):
        return random.randint(1, 10)
    
    def update_health(self, damage, target):
        """ updates the health of the player or monster (based on damage taken)

        Args: 
            game_state (dict): the current state of the game
            damage (int): the damage taken by the player or monster
            target (str): the target of the attack (player or monster)
            
            Returns:
                str: the updated status of the player or monster
        """
        # updates the health of the player or monster (based on the damage taken)
        if target == 'player':
            self.player_health -= damage
            if self.player_health <= 0:
                self.player_health = 0
            self.status.update_health(self.player_health)
            return "You have been defeated.."


        elif target == 'monster':
            self.monster_health -= damage
            if self.monster_health < 0:
                self.monster_health = 0

        




    def fight_round(self, item):
        """ simulates a round of fighting between the player and monster
        
        Args:
            game_state (dict): the current state of the game
            item (str): the item used by the player to fight
            
            Returns:
                tuple: a tuple containing the damage taken by the player and monster, and an optional message
        """
        if item not in ['Teaspoon', 'Pillow', 'Lint']:         # based on a specific item in their inventory

            self.player_health = 0
            self.status.update_health(self.player_health)
            return 0,0, "That was kind of a bad choice...\nYou had nothing to fight with...\nyou die..\n\nPress the 'Exit' button."
        
        # adjusts the players attack based on whatever the item is
        if item == 'Teaspoon':
            self.player_attack = 20
        elif item == 'Pillow':
            self.player_attack = 5         
        elif item == 'Lint':
            self.player_attack = 2

        # use default attacks if the item isnt recognised
        player_attack = self.calculate_player_attack()
        monster_attack = self.calculate_monster_attack()
        player_defend = self.player_defend()
        monster_defend = self.monster_defend()
        
        # calculating the damage of both the player and monster
        player_damage= max(monster_attack - player_defend, 0)
        monster_damage = max(player_attack - monster_defend, 0)

        return player_damage, monster_damage, ""
        

    def start_fight(self):
        """ starts the fight with the monster
        
        Args:
            game_state (dict): the current state of the game

        Returns:
            str: the result of the fight
        """

        # if no items in inventory - instant death
        if not self.inventory.items:
            self.status.update_health(0)
            return "That was kind of a bad choice...\nYou had nothing to fight with...\nyou die.."
        
        # if player is already dead - return message
        if self.player_health <= 0:
            return "You are already dead!"
        
        if self.monster_health <= 0:
            return "The monster is already defeated!"
        
        # get random item from inventory
        item = self.get_random_item()
        if item:
            player_damage, monster_damage, message = self.fight_round(item)
            self.update_health(player_damage, 'player')
            self.update_health(monster_damage, 'monster')

            result = f"You used the {item}.\nMonsters health is now {self.monster_health}\n\n"
            result += f"The monster attacked you!\nThat hurt."
            result += f"\nSay 'Fight' to fight again!"  # just an indicator so the user knows what to say next

            if self.monster_health <= 0:
                result += "\nYou defeated the monster!"
                
            
            if self.player_health <= 0:
                result += "\nYou were defeated by the monster..."
                
        else:
            result = "No items to fight with."
            
        if message:
            result += f"\n{message}"

        if self.monster_health > 0:
            monster_damage = self.calculate_monster_attack()
            self.update_health(monster_damage, 'player')

        return result or "The fight ended with no clear result"
        
    


    def continue_fight(self):
        """ continues the fight between the player and monster until either is defeated
        
        Returns:
            str: the result of the fight
        """
        if not self.inventory.items:
            self.status.update_health(0)
            return "That was kind of a bad choice...\nYou had nothing to fight with...\nyou die.."
        
        if self.player_health <= 0:
            return "You are already dead!"
        
        result = ""
        while self.monster_health > 0 and self.player_health > 0:
            item = self.get_random_item()
            if item:
                player_damage, monster_damage, message = self.fight_round(item)
                self.update_health(player_damage, 'player')
                self.update_health(monster_damage,'monster')

                result += f"You used the {item}. Monsters health is now {self.monster_health}"
                result += f"\n\nThe monster attacked you!"
                result += f"\nSay 'Fight' to fight again!"

            if message:
                result += f"{message}"
        monster_damage = self.calculate_monster_attack()
        self.update_health(monster_damage, 'player')
        result += f"\nThe monster dealt {monster_damage} damage to you."

        if self.monster_health <= 0:
            result += "\nYou defeated the monster!"
        elif self.player_health <= 0:
            result += "\nYou were defeated by the monster..."

            return result        

            

    
def monster_attacks(self):
    """ handling the monsters attack on player (through random integers)
    
    Returns:
        str: the result of the monster's attack on the player
    """
    damage = random.randint(15,30)
    player_status = self.update_health(damage, 'player')
    if player_status:
        return player_status

if __name__ == "__main__":
    # testing the class 'MonsterFight'
    status = Status()
    inventory = Inventory()
    monster_fight = MonsterFight(status, inventory)
    print(monster_fight.start_fight())
    print(f"Player Health: {status.show_status()}")



