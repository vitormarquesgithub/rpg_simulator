class Golem:
    def __init__(self, life, atk, agi):
        self.life = life 
        self.atk = atk 
        self.agi = agi

    def show_status(self):
        print(f'Golem - LIFE: {self.life} ATK: {self.atk} AGI: {self.agi}')

dragon = Golem(vida=1500, atk=10, agi=5)