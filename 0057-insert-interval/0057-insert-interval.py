class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: #insert before next interval
                res.append(newInterval)
                return res+intervals[i:] # here we are returning cause no next value will overlapp
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) # but new interval here can overlapp with coming intervals
                #so we are not returnning anything here, we are just adding ith interval to res
            else: # if overlapped
                newInterval = [min(newInterval[0], intervals[i][0]) , max(newInterval[1], intervals[i][1])]
                # as we are trying to reduce intervals that are overlapped
                # but we can't return here still, cause it can overlapp with upcoming next intervals
        res.append(newInterval) # if it is not returnned from the previous return statement
        return res