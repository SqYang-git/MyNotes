def fibonacci(num):
    if num <= 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(fibonacci(num))

for n in numbers:
    print(n)
