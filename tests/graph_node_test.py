from models.graph_node import Node


def test_eq():
    expected = Node('A')
    expected.add_direction('B', 5)

    actual = Node('A')
    actual.add_direction('B', 5)

    assert expected == actual
