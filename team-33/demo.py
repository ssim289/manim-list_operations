from src.zoomagrams import *
from manim import *
import random


class BubbleSort(ZoomagramsScene):
    def sort(self, data):
        mlist = ListGraphic(data)
        self.play(Create(mlist))
        for j in range(len(data) - 1):
            for i in range(0, len(data) - j - 1):
                self.play(mlist.raise_elements(i, i + 1))
                if mlist[i].data > mlist[i + 1].data:
                    self.play(mlist.shade(i, RED), run_time=0.25)
                    self.play(mlist.unshade(i), run_time=0.25)
                    self.play(mlist.swap_elements(i, i + 1))
                elif mlist[i].data < mlist[i + 1].data:
                    self.play(mlist.shade(i + 1, RED), run_time=0.25)
                    self.play(mlist.unshade(i + 1), run_time=0.25)
                else:
                    self.play(
                        mlist.shade(i, RED), mlist.shade(i + 1, RED), run_time=0.25
                    )
                    self.play(mlist.unshade(i), mlist.unshade(
                        i + 1), run_time=0.25)
                self.play(mlist.lower_elements(i, i + 1))
            self.play(mlist.shade(len(data) - j - 1, GREEN))
        self.play(mlist.shade(0, GREEN))

    def construct(self):
        data = [random.randint(0, 20) for x in range(6)]
        self.sort(data)


class SelectionSort(ZoomagramsScene):
    def sort(self, data):
        mlist = ListGraphic(data)
        s = Subcaption("Draw a random list")
        self.play(FadeIn(s))
        self.play(Create(mlist))
        self.play(FadeOut(s))
        for i in range(len(data)):
            minindx = min(range(i, len(data)), key=lambda i: mlist[i].data)
            s = Subcaption("Select first unsorted element")
            self.play(FadeIn(s))
            self.play(mlist.shade(i, BLUE))
            self.play(FadeOut(s))
            s = Subcaption("Select smallest element right of sorted section")
            self.play(FadeIn(s))
            self.play(mlist.shade(minindx, YELLOW))
            self.play(FadeOut(s))
            #           if i != minindx:
            s = Subcaption("Swap the elements")
            self.play(FadeIn(s))
            self.play(mlist.raise_elements(minindx, i))
            self.play(mlist.swap_elements(minindx, i))
            self.play(mlist.lower_elements(minindx, i))
            self.play(FadeOut(s))
            self.play(mlist.unshade(minindx), mlist.shade(i, GREEN))

    def construct(self):
        l = [random.randint(0, 10) for x in range(0, 6)]
        self.sort(l)


class Demo(ZoomagramsScene):
    def construct(self):
        mlist = ListGraphic([random.randint(0, 10) for x in range(0, 5)])
        s = Subcaption("Draw a random list")
        self.play(FadeIn(s))
        self.play(Create(mlist))
        self.wait(1)
        self.play(FadeOut(s))
        s = Subcaption("Append an element")
        self.play(FadeIn(s))
        self.play(mlist.append(5))
        self.wait(1)
        self.play(FadeOut(s))
        s = Subcaption("Insert element 3 in position 2")
        self.play(FadeIn(s))
        self.play(mlist.insert(3, 2))
        self.wait(1)
        self.play(FadeOut(s))
        s = Subcaption("Pop last element")
        self.play(FadeIn(s))
        self.play(mlist.pop())
        self.wait(1)
        self.play(FadeOut(s))
        s = Subcaption("Pop 4th element")
        self.play(FadeIn(s))
        self.play(mlist.pop(4))
        self.wait(1)
        self.play(FadeOut(s))


class TreeSort(ZoomagramsScene):
    def construct(self):
        tree = TreeGraphic(10)
        tree.clear_updaters()
        self.play(Create(tree))
        self.play(tree.add_node(1))
        self.play(tree.add_node(2))
        self.play(tree.add_node(3))
        self.play(tree.add_node(5))


with tempconfig({"quality": "high_quality", "preview": True, "save_as_gif": True, "output_file": "animated_list"}):
    scene = Demo()
    scene.render()
