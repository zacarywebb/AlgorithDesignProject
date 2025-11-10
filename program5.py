from typing import List, Tuple

def program5(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """Solution to Program 5 - Θ(n) DP optimized for Problem G
    
    dp[i] = maximum value achievable considering vaults up to index i.
    Recurrence:
        dp[i] = max(dp[i-1], values[i] + dp[i - k - 1])
    """
    if n == 0:
        return 0, []

    dp = [0] * n
    dp[0] = values[0]

    # Fill dp table in O(n)
    for i in range(1, n):
        take_val = values[i]
        if i - k - 1 >= 0:
            take_val += dp[i - k - 1]
        dp[i] = max(dp[i - 1], take_val)

    # Reconstruct chosen vault indices
    chosen = []
    i = n - 1
    while i >= 0:
        take_val = values[i] + (dp[i - k - 1] if i - k - 1 >= 0 else 0)
        if take_val >= (dp[i - 1] if i - 1 >= 0 else 0) and dp[i] == take_val:
            chosen.append(i + 1)
            i -= (k + 1)
        else:
            i -= 1

    chosen.reverse()
    return dp[-1], chosen


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    m, indices = program5(n, k, values)
    print(m)
    for i in indices:
        print(i)
