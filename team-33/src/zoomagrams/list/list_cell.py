from manim import *
from ..config import CONFIG


class ListElementCell(Square):
    def __init__(self, value, **kwargs):
        self.default_attributes = kwargs
        super().__init__(side_length=kwargs["side_length"], color=kwargs["color"],
                         fill_color=kwargs["fill_color"], fill_opacity=kwargs["fill_opacity"])
        self.data = value
        self.text_mobject = Text(
            str(value), color=kwargs["font_color"], font_size=kwargs["font_size"], fill_opacity=kwargs["font_opacity"]).move_to(self.get_center())
        self.add(
            self.text_mobject
        )

    def move(self, **kwargs):
        if "target" in kwargs:
            target = kwargs["target"]
            return self.animate.shift(target.get_center() - self.get_center())
        elif "mag" in kwargs:
            mag = kwargs["mag"]
            return self.animate.shift(mag)

    def shade(self, color, op=0.5):
        return AnimationGroup(self.animate.set_fill(color, opacity=op), self.text_mobject.animate.set_fill(self.default_attributes["font_color"], opacity=self.default_attributes["font_opacity"]))

    def unshade(self):
        return AnimationGroup(self.animate.set_fill(self.default_attributes["fill_color"], opacity=self.default_attributes["fill_opacity"]), self.text_mobject.animate.set_fill(self.default_attributes["font_color"], opacity=self.default_attributes["font_opacity"]))

    def __lt__(self, other):
        return self.data < other.data
