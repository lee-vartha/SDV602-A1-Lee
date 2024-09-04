import random
from inventory import Inventory
from status import Status

class MonsterFight:    
    def __init__(self, status, inventory):
        self.monster = 'monster'
        self.monster_health = 50
        self.player_health = 50
        self.status = status
        self.inventory = inventory
        self.monster_attack = 15
        self.player_attack = 10
        
    def has_item(self, item):
        return item in self.inventory.items
    
    def get_random_item(self):
        items = [item for item in ['Teaspoon', 'Pillow', 'Lint'] if item in self.inventory.items]
        return random.choice(items) if items else None

    def calculate_player_attack(self):
        return random.randint(1, self.player_attack)
    
    def calculate_monster_attack(self):
        return random.randint(1, self.monster_attack)
    
    def player_defend(self):
        return random.randint(1, self.player_attack)
    
    def monster_defend(self):
        return random.randint(1, self.monster_attack)


    def update_health(self, damage, target):
        if target == 'player':
            self.player_health -= damage
            self.status.update_health(self.player_health)
            if self.player_health <= 0:
                self.player_health = 0
                return "You have been defeated!"
        elif target == 'monster':
            self.monster_health -= damage
            if self.monster_health <= 0:
                self.monster_health = 0
                return "You have defeated the monster!"
        return None    


    def fight_round(self, item):
        if item not in ['Teaspoon', 'Pillow', 'Lint']:
            self.player_health = 0
            return "That was kind of a bad choice...\nYou had nothing to fight with...\nyou die.."
        
        if item == 'Teaspoon':
            self.player_attack = 20
            # return f"To your surprise..\nthe spoon helped you very well!"
        elif item == 'Pillow':
            self.player_attack = 5            
            # return f"Your pillow somehow helped you!\nMust\'ve scared it away."
        elif item == 'Lint':
            self.player_attack = 1
            # return f"Your lint didn't help you much...\nSo much for luck, huh."


        player_attack = self.calculate_player_attack()
        monster_attack = self.calculate_monster_attack()
        player_defend = self.player_defend()
        monster_defend = self.monster_defend()

        player_damage= max(monster_attack - player_defend, 0)
        monster_damage = max(player_attack - monster_defend, 0)

        return player_damage, monster_damage        
        
    def start_fight(self):
        if not self.inventory.items:
            self.status.update_health(0)
            return "That was kind of a bad choice...\nYou had nothing to fight with...\nyou die.."
        
        if self.player_health <= 0:
            return "You are already dead!"
        
        item = self.get_random_item()
        if item:
            player_damage, monster_damage = self.fight_round(item)
            player_status = self.update_health(player_damage, 'player')
            monster_status = self.update_health(monster_damage, 'monster')
            return f"You used the {item}.\nMonsters health is now {self.monster_health}\n\nThe monster attacked you!\n Your health is now {self.player_health}"
        if player_status:
            result += f"\n{player_status}"
        if monster_status:
            result += f"\n{monster_status}"
        return result
        
    def continue_fight(self):
        if not self.inventory.items:
            self.status.update_health(0)
            return "That was kind of a bad choice...\nYou had nothing to fight with...\nyou die.."
        
        if self.player_health <= 0:
            return "You are already dead!"
        
        item = self.get_random_item()
        if item:
            player_damage, monster_damage = self.fight_round(item)
            player_status = self.update_health(player_damage, 'player')
            monster_status = self.update_health(monster_damage,'monster')

            result = f"You used the {item}. Monsters health is now {self.monster_health}\n\nThe monster attacked you! Your health is now {self.player_health}"

            if player_status:
                result += f"{player_status}"
            if monster_status:
                result += f"{monster_status}"
        
        if self.monster_health > 0:
            monster_attack_result = self.monster_attacks()
            result += f"\n{monster_attack_result}"

            return result
            

    
    def monster_attacks(self):
        damage = random.randint(15,30)
        player_status = self.update_health(damage, 'player')
        if player_status:
            return player_status

if __name__ == "__main__":
    status = Status()
    inventory = Inventory()
    monster_fight = MonsterFight(status)
    print(monster_fight.start_fight())
    print(f"Player Health: {status.show_status()}")



