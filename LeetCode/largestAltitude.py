# Leetcode 1732
# time: O(n)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        presum = [0]
        for i in range(0, len(gain)):
            s = gain[i] + presum[i]
            presum.append(s)
        return max(presum)