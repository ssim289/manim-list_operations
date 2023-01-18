from manim import *
from ..config import CONFIG


class TreeNode(Circle):
    def __init__(self, value, l=None, r=None, **kwargs):
        self.default_attributes = kwargs
        super().__init__(radius=kwargs["side_length"]/4, color=kwargs["color"],
                         fill_color=kwargs["fill_color"], fill_opacity=kwargs["fill_opacity"])
        self.data = value
        self.text_mobject = Text(
            str(value), color=kwargs["font_color"], font_size=kwargs["font_size"]/2, fill_opacity=kwargs["font_opacity"]).move_to(self.get_center())
        self.add(
            self.text_mobject
        )
        self.left = l
        self.right = r

    def set_left(self, n):
        self.left = n

    def set_right(self, n):
        self.right = n

    def shade(self, color):
        return AnimationGroup(self.animate.set_fill(color, opacity=0.5), self.text_mobject.animate.set_fill(self.default_attributes["font_color"], opacity=self.default_attributes["font_opacity"]))

    def unshade(self):
        return AnimationGroup(self.animate.set_fill(self.default_attributes["fill_color"], opacity=self.default_attributes["fill_opacity"]), self.text_mobject.animate.set_fill(self.default_attributes["font_color"], opacity=self.default_attributes["font_opacity"]))

    def __lt__(self, other):
        return self.data < other.data

    def __lt__(self, other):
        return self.data > other.data

    def __eq__(self, other):
        return self.data == other.data

    def __le__(self, other):
        return self.data <= other.data

    def __ge__(self, other):
        return self.data >= other.data

    def __ne__(self, other):
        return self.data != other.data
