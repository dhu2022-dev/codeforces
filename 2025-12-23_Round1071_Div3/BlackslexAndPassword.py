import sys

def main():
    read = sys.stdin.readline
    write = sys.stdout.write

    t = int(read())
    for _ in range(t):
        k, x = map(int, read().split())

        res = solve(k, x)

        write(str(res) + "\n")

def solve(k, x):
    return k * x + 1

if __name__ == "__main__":
    main()