class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        res = []
        for i in range(len(nums)):
            running_sum += nums[i]
            res.append(running_sum)
        return res