from Gameplay_depiction_classes.Direction import Direction
from Game_objects import Food
from Board import Board_behavior
from coordinates import Coordinate

class Snake:

    def __init__(self):
        self.length = 1
        self.direction = Direction.UP
        self.newDirection = Direction.NONE
        self.coordinates = []
        self.body_parts = []

