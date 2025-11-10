from typing import List, Tuple

def program4B(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """Solution to Program 4B - Iterative bottom-up DP
    Θ(n + (n-k)²)
    
    checks all valid previous positions when computing each state, creating
    quadratic behavior when k is small.
    
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
    
    dp = [0] * (n + 1)
    
    # Build dp table with quadratic approach
    for i in range(1, n + 1):
        # Option 1: Don't take vault i-1
        dp[i] = dp[i - 1]
        
        # Option 2: Take vault i-1
        # check all valid positions
        take_value = values[i - 1]
        best_prev = 0
        
        for j in range(0, max(0, i - k)):
            if dp[j] > best_prev:
                best_prev = dp[j]
        
        take_value += best_prev
        
        if take_value > dp[i]:
            dp[i] = take_value
    
    # Reconstruct solution
    chosen_vaults = []
    i = n - 1
    
    while i >= 0:
        # Check if vault i was taken
        take_value = values[i]
        best_prev = 0
        
        # Quadratic check again
        for j in range(0, max(0, i - k + 1)):
            best_prev = max(best_prev, dp[j])
        
        take_value += best_prev
        
        # Check if this matches our dp value and is better than skipping
        if dp[i + 1] == take_value and take_value > dp[i]:
            chosen_vaults.append(i + 1)  # 1-indexed
            i = i - k - 1  # Skip k positions
        else:
            i -= 1
    
    chosen_vaults.reverse()
    
    return dp[n], chosen_vaults


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    m, indices = program4B(n, k, values)
    print(m)
    for i in indices:
        print(i)