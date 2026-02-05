# Leetcode 2215
# time: O(n)
# space: O(n + m)

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        for i in range(len(nums1)):
            if nums1[i] in set2:
                set1.remove(nums1[i])
                set2.remove(nums1[i])

        return [list(set1), list(set2)]