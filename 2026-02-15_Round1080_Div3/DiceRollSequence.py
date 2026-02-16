import sys

def build_dice_adjacency():
    faces = {1, 2, 3, 4, 5, 6}
    
    # Standard opposite mapping
    opposite = {
        1: 6,
        6: 1,
        2: 5,
        5: 2,
        3: 4,
        4: 3
    }
    
    adjacency = {}
    
    for face in faces:
        adjacency[face] = list(faces - {face, opposite[face]})
    
    return adjacency

def solve(n, arr):
    adj = build_dice_adjacency()
    INF = 10**18

    # dp for previous position
    prev = [INF] * 7
    for v in range(1, 7):
        prev[v] = 0 if v == arr[0] else 1

    for i in range(1, n):
        cur = [INF] * 7
        for u in range(1, 7):
            base = prev[u]
            if base == INF:
                continue
            for v in adj[u]:
                cost = base + (0 if arr[i] == v else 1)
                if cost < cur[v]:
                    cur[v] = cost
        prev = cur
    return min(prev[1:7])


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



if __name__ == "__main__":
    main()
