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
        n, q = map(int, read().split())
        arrA = list(map(int, read().split()))
        arrB = list(map(int, read().split()))
        queries = [tuple(map(int, read().split())) for _ in range(q)]
        ans = solve(n, q, arrA, arrB, queries)

        # ---------- INPUT PATTERN 3 ----------
        # n = int(read())
        # grid = [read().strip() for _ in range(n)]
        # ans = solve(n, grid)

        # ---------- INPUT PATTERN 4 ----------
        # a, b, c = map(int, read().split())
        # ans = solve(a, b, c)

        # write(str(ans) + "\n")
        # for lists
        write(" ".join(map(str, ans)) + "\n")

def solve(n, q, A, B, queries):
    results = []
    # maximize vertically
    for i in range(n):
        if A[i] < B[i]:
            A[i] = B[i]
    # maximize horizontally
    for i in range(n-1):
        if A[i] < A[i+1]:
            A[i] = A[i+1]
    for query in queries:
        # sum the range
        for l, r in [query]:
            results.append(sum(A[l-1:r]))
    return results


if __name__ == "__main__":
    main()
