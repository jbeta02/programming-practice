# Leetcode 643
# time: O(n)
class Solution:
    def findMaxAverage(self, nums, k) -> float:
        maximum = 0

        for i in range(k):
            maximum += nums[i]
        curr = maximum
        
        for i in range(k, len(nums)):

            lastVal = nums[i-k]
            nextVal = nums[i]

            curr -= lastVal
            curr += nextVal

            if curr > maximum:
                maximum = curr

        maximum /= k
        return maximum
    

sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))