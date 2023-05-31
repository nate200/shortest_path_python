from core import graph_solver

def solve_graph_from_csv():
    filename: str = input('graph file name: ')
    sNodeLabel: str = input('starting node: ')
    eNodeLabel: str = input('destination node: ')

    ans = graph_solver.solve_shortest_path_graph(filename, sNodeLabel, eNodeLabel)
    print(f'Path from {sNodeLabel} to {eNodeLabel} is', end=" ")
    if ans:
        print('->'.join(ans["path"]), end="")
        print(f', and have the cost of {ans["cost"]}')
    else:
        print('unreachable')

if __name__ == '__main__':
    try:
        solve_graph_from_csv()
    except Exception as err:
        print("An exception occurred:", err)
