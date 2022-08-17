class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0


open_brackets = ["{", "(", "["]
close_brackets = ["}", ")", "]"]


def is_same_bracket(open_bracket, close_bracket):
    open_index = open_brackets.index(open_bracket)
    close_index = close_brackets.index(close_bracket)
    return open_index == close_index


string = input("Enter String: ")
# string = "(){([])}}}"

stack = Stack()
for char in string:
    print(char)
    if char in open_brackets:
        stack.push(char)
        print(char, "pushed")
    elif char in close_brackets:
        if stack.is_empty():
            print("Not Balanced: no open_bracket for", char)
            break
        popped_char = stack.pop()
        print(char, "popped")
        if popped_char not in open_brackets:
            print("Not Balanced:", popped_char, "not in open_brackets")
            break
        if not is_same_bracket(popped_char, char):
            print("Not Balanced:", popped_char, char, "not compatible")
            break
    else:
        print("invalid input")
else:
    if stack.is_empty():
        print("Balanced")
    else:
        s = ""
        for i in stack.stack:
            s += str(i)
        print("Not Balanced: stack is not empty at last: no close bracket for", s)

print("stack:", stack.stack)
# "{", "}", "(", ")", "[", "]"
# [()]{}{[()()]()}  Balanced
# [(])              Not Balanced
# [[()])              Not Balanced
# [[()])              Not Balanced
