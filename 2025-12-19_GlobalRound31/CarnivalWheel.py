import sys

def main():
    read = sys.stdin.readline
    write = sys.stdout.write

    t = int(read())
    for _ in range(t):
        l, a, b = map(int, read().split())

        res = solve(l, a, b)

        write(str(res) + "\n")

def solve(l, a, b):
    curr = (a + b) % l
    m = curr
    while curr != a:
        curr = (curr + b) % l
        m = max(m, curr)
    return m

if __name__ == "__main__":
    main()