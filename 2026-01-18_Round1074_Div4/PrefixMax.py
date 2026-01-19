import sys

def main():
    read = sys.stdin.readline
    write = sys.stdout.write

    t = int(read()) # first line specifying number of test cases
    for _ in range(t): # process each test case
        l = int(read())
        arr = list(map(int, read().split()))

        res = solve(l, arr)

        write(str(res) + "\n")

def solve(l, arr):
    total = 0
    largest = max(arr)
    for i in range(l):
        total += largest
    return total

if __name__ == "__main__":
    main()
