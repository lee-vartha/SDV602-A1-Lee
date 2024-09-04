class Status:
    def __init__(self):
        self.player_health = 50

    
    def update_health(self, new_health):
        self.player_health = new_health


    def show_status(self):
        return f"{self.player_health}"

if __name__ == "__main__":
    status = Status()
    status.update_health(50)
    print(status.show_status())

