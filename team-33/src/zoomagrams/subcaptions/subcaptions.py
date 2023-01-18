from manim import *
from ..config import CONFIG


class Subcaption(Text):
    def __init__(self, text, downshift=3, **kwargs):
        kwargs.setdefault("font_size", CONFIG["caption_size"])
        kwargs.setdefault("color", CONFIG["caption_color"])
        super().__init__(text=text, **kwargs)
        self.shift(DOWN*downshift)
