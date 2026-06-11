nums=[1,3,5,2,4,8,2,2]

while len(nums) > 1:
            newNums = []

            for i in range(0, len(nums), 2):
                j = i // 2

                if j % 2 == 0:
                    newNums.append(min(nums[i], nums[i + 1]))
                else:
                    newNums.append(max(nums[i], nums[i + 1]))

            nums = newNums

print(nums[0]) 