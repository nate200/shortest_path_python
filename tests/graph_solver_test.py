import pytest
from unittest import TestCase
from models.graph_node import Node
from core import graph_solver


def test_file_not_exist():
    filename = "whatever.haha"
    with pytest.raises(Exception) as exc_info:
        graph_solver.solve_shortest_path_graph(filename, "A", "B")

    assert str(exc_info.value) == f"File:[{filename}] doesn't exist"


@pytest.mark.parametrize("s_node, e_node", [("nonExistingNode", "I"), ("A", "nonExistingNode")])
def test_start_node_not_exist(s_node, e_node):
    filename = "t1.csv"
    with pytest.raises(Exception) as exc_info:
        graph_solver.solve_shortest_path_graph(filename, s_node, e_node)

    assert str(exc_info.value) == "Node:[nonExistingNode] doesn't exist in the given graph file"


def test_start_eq_goal():
    filename = "t1.csv"
    start = "A"
    end = "A"
    with pytest.raises(Exception) as exc_info:
        graph_solver.solve_shortest_path_graph(filename, start, end)

    assert str(exc_info.value) == f"start and destination node must not be the same: [{start} == {end}]"


def test_csv_graph():
    node_A = Node('A')
    node_B = Node('B')
    node_C = Node('C')
    node_D = Node('D')
    node_E = Node('E')
    node_F = Node('F')
    node_G = Node('G')
    node_H = Node('H')
    node_I = Node('I')
    node_0 = Node('0')
    node_A.add_direction('B', 5)  # 'A': {'B': 5, 'D': 3, 'E': 4},
    node_A.add_direction('D', 3)
    node_A.add_direction('E', 4)
    node_B.add_direction('A', 5)  # 'B': {'A': 5, 'C': 4},
    node_B.add_direction('C', 4)
    node_C.add_direction('B', 4)  # 'C': {'B': 4, 'G': 2},
    node_C.add_direction('G', 2)
    node_D.add_direction('A', 3)  # 'D': {'A': 3, 'G': 6},
    node_D.add_direction('G', 6)
    node_E.add_direction('A', 4)  # 'E': {'A': 4, 'F': 6},
    node_E.add_direction('F', 6)
    node_F.add_direction('E', 6)  # 'F': {'E': 6, 'H': 5},
    node_F.add_direction('H', 5)
    node_G.add_direction('C', 2)  # 'G': {'C': 2, 'D': 6, 'H': 3},
    node_G.add_direction('D', 6)
    node_G.add_direction('H', 3)
    node_H.add_direction('G', 3)  # 'H': {'G': 3, 'F': 5},
    node_H.add_direction('F', 5)
    node_I.add_direction('0', 0)  # 'I': {'0': 0},
    node_0.add_direction('I', 0)  # '0': {'I': 0}
    expected = {
        'A': node_A,
        'B': node_B,
        'C': node_C,
        'D': node_D,
        'E': node_E,
        'F': node_F,
        'G': node_G,
        'H': node_H,
        'I': node_I,
        '0': node_0,
    }

    actual = graph_solver.read_graph_from_csv("t1.csv")

    TestCase().assertDictEqual(expected, actual)


def test_unreachable():
    filename = "t1.csv"
    s_node = "A"
    e_node = "I"

    actual = graph_solver.solve_shortest_path_graph(filename, s_node, e_node)

    assert actual is None


@pytest.mark.parametrize("file, s_node, e_node, expected_path, expected_cost", [
    ("t1.csv", "A", "B", ["A", "B"], 5),
    ("t1.csv", "H", "A", ["H", "G", "D", "A"], 12),
    ("t1.csv", "B", "A", ["B", "A"], 5),
    ("t1.csv", "C", "F", ["C", "G", "H", "F"], 10),
    ("t1.csv", "F", "G", ["F", "H", "G"], 8),
    ("t1.csv", "F", "C", ["F", "H", "G", "C"], 10)])
def test_shortest_path(file, s_node, e_node, expected_path, expected_cost):
    actual = graph_solver.solve_shortest_path_graph(file, s_node, e_node)

    assert actual["cost"] == expected_cost
    assert all([a == b for a, b in zip(actual["path"], expected_path)])
