import sys

def solve(n, k, p, m, arr):
    # n cards in deck
    # can play first k cards
    # p = wincon index
    # m = energy threshold
    # arr = energy values of cards
    if arr[p-1] > m:
        return 0
    if k >= n:
        x = m // arr[p-1]
    else:
        x = 0
        cost = 0
        while cost < m:
            if p <= k:
                # win con is playable, play it
                cost += arr[p-1]
                if cost > m:
                    break
                arr = arr[:p-1] + arr[p:] + [arr[p-1]]
                x += 1
                p = len(arr)
                #print("win con played")
                #print("p:", p)
                #print(arr)
            else:
                # cycle to win con
                min_cost = m+1
                min_index = -1
                for i in range(k):
                    if arr[i] < min_cost:
                        min_cost = arr[i]
                        min_index = i
                if cost + min_cost > m:
                    break
                cost += min_cost
                #print("min index:", min_index)
                #print("p:", p)
                if min_index < p-1:
                    # bump win con index down by 1 since a card before it was played
                    p -= 1
                # move played card to end of deck and bump up the rest
                arr = arr[:min_index] + arr[min_index+1:] + [arr[min_index]]
                #print(arr)
    return x


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
        n, k, p, m = map(int, read().split())
        arr = list(map(int, read().split()))
        ans = solve(n, k, p, m, arr)

        write(str(ans) + "\n")
        # for lists
        #write(" ".join(map(str, ans)) + "\n")



if __name__ == "__main__":
    main()
