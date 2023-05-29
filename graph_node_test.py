from graph_node import Node
from unittest import TestCase

def test_eq():
    expected = Node('A')
    expected.add_direction('B', 5)

    actual = Node('A')
    actual.add_direction('B', 5)

    assert expected == actual