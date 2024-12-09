out = []
for i in range(int(input())):
    n = int(input())
    ans, flag = 0, 1
    while n:
        test = 0
        if n % 2 == 0 and n//2 % 2 or n == 4:
            n //= 2
            test = n
        else:
            n -= 1
            test = 1
        if flag:
            ans += test
        flag ^= 1
    out.append(ans)
print("\n".join(map(str, out)))
