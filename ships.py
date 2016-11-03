class Ship:

    location = []
    horizontal = False


    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.hit_points = size

    def sunk(self):
        if self.hit_points <= 0:
            return True
    def damage(self):
        self.hit_points -= 1
