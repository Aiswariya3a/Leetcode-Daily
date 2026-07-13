class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_counts = {0: 1} # {prefix_sum: frequency}
        curr_sum = 0
        ans = 0
        
        for num in nums:
            # 1. Update the running sum
            curr_sum += num
            
            # 2. Check if the complement (curr_sum - k) exists in our map
            # If it does, add its frequency to ans
            if curr_sum - k in sum_counts:
                ans += sum_counts[curr_sum - k]
            
            # 3. Update the frequency of the current running sum in the map
            sum_counts[curr_sum] = sum_counts.get(curr_sum, 0) + 1
            
        return ans