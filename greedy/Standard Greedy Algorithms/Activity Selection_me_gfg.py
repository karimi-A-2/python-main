# User function Template for python3

class Solution:
    
    # Function to find the maximum number of activities that can
    # be performed by a single person.
    def activitySelection(self, n, start, end):
        my_list = []
        for i in range(n):
            my_list.append([start[i], end[i]])
        
        def my_lambda(item):
            return item[1]
        
        my_list.sort(key=my_lambda)
        max_count = 0
        current_end = 0
        for i in range(n):
            if my_list[i][0] > current_end:
                max_count += 1
                current_end = my_list[i][1]
            else:
                continue
        return max_count


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        start = list(map(int, input().strip().split()))
        end = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.activitySelection(n, start, end))
# } Driver Code Ends