from typing import List, Tuple

def program4B(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """Solution to Program 4B - Iterative bottom-up DP
    
    dp[i] represents the maximum value considering 
    vaults from index 0 to i-1 (i.e., the first i vaults).
    
    For vault at index i (0-indexed), there are two choices:
    1. Skip vault i: dp[i+1] = dp[i]
    2. Take vault i: dp[i+1] = values[i] + dp[max(0, i-k)] 
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults
    
    Returns:
    int: maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    
    if n == 0:
        return 0, []
    
    # dp table where dp[i] is the maximum value we can get using the first i vaults
    dp = [0] * (n + 1)
    
    # Build dp table bottom-up
    for i in range(n):
        # Option 1: Don't take vault i
        dp[i + 1] = dp[i]
        
        # Option 2: Take vault i
        # If we take vault i, we cannot take any of the previous k vaults
        prev_idx = max(0, i - k)
        take_value = values[i] + dp[prev_idx]
        
        # Take the maximum
        dp[i + 1] = max(dp[i + 1], take_value)
    
    # Reconstruct the solution
    chosen_vaults = []
    i = n - 1
    
    while i >= 0:
        # Check if vault i was taken
        # It was taken if dp[i+1] == values[i] + dp[max(0, i-k)]
        # and this value is greater than dp[i] (not taking it)
        
        prev_idx = max(0, i - k)
        take_value = values[i] + dp[prev_idx]
        
        if dp[i + 1] == take_value and take_value > dp[i]:
            # Vault i was taken
            chosen_vaults.append(i + 1)  # Convert to 1-indexed
            # Next vault to consider is at least k+1 positions back
            i = i - k - 1
        else:
            # Vault i was not taken
            i = i - 1
    
    # Reverse to get ascending order
    chosen_vaults.reverse()
    
    return dp[n], chosen_vaults


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    m, indices = program4B(n, k, values)
    print(m)
    for i in indices:
        print(i)