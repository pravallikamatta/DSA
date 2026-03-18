nums = [100, 4, 200, 1, 3, 2]

h = {n: 1 for n in nums}

max_count = 0

for n in h:
    if n - 1 not in h:
        count = 1
        while n + count in h:
            count += 1
        max_count = max(max_count, count)

print(max_count)  