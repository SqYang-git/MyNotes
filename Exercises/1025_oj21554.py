n = int(input())
list_t = list(map(int, input().split()))
indexed_list_t = list(enumerate(list_t))
indexed_list_t.sort(key=lambda x: x[1])
for i, t in indexed_list_t:
    print(i+1, end=" ")
print()
list_t.sort()
t = sum((n-1-i) * list_t[i] for i in range(n))/n
print(f"{t:.2f}")
