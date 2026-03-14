import sys

def solve(n, grid):
    #print(grid)
    colors = dict()
    for i in range(n):
        for j in range(n):
            if grid[i][j] not in colors:
                colors[grid[i][j]] = 1
            else:
                colors[grid[i][j]] += 1

    for color in colors:
        if int(colors[color]) > (n * (n-1)):
            return "NO"
    return "YES"


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
        n = int(read())
        grid = [read().strip().split(' ') for _ in range(n)]
        ans = solve(n, grid)

        # ---------- INPUT PATTERN 4 ----------
        # a, b, c = map(int, read().split())
        # ans = solve(a, b, c)

        write(str(ans) + "\n")
        # for lists
        #write(" ".join(map(str, ans)) + "\n")



if __name__ == "__main__":
    main()
