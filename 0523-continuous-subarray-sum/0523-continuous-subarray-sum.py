class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1} #doing that to handle for the first value cause we need at least two values
        #   remainder : endIndex
        total = 0
        for i, n in enumerate(nums):
            total += n
            r = total%k
            if r not in remainder:
                remainder[r] = i
            elif i-remainder[r]>1 :
                return True
        return False