
class Inventory:
    def __init__(self):
        """ initialize the Inventory class with an empty list of items
        
        Args:
            game_state (dict): the current state of the game
            list (items): the list of items in the player's inventory
        """
        self.items = []

    def pick_up(self, item):
        """ player picks up an item to put into their inventory
        
        Args:
            game_state (dict): the current state of the game
            item (str): the item to pick up
            
        Returns:
            str: the item picked up.
        """
        if item not in self.items:
            self.items.append(item)
            return f"Picked up {item}."
        return f"You already have {item}."
    


    def show_inventory(self):
        """ shows and updates the inventory 
        
        Args:
            game_state (dict): the current state of the game

        Returns:
            str: the items in the player's inventory
        """
        inventory_text = f"{', '.join(self.items)}" if self.items else "Inventory is empty."        
        print(f"{inventory_text}")
        return inventory_text


    def add_item(game_state, item):
        """add an item to the player's inventory
        
        Args:
            game_state (dict): the current state of the game
            item (str): the item to add to the inventory
            
            Returns:
                dict: the updated game state
        """

        game_state['inventory'].add(item)
        return game_state

if __name__ == "__main__":
    inventory = Inventory()
    print(inventory.pick_up())
    print(inventory.show_inventory())