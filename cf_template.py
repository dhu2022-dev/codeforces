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
        # n, m = map(int, read().split())
        # arr = list(map(int, read().split()))
        # queries = [tuple(map(int, read().split())) for _ in range(m)]
        # ans = solve(n, m, arr, queries)

        # ---------- INPUT PATTERN 3 ----------
        # n = int(read())
        # grid = [read().strip() for _ in range(n)]
        # ans = solve(n, grid)

        # ---------- INPUT PATTERN 4 ----------
        # a, b, c = map(int, read().split())
        # ans = solve(a, b, c)

        write(str(ans) + "\n")


if __name__ == "__main__":
    main()
