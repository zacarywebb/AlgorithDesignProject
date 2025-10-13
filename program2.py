from typing import List, Tuple

def program2(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 2
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults
    Returns:
    int: maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    # Step 1 find index p (minimum value)
    p = 0
    for i in range(1, n):
        if values[i] < values[p]:
            p = i

    # Step 2 select from the left segment
    left: List[int] = []
    i = 0
    while i <= p - (k + 1):
        left.append(i + 1)
        i += (k + 1)

    # Step 3 select from right segment
    right: List[int] = []
    j = n - 1
    while j >= p + 1:
        right.append(j + 1)
        j -= (k + 1)
    right.reverse()

    # Step 4 handle possible overlap
    if left and right and (right[0] - left[-1] <= k):
        if values[left[-1] - 1] < values[right[0] - 1]:
            left.pop()
        else:
            right.pop(0)

    # Step 5 combine and compute total
    indices = left + right
    total = sum(values[idx - 1] for idx in indices)

    return total, indices


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    m, indices = program2(n, k, values)
    print(m)
    for i in indices:
        print(i)
