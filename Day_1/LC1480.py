class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        res = []
        for i in range(len(nums)):
            running_sum += nums[i]
            res.append(running_sum)
        return res


"""
built the prefix sum array by tracking a running total and appending it at each step. This runs in optimal $O(N)$ time.
"""