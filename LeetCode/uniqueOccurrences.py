# Leetcode 1207
# time: O(N)
# space: O(n)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        
        for item in arr:
            d[item] = d.get(item, 0) + 1

        val = d.values()

        valSet = set(val)

        return len(val) == len(valSet)