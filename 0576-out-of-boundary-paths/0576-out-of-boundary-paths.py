class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        @cache
        def path(x,y,movesRemaining):
            if movesRemaining < 0:
                return 0 
            if x>=m or x<0 or y>=n or y<0:
                return 1
            
            u = path(x,y+1,movesRemaining-1) # Move up
            r = path(x+1,y,movesRemaining-1) # Move right
            d = path(x,y-1,movesRemaining-1) # Move down
            l = path(x-1,y,movesRemaining-1) # Move left

            return l + r + u + d # Combine all our paths 
        
        return path(startRow,startColumn,maxMove) % 1000000007