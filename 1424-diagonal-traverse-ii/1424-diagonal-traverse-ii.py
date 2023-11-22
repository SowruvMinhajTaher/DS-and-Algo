class Solution:
    def findDiagonalOrder(self, A: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(A)):
            for j in range(len(A[i])):
                d[i+j].append(A[i][j])
        return [v for k in d.keys() for v in reversed(d[k])]