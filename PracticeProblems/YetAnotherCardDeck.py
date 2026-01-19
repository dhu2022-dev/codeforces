import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        # fallback for testing with input()
        n, q = map(int, input("Enter n q: ").split())
        cardColors = list(map(int, input("Enter cards: ").split()))
        queryColors = list(map(int, input("Enter queries: ").split()))
    else:
        it = iter(data)
        n = int(next(it))
        q = int(next(it))
        cardColors = [int(next(it)) for _ in range(n)]
        queryColors = [int(next(it)) for _ in range(q)]
    # print(cardColors)
    # print(queryColors)

    positions = [float('inf')] * 51 # index = color, value = position

    for i, c in enumerate(cardColors, start=1):
        if positions[c] == float('inf'):
            positions[c] = i

    output = []

    for color in queryColors:
        curr_pos = positions[color]
        output.append(str(curr_pos))

        # all colors that were in front of this one (pos < curr_pos) move back by 1
        for c in range(1, 51):
            if positions[c] < curr_pos:
                positions[c] += 1
        # query color moves to front
        positions[color] = 1

    print(" ".join(output))

if __name__ == "__main__":
    main()