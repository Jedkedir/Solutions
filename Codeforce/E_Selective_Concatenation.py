import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    t = int(next(it))
    
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        
        # We want to find the smallest index i such that b[i] != i.
        # To minimize this, we look at the first possible position of b[1].
        # b[1] comes from the first element of the 2nd subarray.
        # The 1st subarray must have at least 1 element.
        # Subarrays 3...k must have at least k-2 elements.
        # So the 2nd subarray can start at any index from index 1 to n-(k-1) 
        # (using 0-based indexing for the array a).
        
        possible_starts = a[1 : n - k + 2]
        
        # If any value in the range where S2 could start is NOT 1, 
        # we can make b[1] != 1. Min cost = 1.
        if any(x != 1 for x in possible_starts):
            print(1)
        else:
            # If all possible starts for S2 are 1, then b[1] is forced to be 1.
            # Now we check if we can make b[2] != 2.
            print(2)

if __name__ == "__main__":
    solve()