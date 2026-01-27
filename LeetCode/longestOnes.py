# Leetcode 1004
# time: O(n^2)

class Solution:
    def longestOnes(self, nums, k: int) -> int:
        max0 = 0
        left = 0
        curr1 = 0
        f = 0
        max1 = 0
        while f < len(nums):
            if k == 0:
                break
            if nums[f] == 1:
                curr1 += 1

            elif nums[f] == 0:
                max0 += 1
                curr1 += 1
                if max0 == k:
                    f += 1
                    break
            f += 1

        max1 = curr1
        for i in range(f, len(nums)):
            if nums[i] == 1:
                curr1 += 1
            
            elif nums[i] == 0:
                if k > 0:
                    curr1 += 1
                for j in range(left, len(nums)):
                    if nums[j] == 1:
                        curr1 -= 1
                    elif nums[j] == 0:
                        left = j+1
                        if k > 0:
                            curr1 -= 1
                        break
            
            if curr1 > max1:
                max1 = curr1
        
        return max1

sol = Solution()
# print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
# print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))