def twoSum(nums, target):
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
            print(numMap)

        return []  # No solution found

print(twoSum([2,7,11,15],9))