class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = sorted([(startTime[i],endTime[i],profit[i]) for i in range(len(startTime))])
        heap=[]
        cp,mp = 0,0                           # cp->current profit, mp-> max-profit
        for s,e,p in jobs:
            while heap and heap[0][0]<=s:
                et,tmp = heapq.heappop(heap)
                cp = max(cp,tmp)
            heapq.heappush(heap,(e,cp+p))
            mp = max(mp,cp+p)

        return mp