class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        '''
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
        '''
        strSet = {s for s in nums}
        def backtrack(i, cur): #index, currentString
            if i == len(nums):
                res = "".join(cur) 
                # as we converted string as list, so we are converting back to str
                return None if res in strSet else res
            res = backtrack(i+1, cur) #choosing 0 as we given it by default
            if res:
                return res
            
            cur[i] = "1"#choosing 1 
            res = backtrack(i+1, cur)
            if res:
                return res
            
        return backtrack(0,["0" for s in nums]) #converting into list as string is immutable in python