class Node:
    def __init__(self, name):
        self.name = name
        self.direction = {}
        self.currCost = 999999
        self.fromNode: Node = None

    def __repr__(self):  # __str__
        return f'{self.name}:[' + str(self.direction) + ']'

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        if self.name != other.name:
            return False
        if len(self.direction) != len(other.direction):
            return False

        for nodeLabel in self.direction:
            if nodeLabel in other.direction:
                if self.direction[nodeLabel] != other.direction[nodeLabel]:
                    return False
            else:
                return False

        return True

    def add_direction(self, toNodeLabel, cost):
        self.direction[toNodeLabel] = cost