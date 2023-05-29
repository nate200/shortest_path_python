# shortest_path_python

A Python project for solving the shortest path between 2 nodes in a bi-direction graph from a csv file

# How to use
The code can be run from a terminal with this command:
```
> python3 main.py
```
The program will ask the user to give 3 information: **csv file**, **starting node**, and the **destination node**
```
graph file name: t1.csv
starting node: A
destination node: B
```
If the path is found, the program will print out the path as well as the cost
```
Path from A to B is A->B, and have the cost of 5
```
Otherwise, the output will show the destination is unreachable
```
Path from A to B is unreachable
```

# Unit Test
This project uses **pytest**, you can run unit test of this project by using `pytest` command inside the directory
