import sys

def solve(*args):
    pass


def main():
    read = sys.stdin.readline
    write = sys.stdout.write

    t = int(read())

    for _ in range(t):

        # ---------- INPUT PATTERN 1 ----------
        # n = int(read())
        # arr = list(map(int, read().split()))
        # ans = solve(n, arr)

        # ---------- INPUT PATTERN 2 ----------
        n, s, x = map(int, read().split())
        arr = list(map(int, read().split()))
        ans = solve(n, s, x, arr)

        # ---------- INPUT PATTERN 3 ----------
        # n = int(read())
        # grid = [read().strip() for _ in range(n)]
        # ans = solve(n, grid)

        # ---------- INPUT PATTERN 4 ----------
        # a, b, c = map(int, read().split())
        # ans = solve(a, b, c)

        write(str(ans) + "\n")

def solve(n, s, x, arr):
    remainder = s - sum(arr)
    if remainder >= 0 and remainder % x == 0:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    main()
