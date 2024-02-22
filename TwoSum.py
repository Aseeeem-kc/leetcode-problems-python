class Solution(object):
    def twoSum(self, nums, target):
        output = []
        for i in nums:
            diff = target - i
            for j in range(nums.index(i)+1, len(nums)):
                if (nums[j] == diff):
                  output.append(nums.index(i))
                  output.append(j)
        return output
            



solution_instance = Solution()
nums = [2,7,11]
target = 9
result = solution_instance.twoSum(nums, target)
print(result)



