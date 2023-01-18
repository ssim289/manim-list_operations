# Zoomagrams

## Description

A framework to algorithmically generate walkthough animations for teaching data structure operations and algorithms.
Developed using Python and the [Manim](https://www.manim.community/) animation library. See `/requirements.txt` for a full list of modules used and versions.

Documentation for Zoomagrams is found [here](https://github.com/uoa-compsci399-s2-2022/team-33#documentation).
All our work is built as an extension of Manim and as such, all [Manim documentation](https://docs.manim.community/en/stable/) may be relevant.

## Jira Board

https://cs399-team33.atlassian.net/jira/software/projects/CT/boards/1

# Setup

## Dependencies

### Python

1. Download and install [here](https://www.python.org/).
    1. At least Python 3.10.
2. Make sure to tick Add to PATH during setup!

### FFmpeg

#### Windows

1. Download FFmpeg from [here](https://ffmpeg.org/).
    1. Make sure you download a packaged executable.
    2. Alternatively, you can manually build one yourself.
2. Extract and save anywhere.
3. Add to PATH manually.
3. Restart computer.

#### Mac

```brew install py3cairo ffmpeg```

Additionally, if on *Apple Silicon* (Such as M1 or similar):

```brew install pango scipy```

# Installation

## Source from GitHub

Clone the repo using your preferred method. Necessary package and source inside `src/zoomagrams`.
To ensure you have all required Python dependencies, run:

```pip install -r requirements.txt```

From here you can use the package directly or install it.

### Building an Installable Distribution

Once cloned, run the following in the local repo to create an installable distribution:

```py -m pip install --upgrade build```

```py -m build```

And to install locally:

```pip install dist/zoomagrams-1.0.0.tar.gz```

For Mac, use `python3`.

# Usage examples

`demo.py` contains three example animations, bubble sort, selection sort and a generic graphic animation. You can see the examples in action by running `manim -pql demo.py <AnimationClassName>`, e.g. `manim -pql demo.py Demo` or `manim -pql demo.py SelectionSort`.

See [here](https://docs.manim.community/en/stable/guides/configuration.html) for Manim's CLI rendering flags.

# Future plan

- Expand tree functionality.
- Improve the developer experience, e.g. add better abstractions around the function calls and make operations more intuitive.
- Try create animations for different algorithms for data structures such as linked list, hash table, etc. Note down the potential improvements and execute them.
  - More functionality for Lists (split, merge, etc. for usage in Merge Sort and Quicksort)
  - The goal is to make sure we have got every foundational function covered for a data structure so educators can create whatever animations they want with a data structure.
- Increase the performance of our API.
- Create a website similar to Scratch where it allows other people to learn data structures by creating their own animations.
  - Instead of creating the animations from scratch, they can also specify the data structure, algorithm and the input, then the website will output a downloadable animation for the user.
  - If the demand of this website is high, we can create a web API for users to interact over HTTP.

# Documentation

DISCLAIMER: We assume that you are familiar with Manim.
Trees are not functional in a way that we are happy with in our final product, so we are omitting the documentation. The code is still published.

## Config

The factory configuration can be found at `src/zoomagrams/config/default_config.toml`. This config is automatically loaded.
If you wish to use your own custom config, you can load a custom `.toml` file by using `load_config(PATH_TO_CONFIG)`, which will override the defaults.
Values for the configurable settings can be found in the Manim documentation found [here](https://docs.manim.community/en/stable/)

## Objects

### class ListElementCell(int value, **kwargs)

- Extends Manim's [`Square`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html)
- Defaults for `side_length`, `color`, `fill_color`, `fill_opacity` found in `default_config.toml`
- `**kwargs` is NOT passed through to `Square(**kwargs)`

#### Attributes

- `data`, the number element displayed

#### Methods

- `move(self, **kwargs)`, if `target` is specified, the cell moves towards the target. If `mag` is specified, the cell moves in the given magnitude (UP, DOWN, LEFT, RIGHT)
- `shade(color, opacity=0.5)`, shades the cell the given colour with the given opacity.
- `unshade()`, returns shading and opacity to the defaults specified in `default_config.toml`

## class ListGraphic(list, **kwargs)

- Extends Manim's [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html)
- `**kwargs` are passed through to `ListElementCell(int value, **kwargs)`

#### Attributes

- `default_attributes`, which is just `**kwargs`

#### Methods

- `swap_elements(e1, e2)`, swaps the posititions of elements with index `e1` and `e2`
- `raise_elements(*args)`, raises the elements of with given indexes in `*args`
- `lower_elements(*args)`, lowers the elements of with given indexes in `*args`
- `shade(n, color, opacity=0.5)`, shades element with index `n` to `color` with given `opacity`
- `unshade(n)`, returns shading and opacity of the element with index `n` to the defaults specified in `default_config.toml`
- `pop(n)`, pop element `n` from the list. If `n` is not specified, pop the last element.
- `insert(v, i)`, insert element of value `v` at index `i`.
- `append(n)`, insert element `n` at the end of the list

### class Subcaption(text, downshift=3, **kwargs)

- Extends Manim's [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html)
- `downshift` specifies how far down to shift the subcaption on the screen
- `**kwargs` is passed through to `Text(**kwargs)`

#### Attributes

#### Methods


