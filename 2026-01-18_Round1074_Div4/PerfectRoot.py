import sys

def main():
    read = sys.stdin.readline
    write = sys.stdout.write

    t = int(read()) # first line specifying number of test cases
    for _ in range(t): # process each test case
        a = int(read()) # as many variable::input as u need

        res = solve(a)

        write(str(res) + "\n")

def solve(a):
    nums = ""
    for i in range(1, a+1):
        nums += str(i) + " "
    return nums

if __name__ == "__main__":
    main()
