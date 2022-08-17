""" Python program for activity selection problem
when input activities may not be sorted."""
from heapq import heappop, heappush
# todo: read more about heap

# Function to select activities
def SelectActivities(s, f):
    ans = []
    p = []
    # todo: why start and finish are altered whith each other
    # Pushing elements in the list
    for i, j in zip(s, f):
        heappush(p, (j, i))
    
    it = heappop(p)
    end = it[0]
    ans.append(it)
    
    # Sorting process
    while p:
        it = heappop(p)
        if it[1] >= end:
            end = it[0]
            ans.append(it)
    
    print("Following Activities should be selected.")
    for f, s in ans:
        print(f"[{s}, {f}]")


if __name__ == "__main__":
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    SelectActivities(s, f)