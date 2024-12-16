n = int(input())


def check(input_str):
    if int(input_str) % 19 == 0:
        return "Yes"
    elif input_str.find("19") != -1:
        return "Yes"
    return 'No'


for _ in range(n):
    print(check(input()))
