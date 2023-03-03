class Snake:
    def __init__(self, screen_width, screen_height):
        self.segments = [(0, 0), (-20, 0), (-40, 0)]
        self.direction = 0
        self.MOVE_DISTANCE = 14
        self.screen_width = screen_width
        self.screen_height = screen_height

    def create_extra_segment(self):
        x, y = self.segments[-1]
        self.segments.append((x, y))

    def move(self):
        x, y = self.segments[0]

        if self.direction == 0:
            x += self.MOVE_DISTANCE
        elif self.direction == 90:
            y += self.MOVE_DISTANCE
        elif self.direction == 180:
            x -= self.MOVE_DISTANCE
        elif self.direction == 270:
            y -= self.MOVE_DISTANCE

        # Check if the x position is beyond the screen width
        if x >= self.screen_width:
            x = 0
        elif x < 0:
            x = self.screen_width

        # Check if the y position is beyond the screen height
        if y >= self.screen_height:
            y = 0
        elif y < 0:
            y = self.screen_height

        self.segments.insert(0, (x, y))
        self.segments.pop()

    def up(self):
        if self.direction != 90:
            self.direction = 270

    def down(self):
        if self.direction != 270:
            self.direction = 90

    def left(self):
        if self.direction != 0:
            self.direction = 180

    def right(self):
        if self.direction != 180:
            self.direction = 0





