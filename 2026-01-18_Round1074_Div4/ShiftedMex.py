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
    nums = sorted(arr)

    best = 1
    cur = 1

    for i in range(1, l):
        if nums[i] == nums[i-1]:
            continue              # ignore duplicates
        if nums[i] == nums[i-1] + 1:
            cur += 1              # extend run
        else:
            cur = 1               # reset run
        if cur > best:
            best = cur
    
    return best

if __name__ == "__main__":
    main()
