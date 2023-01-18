from typing import List
from manim import *
from .node import TreeNode
from ..config import CONFIG

def _get_parent(nodes,num):
    parent = None
    id = None
    for key, values in nodes.items():
        if num in values:
            parent = key
            id = values.index(num)
            break
    return (parent, id)

class TreeGraphic(Graph):
    def __init__(self, num, vertices = [], edges = [], nodes = {}, **kwargs):
        kwargs.setdefault("side_length", CONFIG["cell_size"])
        kwargs.setdefault("color", CONFIG["node_border_color"])
        kwargs.setdefault("fill_color", CONFIG["node_fill_color"])
        kwargs.setdefault("fill_opacity", CONFIG["node_fill_opacity"])
        kwargs.setdefault("font_size", CONFIG["node_font_size"])
        kwargs.setdefault("font_color", CONFIG["node_font_color"])
        kwargs.setdefault("font_opacity", CONFIG["node_font_opacity"])
        self.default_attributes = kwargs
        if len(vertices) == 0 and len(edges) == 0 and len(nodes) == 0:
            self._vertices = []
            self._vertices.append(num)
            self.nodes = {self._vertices[0] : [None, None]}
            self._edges = []
        elif num == None: 
            self._vertices = vertices
            self.nodes = nodes
            self._edges = edges
        self.elements = {x: TreeNode(x, **kwargs) for x in self._vertices}
        super().__init__(self._vertices, self._edges, layout="tree",
                         root_vertex=self._vertices[0], vertex_mobjects=self.elements, edge_config={"stroke_color": kwargs["color"], "buff": 0}, layout_config={"vertex_spacing": (1, 1)})
        # self.edge_updater = self.get_updaters()[0]
        self.remove_updater(self.get_updaters()[0])

    def _update_nodes_list(self):
        for key, value in self.nodes.items():
            if None in value:
                none_id = value.index(None)
                self.nodes[key][none_id] = self._vertices[-1]
                break
        self.nodes[self._vertices[-1]]=[None,None]

    def _update_edges(self):
        for key, values in self.nodes.items():
            if values[0] != None:
                if (key,values[0]) not in self._edges and (values[0], key) not in self._edges:
                    self._edges += [(values[0], key)]
                    self.add_edges((values[0], key))
            if values[1] != None:
                if (key,values[1]) not in self._edges and (values[1], key) not in self._edges:
                    self._edges += [(values[1], key)]
                    self.add_edges((values[1], key))

    def swap(self, n1, n2):
        animations = []
        if (n1, n2) in self._edges or (n2, n1) in self._edges:
            n1m = self._vertices.index(n1)
            n2m = self._vertices.index(n2)
            self._vertices[n1m], self._vertices[n2m] = self._vertices[n2m], self._vertices[n1m]
            n2_increment = self.vertices[n1].get_center() - self[n2].get_center()
            n1_increment = self[n2].get_center() - self[n1].get_center()
            n2_increment[2] += 1
            n1_increment[2] += 1    # manim scene moves objects based on the coordinate, so shifting it by 1 in z-direction changes the z-coordinate 
                                    # and manim scene can move an object on the same x,y coordinate.
                                    # e.g. Nodes 1 and 2 are on (1,1), manim can't move both at the same time. By makaing the z-coordinate different,
                                    # manim can successfully move the nodes because it has different coordinates
            animations.extend([self[n1].animate.shift(n1_increment), self[n2].animate.shift(n2_increment)])

            # making edges consistent
            new_edges = []
            for i in range(len(self._edges)):
                if not(n1 not in self._edges[i] and n2 not in self._edges[i]) and not (n1 in self._edges[i] and n2 in self._edges[i]):
                    if n1 in self._edges[i]:
                        index = abs(1-self._edges[i].index(n1)) # relative of n1
                        new_edges.append((self._edges[i][index], n2))
                    if n2 in self._edges[i]:
                        index = abs(1-self._edges[i].index(n2)) # relative of n2
                        new_edges.append((self._edges[i][index], n1)) 
                else:
                    new_edges.append(self._edges[i])
            for i in self._edges:
                self.remove_edges(i)
            for i in new_edges:
                self.add_edges(i)
            self._edges = [x for x in new_edges]

            return animations

        else: 
            raise IndexError("Edge between {} and {} does not exist".format(n1, n2))

    def _nodes_dict_after_swap(self, num, id = None, parent = None):
        if parent: # num is not root node
            numleft = self.nodes[num][0]
            numright = self.nodes[num][1]
            parentleft = self.nodes[parent][0]
            parentright = self.nodes[parent][1]
            grandparent = _get_parent(self.nodes, parent)
            if id == 0:
                self.nodes[num][0] = parent
                self.nodes[num][1] = parentright
                self.nodes[parent][0] = numleft
                self.nodes[parent][1] = numright
            if id == 1:
                self.nodes[num][0] = parentleft
                self.nodes[num][1] = parent
                self.nodes[parent][0] = numleft
                self.nodes[parent][1] = numright
            if grandparent[0]:
                self.nodes[grandparent[0]][grandparent[1]] = num
        else: #swap root node 
            if id == 0: # with left child node
                left = self.nodes[num][0]
                leftleft = self.nodes[left][0]
                leftright = self.nodes[left][1]
                right = self.nodes[num][1]
                self.nodes[num][0] = leftleft
                self.nodes[num][1] = leftright
                self.nodes[left][0] = num
                self.nodes[left][1] = right

            if id == 1: # with right child node
                right = self.nodes[num][1]
                rightleft = self.nodes[right][0]
                rightright = self.nodes[right][1]
                left = self.nodes[num][0]
                self.nodes[num][0] = rightleft
                self.nodes[num][1] = rightright
                self.nodes[right][0] = left
                self.nodes[right][1] = num

        new_dict = {num:[self.nodes[num][0], self.nodes[num][1]] for num in self._vertices}
        self.nodes = new_dict

    # SORTS THE NODES AFTER ADDING NODES 
    def sort(self, num, all_animations) -> List: 
        if len(all_animations) == 0:
            animations = []
        else:
            animations = all_animations
        # print("start of sorting", animations)
        # original
        parent = _get_parent(self.nodes, num)
        id = parent[1]
        if not parent[0]: # if node is root node 
            if self.nodes[num][0] and num < self.nodes[num][0]: # if root node needs a swap
                animations.extend(self.swap(num, self.nodes[num][0]))
                self._nodes_dict_after_swap(num, 0) # id = 0: root node swap with left child
                # print("animation after swapping root", animations)
                self.sort(num, animations)
            elif self.nodes[num][1] and num > self.nodes[num][1]:
                animations.extend(self.swap(num, self.nodes[num][1]))
                self._nodes_dict_after_swap(num, 1) # id = 1: root node swap with right child
                # print("animation after swapping root", animations)
                self.sort(num, animations)
            else:
                print("done sorting no swaps", animations)
                return animations
        elif (num < parent[0] and id == 0 or num > parent[0] and id == 1):
            done_left = True
            done_right = True
            if self.nodes[num][0]:
                if self.nodes[num][0] > num: # id 0 = left, 1 = right
                    done_left = False
            if self.nodes[num][1]:
                if self.nodes[num][1] < num:
                    done_right = False
            if done_left and done_right:
                # print("done sorting after swaps", animations)
                return animations

        animations.extend(self.swap(num, parent[0]))
        # print(animations)
        # update self.nodes list after swapping
        self._nodes_dict_after_swap(num, id, parent[0])
        self.sort(num, animations)

    def add_node(self, num):
        # self.add_updater(self.edge_updater)
        self.clear_updaters()
        animations = []
        self._vertices.append(num)
        kwargs = self.default_attributes
        self.add_vertices(num, vertex_mobjects = {num: TreeNode(num, **kwargs)})
        self._update_nodes_list()
        self._update_edges()

        # make adding vertices consistent
        g = TreeGraphic(num = None, vertices = self._vertices, edges = self._edges, nodes = self.nodes, layout="tree",
                         root_vertex=self._vertices[0], vertex_mobjects=self.elements, edge_config={"stroke_color": kwargs["color"], "buff": 0}, 
                         layout_config={"vertex_spacing": (1, 1)})
        g.clear_updaters()
        for i in g.vertices.keys():
            self.vertices[i].move_to(g.vertices[i].get_center())
        self.elements = {x: TreeNode(x, **kwargs) for x in self._vertices}
        self.update(self)

        print(self.nodes, self.edges)
        # # sort the nodes
        # self.clear_updaters()
        animations.append(self.animate.shift([0,0,0.04]))
        self.sort(num, animations)

        if animations:
            return AnimationGroup(*animations)
        else:
            return AnimationGroup(*animations)
