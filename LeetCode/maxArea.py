# Leetcode 11
# time: O(n)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        L = 0
        R = len(height)-1

        while L < R:
            waterH = min(height[L], height[R])
            currArea = (R-L) * waterH
            if currArea >= area:
                area = currArea

            if waterH == height[L]:
                L += 1

            if waterH == height[R]:
                R -= 1

        return area