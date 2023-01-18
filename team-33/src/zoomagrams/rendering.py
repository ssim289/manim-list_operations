from manim import *
import enum
from .config import CONFIG


class TextPosition(enum.Enum):
    TopLeft = "{\\an7}"
    TopCenter = "{\\an8}"
    TopRight = "{\\an9}"
    MiddleLeft = "{\\an4}"
    MiddleCenter = "{\\an5}"
    MiddleRight = "{\\an6}"
    BottomLeft = "{\\an1}"
    BottomCenter = "{\\an2}"
    BottomRight = "{\\an3}"


def format_srt_content(
    content: str,
    font_size=64,
    text_color="",
    text_position=TextPosition.BottomCenter,
    is_bold=False,
    is_italic=False,
):
    result = f"{content}"

    if is_italic:
        result = f"<i>{result}</i>"

    if is_bold:
        result = f"<b>{result}</b>"

    return (
        text_position.value
        + f"<font color={text_color} size={font_size}>{result}</font>"
    )


class ZoomagramsScene(Scene):
    def setup(self):
        self.camera.background_color = CONFIG["background_color"]
        self.camera.background_opacity = CONFIG["background_opacity"]

        def add_subtitle(
            self,
            content: str,
            duration: float = 1,
            offset: float = 0,
            font_size=64,
            text_color="",
            text_position=TextPosition.BottomCenter,
            is_bold=False,
            is_italic=False,
        ):
            srt_content = format_srt_content(
                content,
                font_size=font_size,
                text_color=text_color,
                text_position=text_position,
                is_italic=is_italic,
                is_bold=is_bold,
            )

            self.add_subcaption(srt_content, duration=duration, offset=offset)
