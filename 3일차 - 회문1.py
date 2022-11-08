for t in range(1, 11):
    palindrome_length = int(input())
    arr = []
    for _ in range(8):
        arr.append(list(input()))
    count = 0
    for col in range(8):

        for first_row in range(9 - palindrome_length):
            row_str = []
            for mini_row in range(palindrome_length):
                row_str.append(arr[col][first_row + mini_row])
            if palindrome_length % 2 == 0:
                cutting_str = "".join(row_str)
                reversed_str = cutting_str[0:palindrome_length // 2]
                if reversed_str[::-1] == cutting_str[palindrome_length // 2:palindrome_length]:
                    count += 1
                col_str = []
                for mini_col in range(palindrome_length):
                    col_str.append(arr[first_row + mini_col][col])
                cutting_str = "".join(col_str)
                reversed_str = cutting_str[0:palindrome_length // 2]
                if reversed_str[::-1] == cutting_str[palindrome_length // 2:palindrome_length]:
                    count += 1
            else:
                cutting_str = "".join(row_str)
                reversed_str = cutting_str[0:palindrome_length // 2]
                if reversed_str[::-1] == cutting_str[palindrome_length // 2 +1:palindrome_length]:
                    count += 1
                col_str = []
                for mini_col in range(palindrome_length):
                    col_str.append(arr[first_row + mini_col][col])
                cutting_str = "".join(col_str)
                reversed_str = cutting_str[0:palindrome_length // 2]
                if reversed_str[::-1] == cutting_str[palindrome_length // 2 + 1:palindrome_length]:
                    count += 1
    print("#" + str(t), count)
