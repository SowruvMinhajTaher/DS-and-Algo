# class Solution:
#     def findDiagonalOrder(self, A: List[List[int]]) -> List[int]:
#         d = defaultdict(list)
#         for i in range(len(A)):
#             for j in range(len(A[i])):
#                 d[i+j].append(A[i][j])
#         return [v for k in d.keys() for v in reversed(d[k])]

class Solution:
    def findDiagonalOrder(self, nums):
        diagonals = [deque() for _ in range(len(nums) + max(len(row) for row in nums) - 1)]
        for row_id, row in enumerate(nums):
            for col_id in range(len(row)):
                diagonals[row_id + col_id].appendleft(row[col_id])
        return list(chain(*diagonals))