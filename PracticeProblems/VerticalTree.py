# Codeforces Round 787 Problem D
import sys

def main():
    read = sys.stdin.readline
    write = sys.stdout.write

    t = int(read())
    for _ in range(t):
        n = int(read())
        arr = list(map(int, read().split()))
        res = solve(n, arr)
        write(str(len(res)) + "\n")
        for path in res:
            write(str(len(path)) + "\n")
            write(" ".join(map(str, path)) + "\n")
        write("\n")

def solve(n, arr):
    # construct the tree from parent array
    tree = dict()
    root = -1
    for i in range(1, n+1):
        if arr[i-1] == i:
            root = i
            continue
        if arr[i-1] not in tree:
            tree[arr[i-1]] = [i]
        else:
            tree[arr[i-1]].append(i)

    # Traverse paths and record them in order of traversal
    paths = []
    path = []
    toProcess = [root]
    while toProcess:
        pointer = toProcess.pop()
        path.append(pointer)
        while pointer in tree:
            if len(tree[pointer]) > 1: 
                # if there are multiple children, add the second one to the stack as a potential next path start
                for i in range(1, len(tree[pointer])):
                    toProcess.append(tree[pointer][i])
            pointer = tree[pointer][0]
            path.append(pointer)
        paths.append(path)
        path = []

    return paths

if __name__ == "__main__":
    main()