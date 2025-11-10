from typing import List, Tuple

def program4A(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """Solution to Program 4A - Top-down recursive DP with memoization
    Θ(n²) when k is small, Θ(n + (n-k)²) general.

    Uses a 2D DP formulation: dp[i][last] = maximum value considering 
    vaults 0..i-1 where 'last' is the index of the last vault taken 
    (or -1 if none)
    
    Parameters:
        n (int): number of vaults
        k (int): spacing constraint (no two chosen vaults within k)
        values (List[int]): values of the vaults
        
    Returns:
        int: maximal total value
        List[int]: 1-indexed indices of chosen vaults
    """

    memo = {}

    def dp(i: int, last_taken: int) -> int:
        """Returns max value considering vaults from i..n-1, 
        given last vault taken was last_taken (-1 if none)."""
        if i >= n:
            return 0

        if (i, last_taken) in memo:
            return memo[(i, last_taken)]

        # Option 1: Skip vault i
        skip_value = dp(i + 1, last_taken)

        # Option 2: Take vault i (only if spacing allows)
        take_value = 0
        if last_taken == -1 or i - last_taken > k:
            take_value = values[i] + dp(i + 1, i)

        memo[(i, last_taken)] = max(skip_value, take_value)
        return memo[(i, last_taken)]

    # Compute maximum value
    max_value = dp(0, -1)

    # Reconstruct chosen vaults
    chosen_vaults = []
    i = 0
    last_taken = -1

    while i < n:
        skip_value = dp(i + 1, last_taken) if i + 1 <= n else 0
        take_value = 0
        if last_taken == -1 or i - last_taken > k:
            take_value = values[i] + (dp(i + 1, i) if i + 1 <= n else 0)

        if (last_taken == -1 or i - last_taken > k) and dp(i, last_taken) == take_value:
            chosen_vaults.append(i + 1)  # Convert to 1-indexed
            last_taken = i
            i += k + 1  # skip k vaults
        else:
            i += 1

    return max_value, chosen_vaults


if __name__ == "__main__":
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    m, indices = program4A(n, k, values)
    print(m)
    for idx in indices:
        print(idx)
