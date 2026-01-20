# Leetcode 334
# time: O(n)
class Solution:
    def increasingTriplet(self, nums) -> bool:
        first = float('inf')
        second = float('inf')
        for i in range(len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                # print(f"f {first}, s {second}")
                return True
        return False

sol = Solution()
print(sol.increasingTriplet([1,1,-2,6]))