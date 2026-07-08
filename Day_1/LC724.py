class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        curr_sum = 0
        for i in range(len(nums)):
            if curr_sum == (total-curr_sum - nums[i]):
                return i
            curr_sum += nums[i]
        return -1
        

"""
Calculated the total sum of the array and then iterated through the array while maintaining a running sum. 
At each index, checked if the running sum equals the total sum minus the running sum minus the current element. 
If so, returned that index as the pivot index. 
This runs in optimal $O(N)$ time.
"""