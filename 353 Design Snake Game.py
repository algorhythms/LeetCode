"""
Design a Snake game that is played on a device with screen size = width x height.
"""
from collections import deque

__author__ = 'Daniel'


class SnakeGame(object):
    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.w = width
        self.h = height
        self.food = deque(food)
        self.body = deque([(0, 0)])
        self.dirs = {
            'U': (-1, 0),
            'L': (0, -1),
            'R': (0, 1),
            'D': (1, 0),
        }
        self.eat = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        x, y = self.body[0]
        dx, dy = self.dirs[direction]
        x += dx
        y += dy
        fx, fy = self.food[0] if self.food else (-1, -1)
        if x == fx and y == fy:
            self.food.popleft()
            self.eat += 1
        else:
            self.body.pop()
            if (x, y) in self.body or not (0 <= x < self.h and 0 <= y < self.w):
                # possible to use set to accelerate check
                return -1

        self.body.appendleft((x, y))
        return self.eat


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

if __name__ == "__main__":
    game = SnakeGame(3, 2, [[1, 2], [0, 1]])
    for char, expect in zip('RDRULU', [0, 0, 1, 1, 2, -1]):
        assert game.move(char) == expect
