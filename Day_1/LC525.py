class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Map to store {curr_sum: first_time_we_saw_this_index}
        sum_map = {0: -1} 
        curr_sum = 0
        max_len = 0
        
        for i in range(len(nums)):
            # 1. Update curr_sum (add 1 if nums[i] is 1, else subtract 1)
            if nums[i] == 1:
                curr_sum += 1
            else:
                curr_sum -= 1
                
            # 2. Check if we have seen this curr_sum before
            if curr_sum in sum_map:
                # Calculate length and update max_len if it's bigger
                max_len = max(i - sum_map[curr_sum], max_len)
                
            else:
                # Store the index where we first saw this sum
                sum_map[curr_sum] = i
                
                
        return max_len