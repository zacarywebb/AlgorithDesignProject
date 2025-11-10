from typing import List, Tuple

def program4A(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """Solution to Program 4A - Top-down recursive DP with memoization
    
    Uses dynamic programming where dp[i] represents the maximum
    value we can get considering vaults from index i to n-1.
    
    For each vault i, there are two choices:
    1. Skip vault i: dp[i] = dp[i+1]
    2. Take vault i: dp[i] = values[i] + dp[i+k+1] (skip next k vaults)
    
    Alg chooses the maximum of these two options.
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults
    
    Returns:
    int: maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    
    # Memoization dictionary to store computed results so we don't repeat overlapping subproblems
    memo = {}
    
    def dp(i):
        """Returns the maximum value we can get starting from vault i"""

        # Base case:
        if i >= n:
            return 0
        
        # Check if already computed
        if i in memo:
            return memo[i]
        
        # Choice 1: Skip vault i
        skip_value = dp(i + 1)
        
        # Choice 2: Take vault i and skip next k vaults
        take_value = values[i] + dp(i + k + 1)
        
        memo[i] = max(skip_value, take_value)
        return memo[i]
    
    # Compute the maximum value
    max_value = dp(0)
    
    chosen_vaults = []
    i = 0
    # reconstruct problem solution
    while i < n:
        # Check if vault i was taken
        skip_value = dp(i + 1) if i + 1 < n else 0
        take_value = values[i] + (dp(i + k + 1) if i + k + 1 < n else 0)
        
        if take_value >= skip_value and dp(i) == take_value:
            # vault i taken
            chosen_vaults.append(i + 1)  # Convert to 1-indexed
            i += k + 1  # Skip next k vaults
        else:
            # skipped vault i
            i += 1
    
    return max_value, chosen_vaults


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    m, indices = program4A(n, k, values)
    print(m)
    for i in indices:
        print(i)