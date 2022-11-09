for t in range(1, 11):
    test_case = input().strip()
    sample_str = input().strip()
    search_str = input().strip()
    count = 0

    for idx in range(len(search_str) - len(sample_str) + 1):
        cutting_str = search_str[idx:idx + len(sample_str)]
        if cutting_str == sample_str:
            count += 1
    print("#" + str(t), count)
