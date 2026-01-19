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

if __name__ == "__main__":
    main()