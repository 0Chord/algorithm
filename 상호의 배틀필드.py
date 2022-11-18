T = int(input().rstrip())

for t in range(1, T + 1):
    H, W = map(int, input().split())
    arr = []
    for _ in range(H):
        arr.append(list(input().rstrip()))
    N = int(input())
    command_arr = list(input().rstrip())
    idx = [0, 0]
    for col in range(H):
        for row in range(W):
            if arr[col][row] == "^" or arr[col][row] == "v" or arr[col][row] == "<" or arr[col][row] == ">":
                idx = [col, row]
    for el in command_arr:

        if el == "S":
            if arr[idx[0]][idx[1]] == "^":
                for col in range(idx[0], -1, -1):
                    if arr[col][idx[1]] == "*":
                        arr[col][idx[1]] = "."
                        break
                    elif arr[col][idx[1]] == "#":
                        break
            elif arr[idx[0]][idx[1]] == "v":
                for col in range(idx[0], H):
                    if arr[col][idx[1]] == "*":
                        arr[col][idx[1]] = "."
                        break
                    elif arr[col][idx[1]] == "#":
                        break
            elif arr[idx[0]][idx[1]] == "<":
                for row in range(idx[1], -1, -1):
                    if arr[idx[0]][row] == "*":
                        arr[idx[0]][row] = "."
                        break
                    elif arr[idx[0]][row] == "#":
                        break
            elif arr[idx[0]][idx[1]] == ">":
                for row in range(idx[1], W):
                    if arr[idx[0]][row] == "*":
                        arr[idx[0]][row] = "."
                        break
                    elif arr[idx[0]][row] == "#":
                        break
        elif el == "U":
            arr[idx[0]][idx[1]] = "^"
            if idx[0] > 0:
                if arr[idx[0] - 1][idx[1]] == ".":
                    arr[idx[0]][idx[1]] = "."
                    idx[0] -= 1
                    arr[idx[0]][idx[1]] = "^"
        elif el == "D":
            arr[idx[0]][idx[1]] = "v"
            if idx[0] < H - 1:
                if arr[idx[0] + 1][idx[1]] == ".":
                    arr[idx[0]][idx[1]] = "."
                    idx[0] += 1
                    arr[idx[0]][idx[1]] = "v"
        elif el == "L":
            arr[idx[0]][idx[1]] = "<"
            if idx[1] > 0:
                if arr[idx[0]][idx[1] - 1] == ".":
                    arr[idx[0]][idx[1]] = "."
                    idx[1] -= 1
                    arr[idx[0]][idx[1]] = "<"
        elif el == "R":
            arr[idx[0]][idx[1]] = ">"
            if idx[1] < W - 1:
                if arr[idx[0]][idx[1] + 1] == ".":
                    arr[idx[0]][idx[1]] = "."
                    idx[1] += 1
                    arr[idx[0]][idx[1]] = ">"
    print("#" + str(t), "".join(arr[0]))
    for e in range(1, len(arr)):
        print("".join(arr[e]))
