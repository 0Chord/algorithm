import sys

n = int(sys.stdin.readline().rstrip())
coin_list = [500, 100, 50, 10]


def count_coin(value: int):
    coins = 0
    for el in coin_list:
        coins += value // el
        value -= el * (value // el)

    return coins


print(count_coin(n))
