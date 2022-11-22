T = int(input().rstrip())

for t in range(1, T + 1):
    input_str = list(input().rstrip())
    arr = [[] for _ in range(5)]
    for idx in range(1, len(input_str) + 1):
        if idx % 2 == 1:
            arr[0].append("..#..")

            if idx == 1:
                arr[2].append("#." + input_str[idx - 1] + ".#")
                arr[1].append(".#.#.")
                arr[3].append(".#.#.")
            else:
                arr[2].append("." + input_str[idx - 1] + ".#")
                arr[1].append("#.#.")
                arr[3].append("#.#.")
            arr[4].append("..#..")
        elif idx % 2 == 0:
            if idx == len(input_str):
                arr[0].append(".#..")
                arr[4].append(".#..")
            else:
                arr[0].append(".#.")
                arr[4].append(".#.")
            arr[1].append("#.#.")
            arr[2].append("." + input_str[idx - 1] + ".#")
            arr[3].append("#.#.")
    for el in arr:
        print("".join(el))
