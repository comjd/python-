"""
    1.记录所有图形
    2.计算总面积

    圆形，矩形..

"""


class GraphManager:
    def __init__(self):
        self.list_graph = []

    def total_area(self):
        result = 0
        for item in self.list_graph:
            result += item.computed_graph_area()
        return result


class Graph:
    def __init__(self, name=''):
        self.name = name

    def computed_graph_area(self):
        pass


class Circle(Graph):

    def __init__(self, name='', radius=0):
        super().__init__(name)
        self.radius = radius

    def computed_graph_area(self):
        super().computed_graph_area()
        return self.radius ** 2 * 3.14


class Rectangle(Graph):
    def __init__(self, name='', width=0, length=0):
        super().__init__(name)
        self.width = width
        self.length = length

    def computed_graph_area(self):
        super().computed_graph_area()
        return self.width * self.length


class Triangle(Graph):

    def __init__(self, name='', bottom=0, height=0):
        super().__init__(name)
        self.bottom = bottom
        self.height = height

    def computed_graph_area(self):
        super().computed_graph_area()
        return self.bottom * self.height / 2


gm = GraphManager()
c01 = Circle('圆', 5)
gm.list_graph.append(c01)
r01 = Rectangle('矩形', 6, 5)
gm.list_graph.append(r01)
t01 = Triangle('三角形', 4, 9)
gm.list_graph.append(t01)
print(str(gm.total_area()))
for item in gm.list_graph:
    print(item.name, item.computed_graph_area())
