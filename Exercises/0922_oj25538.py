def symmetry(n):
    binary_str = bin(n)[2:]
    return binary_str == binary_str[::-1]


if symmetry(int(input())):
    print("Yes")
else:
    print("No")
