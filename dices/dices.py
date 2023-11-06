class Dice:
    def __init__(self, id, faces, name):
        self.id = id
        self.faces = faces
        self.name = name

d4 = Dice(1, 4, 'D4') 
d6 = Dice(2, 6, 'D6') 
d8 = Dice(3, 8, 'D8') 
d10 = Dice(4, 10, 'D10') 
d12 = Dice(5, 12, 'D12') 
d20 = Dice(6, 20, 'D20') 

dices_list = [d4, d6, d8, d10, d12, d20]