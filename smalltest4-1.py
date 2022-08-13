import math

arr = (166.5, 168.2, 177.3, 164.9, 172.0, 165.4)
avg = sum(arr) / len(arr)
print(avg)

s2 = 0.0

for i in arr:
    s2 += (i - avg)**2

s2 = s2 / len(arr)
print(s2)

s = math.sqrt(s2)

print(s)