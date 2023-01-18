
from .list_cell import ListElementCell
from manim import *
from ..config import CONFIG
import random


class ListGraphic(VGroup):
    def __init__(self, list, **kwargs):
        kwargs.setdefault("side_length", CONFIG["cell_size"])
        kwargs.setdefault("color", CONFIG["border_color"])
        kwargs.setdefault("fill_color", CONFIG["fill_color"])
        kwargs.setdefault("fill_opacity", CONFIG["fill_opacity"])
        kwargs.setdefault("font_size", CONFIG["font_size"])
        kwargs.setdefault("font_color", CONFIG["font_color"])
        kwargs.setdefault("font_opacity", CONFIG["font_opacity"])
        self.default_attributes = kwargs
        elements = (ListElementCell(x, **kwargs) for x in list)
        super().__init__(*elements)
        self.arrange_submobjects(buff=0)

    def swap_elements(self, n1, n2):
        n1m = self[n1]
        n2m = self[n2]
        animation = AnimationGroup(
            *[n1m.move(target=n2m), n2m.move(target=n1m)])
        self[n1], self[n2] = self[n2], self[n1]
        return animation

    def raise_elements(self, *args):
        animations = []
        for x in args:
            animations.append(self[x].animate.shift(UP))
        return AnimationGroup(*animations)

    def lower_elements(self, *args):
        animations = []
        for x in args:
            animations.append(self[x].animate.shift(DOWN))
        return AnimationGroup(*animations)

    def shade(self, n, color, op=0.5):
        return self[n].shade(color, op)

    def unshade(self, n):
        return self[n].unshade()

    def pop(self, n=-1):
        animations = []
        if n == -1:
            n = len(self)-1
        last = self[n]
        self.remove(last)
        animations.append(self.animate.arrange_submobjects(buff=0))
        return AnimationGroup(FadeOut(last), *animations)

    def insert(self, n, i):
        animations = []
        element = ListElementCell(n, **self.default_attributes)
        self.add(element)
        for x in range(len(self)-1, i, -1):
            self[x] = self[x-1]
        self[i] = element
        element.shift(self[i-1].get_center() -
                      element.get_center()+RIGHT)

        animations.append(self.animate.arrange_submobjects(buff=0))
        return AnimationGroup(FadeIn(element), *animations)

    def append(self, n):
        return self.insert(n, len(self))
