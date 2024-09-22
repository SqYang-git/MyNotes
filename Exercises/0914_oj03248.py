def min(a, b):
    while b != 0:
        a, b = b, a % b
    return a



while True:
    try:
        stra, strb = input().split()
        a = int(stra)
        b = int(strb)
        print(min(a, b))
    except EOFError:
        break
