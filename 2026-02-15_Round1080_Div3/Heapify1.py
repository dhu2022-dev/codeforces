import sys

def main():
    read = sys.stdin.readline
    write = sys.stdout.write

    t = int(read())

    for _ in range(t):

        # ---------- INPUT PATTERN 1 ----------
        n = int(read())
        arr = list(map(int, read().split()))
        ans = solve(n, arr)

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

def solve(n, arr):
    b = sorted(arr)
    
    for k in range(1, n+1, 2):
        chain = []
        x = k
        while x <= n:
            chain.append(x-1)
            x *= 2
        cur = sorted(arr[i] for i in chain)
        tgt = sorted(b[i]   for i in chain)
        if cur != tgt:
            return "NO"
    
    return "YES"

if __name__ == "__main__":
    main()
