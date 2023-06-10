'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
'''

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        result = 1
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key=lambda x:x[1])
        min_start = intervals[0][1]
        for i in range (1,len(intervals)):
            if intervals[i][0] < min_start:
              
              continue
            else:
              result +=1
              min_start = intervals[i][1]    
        
        return len(intervals)-result


        '''
        [[1,2],[2,3],[3,4],[1,3]]
        min_start=4

        [[1,2],[9,12],[20,21],[3,4], [8,10],[10,12]]

        [[1,2],[3,5], [4,10],[10,12],[9,12],[20,21]]


        min_start=2
        max_end = true
        {
            2:9
            12:20
            21:true

        }   {}
        '''