
class Inventory:
    def __init__(self):
        self.items = []

    def pick_up(self, item):
        if item not in self.items:
            self.items.append(item)
            return f"Picked up {item}."
        return f"You already have {item}."
    

    def show_inventory(self):
        inventory_text = f"{', '.join(self.items)}" if self.items else "Inventory is empty."        
        print(f"{inventory_text}")
        return inventory_text

    def add_item(game_state, item):
        """Add an item to the player's inventory.
        
        Args:
            game_state (dict): The current state of the game.
            item (str): The item to add to the inventory.
            
            Returns:
                dict: The updated game state.
        """

        game_state['inventory'].add(item)
        return game_state

if __name__ == "__main__":
    inventory = Inventory()
    print(inventory.pick_up())
    print(inventory.show_inventory())