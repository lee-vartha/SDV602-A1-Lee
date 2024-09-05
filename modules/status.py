class Status:
    def __init__(self):
        """ initialize the Status class with the player's health.
        
        Args:
            player_health (int): the health of the player.
        """
        self.player_health = 50

    
    def update_health(self, new_health):
        """ updates the players health based on the fight
        
        Args:
            new_health (int): the new (updated) health of the player.
        """
        self.player_health = new_health


    def show_status(self):
        """ shows the players health 
        
        Returns:
            str: the health of the player.
        """
        return f"{self.player_health}"

if __name__ == "__main__":
    # testing the class of Status 
    status = Status()
    status.update_health(50)
    print(status.show_status())

