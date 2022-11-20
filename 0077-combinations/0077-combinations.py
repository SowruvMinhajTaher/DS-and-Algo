class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(start, n+1): # we are only taking values greater because it is combination(1,2 == 2,1)
                comb.append(i)
                backtrack(i+1, comb) #start from i+1
                
                comb.pop()
                
        backtrack(1,[]) #starting from 1 and comb list
        
        return res