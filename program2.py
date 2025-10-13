import sys

def solve():
    first = sys.stdin.readline().strip()
    if not first:
        return
    n, k = map(int, first.split())
    values = list(map(int, sys.stdin.readline().strip().split()))

    # Step 1 find index p (minimum value)
    p = 0
    for i in range(1, n):
        if values[i] < values[p]:
            p = i

    # Step 2 select from the left segment
    left = []
    i = 0
    while i <= p - (k + 1):
        left.append(i + 1)
        i += (k + 1)

    # Step 3 select from right segment
    right = []
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

    out = [str(total)] + [str(idx) for idx in indices]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
