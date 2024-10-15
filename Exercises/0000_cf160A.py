n = int(input())
list_values = list(map(int, input().split()))

list_values.sort(reverse=True)
sum_values = sum(list_values)
my_coins = 0
my_coins_value = 0
for i in list_values:
    my_coins_value += i
    my_coins += 1
    if my_coins_value > sum_values/2:
        break

print(my_coins)
