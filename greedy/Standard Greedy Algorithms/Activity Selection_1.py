"""The following implementation assumes that the activities
are already sorted according to their finish time"""

"""Prints a maximum set of activities that can be done by a
single person, one at a time"""
# todo: read greedy

# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities

def printMaxActivities(s, f):
    n = len(f)
    print("The following activities are selected")
    
    # The first activity is always selected
    current = 0
    print(current, end=' ')
    
    # Consider rest of the activities
    for i in range(n):
        
        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[i] >= f[current]:
            print(i, end=' ')
            current = i


# Driver program to test above function
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
printMaxActivities(s, f)
