""" Python program for activity selection problem
when input activities may not be sorted."""


def MaxActivities(arr, n):
    selected = []
    
    # Sort jobs according to finish time
    Activity.sort(key=lambda x: x[1])
    
    # The first activity always gets selected
    current = 0
    selected.append(arr[current])
    
    for i in range(1, n):
        '''If this activity has start time greater than or
            equal to the finish time of previously selected
            activity, then select it'''
        if arr[i][0] >= arr[current][1]:
            selected.append(arr[i])
            current = i
        return selected


# Driver code
Activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
n = len(Activity)
selected = MaxActivities(Activity, n)
print("Following activities are selected :")
print(selected)

# This cde is contributed by kshitijjainm
