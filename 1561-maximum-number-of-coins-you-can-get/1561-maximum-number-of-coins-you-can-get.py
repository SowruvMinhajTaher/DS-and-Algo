class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        me = 0
        j = n - 1

        for i in range(n//3):
            #created list of piles (starting first and last 2 one)
            temp = [piles[i], piles[j-1], piles[j]]   
            me += temp[1]
            # print(temp)
            j -= 2

        return me