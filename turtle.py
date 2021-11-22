f_in = open('turtle.in')
f_out = open('turtle.out', 'w')
arr = []
h, w = map(int, f_in.readline().split())

for i in range (h):
    line = list(map(int, f_in.readline().split()))
    arr += line
arr = [arr[i : i + w] for i in range(0, len(arr), w)]

for i in range (h - 2, -1, -1):
    arr[i][0] += arr[i + 1][0]
    
for i in range (1, w):
    arr[h - 1][i] += arr[h - 1][i - 1]

for i in range (min(h,w) - 1):
    arr[h - 2 - i][1 + i] += max(arr[h - 1 - i][1 + i], arr[h - 2 - i][0 + i])
    for j in range (h - i - 2):
        arr[h - 3 - i - j][i + 1] += max(arr[h - 3 - i - j][i], arr[h - 2 - i - j][i + 1])
    for k in range (w - i - 2):
        arr[h - 2 - i][i + 2 + k] += max(arr[h - 1 - i][i + 2 + k], arr[h - 2 - i][i + 1 + k])

f_out.write(str(arr[0][w-1]))
f_in.close()
f_out.close()