# Leetcode 238
# time: O(n)
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeroCount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            else:
                nums[i-zeroCount] = nums[i]

        # print("zero", zeroCount)
        # print("len-1", len(nums)-1)
        for i in range(len(nums)-1, (len(nums)-1)-zeroCount, -1):
            # print("i", i)
            # print("num", nums[i])
            nums[i] = 0

        return nums

sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))