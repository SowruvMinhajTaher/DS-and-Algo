class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        prefix_xor: list[int] = [0] + arr[:]
        n: int = len(arr) + 1
        for i in range(1, n):
            prefix_xor[i] ^= prefix_xor[i - 1]

        res = 0

        for start in range(n):
            for end in range(start + 1, n):
                if prefix_xor[start] == prefix_xor[end]:
                    res += end - start - 1

        return res