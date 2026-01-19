import sys

def main():
    read = sys.stdin.readline
    write = sys.stdout.write

    t = int(read()) # first line specifying number of test cases
    for _ in range(t): # process each test case
        n, m, h = map(int, read().split())
        
        arr = list(map(int, read().split()))

        operations = []
        for i in range(m):
            operations.append(list(map(int, read().split())))

        res = solve(n, h, arr, operations)

        write(" ".join(map(str, res)) + "\n")

def solve(n, h, arr, operations):
    original = arr[:]
    for op in operations:
        i = op[0]
        c = op[1]
        arr[i-1] += c
        if arr[i-1] > h:
            arr[:] = original
    return arr

if __name__ == "__main__":
    main()
