# Leetcode 1679
# time: O(n^2)
# space: O(1)

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        anchor = 0
        search = len(nums)-1
        rightEdge = len(nums)-1
        count = 0

        if len(nums) <= 1:
            if len(nums) == 1 and nums[0] == k:
                return 1
            return 0
        
        while anchor < rightEdge:
            if anchor == search:
                anchor += 1
                search = rightEdge

            elif nums[anchor] + nums[search] == k:
                nums[search] = nums[rightEdge]
                anchor += 1
                rightEdge -= 1
                search = rightEdge
                count += 1

            else:
                search -= 1

            # print(f"anchor, search, rightE: {anchor}, {search}, {rightEdge}| a, s: {nums[anchor]}, {nums[search]} | {nums}")

        return count
    

# Leetcode 1679
# time: O(n)
# space: O(1)

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = len(nums)-1
        count = 0

        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                count += 1
            
            elif nums[left] + nums[right] < k:
                left += 1

            else:
                right -= 1

        return count
