import sys

def main():
    read = sys.stdin.readline
    write = sys.stdout.write

    t = int(read())
    for _ in range(t):
        n = int(read())
        arr = list(map(int, read().split()))
        res = solve(n, arr)
        write(str(res) + "\n")

def solve(n, arr):
    if n == 1:
        return 0
    
    total = sum(abs(arr[i] - arr[i+1]) for i in range(n-1))

    max_save = 0

    # endpoints
    max_save = max(max_save, abs(arr[0] - arr[1]))
    max_save = max(max_save, abs(arr[n-1] - arr[n-2]))

    # interior spikes
    for i in range(1, n-1):
        save = abs(arr[i] - arr[i-1]) + abs(arr[i] - arr[i+1]) - abs(arr[i+1] - arr[i-1])
        max_save = max(max_save, save)

    return total - max_save

if __name__ == "__main__":
    main()