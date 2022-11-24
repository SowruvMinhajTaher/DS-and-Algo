class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = {s for s in nums} #hashset
        k = len(nums)
        def dfs(comb):
            if len(comb) == k:
                res = "".join(comb)             
                return None if res in strSet else res
            
            for i in range(0,2):
                comb.append(str(i))
                res = dfs(comb)

                if res is not None:
                    return res
                comb.pop()
            
        return dfs([])