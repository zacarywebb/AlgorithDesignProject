from typing import List, Tuple


def program3(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """Solution to Program 3 (Naïve 2^n search, no memoization)

    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults (1-indexed, increasing)
    """

    def dfs(i: int) -> Tuple[int, List[int]]:
        # base case
        if i >= n:
            return 0, []

        # option 1 skip vault i next vaault to explore is i+1
        skipVal, skipIndecies = dfs(i + 1)

        # option 2 use vault i next vault to explore is i+k+1
        restValue, restIndex = dfs(i + k + 1)

        # add vault total from rest at index i (current)
        currentVal = values[i] + restValue

        # store as 1-based
        currentInicies = [i + 1] + restIndex

        # compare options
        if currentVal > skipVal:
            # taking current vault higher
            return currentVal, currentInicies
        else:
            return skipVal, skipIndecies

    # start recursion at first vault
    maxVal, maxIndices = dfs(0)
    return maxVal, maxIndices


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    m, indices = program3(n, k, values)
    print(m)
    for i in indices:
        print(i)