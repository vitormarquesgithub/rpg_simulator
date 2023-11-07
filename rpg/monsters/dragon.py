class Dragon:
    def __init__(self, life, atk, agi):
        self.life = life 
        self.atk = atk 
        self.agi = agi

    def show_status(self):
        print(f'Dragon - LIFE: {self.life} ATK: {self.atk} AGI: {self.agi}')

dragon = Dragon(vida=1000, atk=20, agi=10)

