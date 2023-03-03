import sys

first_roma = list(sys.stdin.readline().rstrip())
second_roma = list(sys.stdin.readline().rstrip())

roma = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}

calc = 0
idx = 0
while True:
    if idx == len(first_roma):
        break
    if idx + 1 < len(first_roma) and roma[first_roma[idx + 1]] > roma[first_roma[idx]]:
        calc += roma[first_roma[idx + 1]] - roma[first_roma[idx]]
        idx += 2
    else:
        calc += roma[first_roma[idx]]
        idx += 1
idx = 0
while True:
    if idx == len(second_roma):
        break
    if idx + 1 < len(second_roma) and roma[second_roma[idx + 1]] > roma[second_roma[idx]]:
        calc += roma[second_roma[idx + 1]] - roma[second_roma[idx]]
        idx += 2
    else:
        calc += roma[second_roma[idx]]
        idx += 1
print(calc)

res = ""

while calc > 0:
    if calc >= 1000:
        res += "M"
        calc -= 1000
    elif 900 <= calc:
        res += "CM"
        calc -= 900
    elif 500 <= calc:
        res += "D"
        calc -= 500
    elif 400 <= calc:
        res += "CD"
        calc -= 400
    elif 100 <= calc:
        res += "C"
        calc -= 100
    elif 90 <= calc:
        res += "XC"
        calc -= 90
    elif 50 <= calc:
        res += "L"
        calc -= 50
    elif 40 <= calc:
        res += "XL"
        calc -= 40
    elif 10 <= calc:
        res += "X"
        calc -= 10
    elif 9 <= calc:
        res += "IX"
        calc -= 9
    elif 5 <= calc:
        res += "V"
        calc -= 5
    elif 4 <= calc:
        res += "IV"
        calc -= 4
    elif 1 <= calc:
        res += "I"
        calc -= 1
print(res)
