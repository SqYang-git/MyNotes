n = int(input())
group_size = list(map(int, input().split()))
num_1 =group_size.count(1)
num_2 =group_size.count(2)
num_3 =group_size.count(3)
num_4 =group_size.count(4)
sum_taxis = num_4 + num_3 + (num_2 + 1) // 2 + (max(0, num_1-num_3-(num_2 % 2) * 2) + 3) // 4
print(sum_taxis)
