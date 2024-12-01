n, M = map(int, input().split())
times = [0]+list(map(int, input().split()))+[M]
length = len(times)

trigger = set()
for time in times:
    trigger.add(time)

buffer = [0] * (M + 1)
for i in range(1, length):
    if i % 2 == 1:
        for j in range(times[i - 1]+1, times[i]+1):
            buffer[j] = buffer[j - 1] + 1
    if i % 2 == 0:
        for j in range(times[i - 1]+1, times[i]+1):
            buffer[j] = buffer[j - 1]

max_t = buffer[M]

trials = set()
if times[1] != 1:
    trials.add(1)
for k in range(1, length - 1):
    if times[k]-1 not in trigger:
        trials.add(times[k] - 1)
    if times[k]+1 not in trigger:
        trials.add(times[k] + 1)
if times[length - 2] != M-1:
    trials.add(M - 1)


for trial in trials:
    max_t = max(max_t, buffer[trial]+(M-trial)-(buffer[M]-buffer[trial]))
print(max_t)
