class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        from collections import defaultdict

        ans = 0
        lastH = {} # value : last point of seen... where the value last seen
        num = defaultdict(int)

        for i in range(len(garbage)):
            for char in garbage[i]:
                num[char] += 1
                lastH[char] = i
                
        pref = [] # building an prefix sum cause we should add the time value of travel cost
        res = 0
        for x in travel:
            res += x
            pref.append(res)

        ans = sum(num.values())
        for k, v in lastH.items():
            if lastH[k] != 0:
                ans += pref[lastH[k] - 1]
            
        return ans