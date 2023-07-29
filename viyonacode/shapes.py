class Rectangle:
    def __init__(self):
        self.x = 400
        self.y = 400
        self.width = 200
        self.height = 100

    def move(self, direction):
        if direction == 'UP':
            self.y -= 10
        if direction == 'DOWN':
            self.y += 10
        if direction == 'RIGHT':
            self.x += 10
        if direction == 'LEFT':
            self.x -= 10

    def covers(self, x, y):
        if self.x < x < (self.x + self.width) and self.y < y < (self.y + self.height):
            return True
        else:
            return False
class Triangle:
    def __init__(self):
        self.x1 = 400
        self.y1 = 400
        self.x2 = 300
        self.y2 = 500
        self.x3 = 500
        self.y3 = 500


    def move(self, direction):
        if direction == 'UP':
            self.y1 -= 10
            self.y2 -= 10
            self.y3 -= 10
        if direction == 'DOWN':
            self.y1 += 10
            self.y2 += 10
            self.y3 += 10
        if direction == 'RIGHT':
            self.x1 += 10
            self.x2 += 10
            self.x3 += 10
        if direction == 'LEFT':
            self.x1 -= 10
            self.x2 -= 10
            self.x3 -= 10

    def covers(self, x, y):
        return False

class Circle:
    def __init__(self):
        self.x = 400
        self.y = 400
        self.r = 200


    def move(self, direction):
        if direction == 'UP':
            self.y -= 10
        if direction == 'DOWN':
            self.y += 10
        if direction == 'RIGHT':
            self.x += 10
        if direction == 'LEFT':
            self.x -= 10

    def covers(self, x, y):
        if (self.x - x)**2 + (self.y - y)**2 < self.r**2:
            return True
        else:
            return False