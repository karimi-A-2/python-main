# Python Program for Representation of
# Sparse Matrix into Linked List

# Node Class to represent Linked List Node
class Node:
    __slots__ = "row", "col", "value", "next"
    
    def __init__(self, row=0, col=0, value=0, next=None):
        self.row = row
        self.col = col
        self.value = value
        self.next = next


# Linked List Class to store Sparse Matrix values
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size == 0
    
    def append_new_node(self, row, col, value):
        
        new = Node(row, col, value, None)
        
        if self.isempty():
            self.head = new
        else:
            self.end.next = new
        self.end = new
        
        self.size += 1
    
    def print_elements(self):
        print("(row, column, value):")
        end = self.head
        while end is not None:
            print("(" + str(end.row), end.col, end.value, sep=",", end=")\n")
            end = end.next


if __name__ == "__main__":
    
    linked_list = LinkedList()
    
    sparseMatrix = [[0, 0, 1, 0, 1],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0]]
    for i in range(4):
        for j in range(5):
            value = sparseMatrix[i][j]
            if value != 0:
                linked_list.append_new_node(i, j, value)
    
    linked_list.print_elements()
