class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         c = Counter(nums)
#         n = len(nums)
        
#         for i in range(n+1):
#             if i not in c:
#                 return i
#         N = len(nums)
#         sumExp = N*(N+1)//2
#         sumAct = sum(nums)
        
#         return sumExp - sumAct
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)