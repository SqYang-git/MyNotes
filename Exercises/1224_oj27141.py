def max_total_value(n, values):
    prefix_sum = 0
    max_k = 0
    hashmap = {}
    hashmap[0] = 0
    for j in range(1, n+1):
        prefix_sum += values[j-1]
        key = prefix_sum - 520 * j
        if key in hashmap:
            i = hashmap[key]
            k = j - i
            if k > max_k:
                max_k = k
        else:
            hashmap[key] = j
    return 520 * max_k


n = int(input())
values = list(map(int, input().split()))
result = max_total_value(n, values)
print(result)