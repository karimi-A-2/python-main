from collections import deque


class Node:
    
    def __init__(self, num):
        self.num = num
        self.parent = None
        self.adjacent_list = []

    def __repr__(self):
        return f'{self.num} {[node.num for node in self.adjacent_list]}'


class NotConnectedGraph(ValueError):
    pass


no_nodes, no_edges = list(map(int, input().split()))
nodes = []
for i in range(no_nodes):
    nodes.append(Node(i + 1))
for _ in range(no_edges):
    a, b = list(map(int, input().split()))
    nodes[a - 1].adjacent_list.append(nodes[b - 1])
    nodes[b - 1].adjacent_list.append(nodes[a - 1])
q = deque()
root = nodes[0]
root.parent = root
q.append(root)
while len(q) > 0:
    popped = q.popleft()
    # print(popped)
    # print(popped.adjacent_list)
    for node in popped.adjacent_list:
        if node.parent is not None:
            continue
        node.parent = popped
        q.append(node)
try:
    for node in nodes:
        if node.parent is None:
            raise NotConnectedGraph()
    for node in nodes:
        print(f'{node.num} {node.parent.num}')
except NotConnectedGraph:
    print('not connected graph')
