nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

hash = set(nums1)
result = set()

for num in nums2:
    if num in hash:
        result.add(num)

print(list(result))