import sys

def solve(tasks):
    n = len(tasks)
    dp = [0.0] * (n+2)

    for i in range(n-1, -1, -1):
        c, p = tasks[i]
        mult = 1-p/100.0

        skip = dp[i+1]
        take = c + mult * dp[i+1]

        dp[i] = max(skip, take)
    
    return dp[0]


def main():
    read = sys.stdin.readline
    write = sys.stdout.write

    t = int(read())

    for _ in range(t):

        # ---------- INPUT PATTERN 1 ----------
        tasks = []
        for _ in range(2):
            task = list(map(int, read().split()))
            tasks.append(task)
        ans = solve(tasks)

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
        # for lists
        #write(" ".join(map(str, ans)) + "\n")



if __name__ == "__main__":
    main()
