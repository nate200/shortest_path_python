import csv
import os.path
from models.graph_node import Node
def solve_shortest_path_graph(filename: str, sNodeLabel: str, eNodeLabel: str):
    if not os.path.exists(filename):
        raise Exception(f"File:[{filename}] doesn't exist")
    graph = get_graph_from_csv(filename)

    if sNodeLabel == eNodeLabel:
        raise Exception(f"start and destination node must not be the same: [{sNodeLabel} == {eNodeLabel}]")
    if not sNodeLabel in graph:
        raise Exception(f"Node:[{sNodeLabel}] doesn't exist in the given graph file")
    if not eNodeLabel in graph:
        raise Exception(f"Node:[{eNodeLabel}] doesn't exist in the given graph file")

    sNode: Node = graph[sNodeLabel]
    eNode: Node = graph[eNodeLabel]
    find_shortest_path(graph, sNode, eNode)
    currNode: Node = eNode
    if currNode.fromNode:
        path = []
        while currNode.name != sNodeLabel:
            path.append(currNode.name)
            currNode = currNode.fromNode
        path.append(sNodeLabel)
        return {"path": path[::-1], "cost": eNode.currCost}
    else:
        return None
def get_graph_from_csv(filename):
    graph = {}
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            fromLabel: str = row[0]
            toLabel: str = row[1]
            cost: int = int(row[2])
            if fromLabel in graph:
                from_node = graph[fromLabel]
            else:
                from_node = Node(fromLabel)
                graph[fromLabel] = from_node
            if toLabel in graph:
                to_node = graph[toLabel]
            else:
                to_node = Node(toLabel)
                graph[toLabel] = to_node

            from_node.add_direction(toLabel, cost)
            to_node.add_direction(fromLabel, cost)
    #print(str(graph))
    return graph

def find_shortest_path(graph, sNode: Node, eNode: Node):
    sNode.currCost = 0
    eNode.currCost += 1
    q = [sNode.name]
    while q:
        currNode: Node = graph[q.pop()]
        for toNodeLabel, cost in currNode.direction.items():
            toNode: Node = graph[toNodeLabel]
            newCost: int = currNode.currCost + cost
            if newCost < eNode.currCost and newCost < toNode.currCost:
                toNode.currCost = newCost
                toNode.fromNode = currNode
                if toNode.name != eNode.name:
                    q.append(toNode.name)