nums = [1, 2, 3, -2, 5]
k = 5

s = 0
count = 0
h = {0: 1}

for n in nums:
    s += n
    count += h.get(s - k, 0)
    h[s] = h.get(s, 0) + 1

print(count)