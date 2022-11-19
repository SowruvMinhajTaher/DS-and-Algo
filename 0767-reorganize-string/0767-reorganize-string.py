class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        
        prev = None
        res = ''
        while maxHeap or prev:
            
            if prev and not maxHeap: #abaa
                return ''
            
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1 #maxHeap
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        
        return res
            