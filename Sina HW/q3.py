from collections import deque


class Node:
    
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        if self.right is None or self.left is None:
            return f'({self.value})'
        else:
            return f'({self.left}-o-{self.right})'


class NotEatableTree(ValueError):
    pass


def sort(node: Node):
    global count
    if node.left is None:
        return
    if node.left.value is None:
        sort(node.left)
    if node.right.value is None:
        sort(node.right)
    if node.left.value > node.right.value:
        node.left, node.right = node.right, node.left  # swap left and right
        count += 1
    node.value = node.left.value


def check(node: Node):
    global count, point
    if node.left is None:
        if node.value == point + 1:
            point += 1
        else:
            raise NotEatableTree()
        return
    check(node.left)
    check(node.right)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = map(int, input().split())
    q = deque()
    for num in arr:
        q.append(Node(num))
    # print(q)
    
    while len(q) > 1:
        left = q.popleft()
        right = q.popleft()
        q.append(Node(left=left, right=right))
    root = q.popleft()
    # print(root)
    count = 0
    point = 0
    sort(root)
    # print(root)
    try:
        check(root)
    except NotEatableTree:
        count = -1
    print(count)


'''
input:
4
8
6 5 7 8 4 3 1 2
4
3 1 4 2
1
1
8
7 8 4 3 1 2 6 5

output:
4
-1
0
-1
'''