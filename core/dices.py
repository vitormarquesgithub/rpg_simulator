class Dice:
    def __init__(self, id, faces, name):
        self.id = id
        self.faces = faces
        self.name = name

d3 = Dice(1, 3, 'D3')

dices_list = [d3]