from manim import *
import math
import random

# Create each cell for the list


def ListCellGraphic(num, scale=1):
    fsize = scale*48
    ssize = scale*1
    square = Square(side_length=scale*1)
    text = Text(str(num), font_size=scale*48)
    return Group(square, text)


# Generate the list graphic
def ListGraphic(input_list, scale=1):
    input_len = len(input_list)
    MobjectGroup = Group()
    for x in range(input_len):
        # Create new cell for each element
        cell = ListCellGraphic(input_list[x], scale)

        # We need to reposition them, otherwise they all render in the same location
        if (input_len % 2 == 0):
            if x < input_len / 2:
                cell.shift(RIGHT * scale / 2)
                cell.shift(LEFT * scale * ((input_len / 2) - x))
            else:
                cell.shift(RIGHT * scale / 2)
                cell.shift(RIGHT * scale * (x - (input_len / 2)))
        else:
            mid = math.floor(input_len/2)
            if x < mid:
                cell.shift(LEFT * scale * (mid - x))
            if x > mid:
                cell.shift(RIGHT * scale * (x - mid))
        MobjectGroup.add(cell)
    return MobjectGroup


class CreateTable(Scene):
    def construct(self):
        # create random list of elements to sort
        randlist = []
        len = random.randint(7, 7)
        for x in range(len):
            randlist.append(random.randint(0, 20))
        square = ListGraphic(randlist, 1)
        self.add(square)


# To run, python -m in-python-render.py in venv terminal

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = CreateTable()
    scene.render()
