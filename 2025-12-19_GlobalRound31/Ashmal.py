import sys

def main():
    read = sys.stdin.readline
    write = sys.stdout.write

    t = int(read())

    for _ in range(t):
        n = int(read())          # line 1 of test case
        arr = read().split()     # line 2 of test case (n strings)

        res = solve(n, arr)
        write(res + "\n")

def solve(n, arr):
    s = arr[0]
    for i in range(1, n):
        s1 = s + arr[i]
        s2 = arr[i] + s
        if s2 < s1:
            s = s2
        else:
            s = s1
    return s

if __name__ == "__main__":
    main()