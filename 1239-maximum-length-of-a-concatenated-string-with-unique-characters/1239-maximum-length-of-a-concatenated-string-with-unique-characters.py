class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charset = set()
        def overlap(charset, s):
            c = Counter(charset) + Counter(s)
            return max(c.values()) > 1
        """
        prev = set()
        for c in s:
            if c in charset or c in prev:
                return True
            prev.add(c)
        return False
        """
        
        def backtrack(i):
            if i==len(arr):
                return len(charset)
            
            res = 0
            if not overlap(charset, arr[i]):
                for c in arr[i]:
                    charset.add(c)
                res = backtrack(i+1)
                
                for c in arr[i]:
                    charset.remove(c)
            
            return max(res, backtrack(i+1)) #donot concatenate arr[i]
        
        return backtrack(0)