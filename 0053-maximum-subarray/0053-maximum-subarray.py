class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMaxSum = float('-inf')
        curSum = float('-inf')
        
        for num in nums:
            if curSum < 0:
                curSum = num
            else:
                curSum += num
                
            if globalMaxSum<curSum:
                globalMaxSum = curSum
        
        return globalMaxSum