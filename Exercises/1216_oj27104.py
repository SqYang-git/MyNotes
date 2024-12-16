N = int(input())
cameras = list(map(int, input().split()))
clips = []
i = 0
while i < N:
    if cameras[i] != 0:
        clips.append([i-cameras[i], i+cameras[i]])
    i += 1


def find_num(clips, start, end):
    clips.sort()
    ans = 0
    i = 0
    while i < len(clips):
        maxR = -1
        while i < len(clips) and clips[i][0] <= start:
            maxR = max(maxR, clips[i][1])
            i += 1
        ans += 1
        if maxR >= end:
            return ans
        start = maxR


print(find_num(clips, 0, N-1))
