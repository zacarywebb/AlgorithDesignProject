import sys

def solve():
    # retrieve first two line inputs
    first = sys.stdin.readline().strip()
    # return if empty
    if not first:
        return
    # first line input n and k
    n, k = map(int, first.split())
    # vault values second lines {vi}
    vals = list(map(int, sys.stdin.readline().strip().split()))

    total = 0
    chosen = []

    # pick from the rightmost feasible, then jump left by (k+1)
    for i in range(n - 1, -1, -(k + 1)):
        total += vals[i]
        chosen.append(i + 1)  # store as 1-indexed

    chosen.reverse()  # print in increasing order

    out_lines = [str(total)] + [str(idx) for idx in chosen]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()