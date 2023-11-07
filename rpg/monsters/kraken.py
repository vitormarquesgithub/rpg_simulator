class Kraken:
    def __init__(self, life, atk, agi):
        self.life = life 
        self.atk = atk 
        self.agi = agi

    def show_status(self):
        print(f'Kraken - LIFE: {self.life} ATK: {self.atk} AGI: {self.agi}')

kraken = Kraken(vida=1200, atk=15, agi=12)