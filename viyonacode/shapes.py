class Rectangle():
    def __init__(self):
        self.e1 = (400, 400)
        self.width = (200)
        self.height = (100)
    def move(self, direction):
        if direction == 'UP':
            self.e1[1] = self.e1[1] + 10
        if direction == 'DOWN':
            self.e1[1] = self.e1[1] - 10
        if direction == 'RIGHT':
            self.e1[0] = self.e1[0] + 10
        if direction == 'LEFT':
            self.e1[0] = self.e1[0] - 10