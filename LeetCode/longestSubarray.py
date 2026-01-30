# Leetcode 1493
# time: O(n)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        last1Count = 0
        count1s = 0
        max1 = 0
        has0 = False

        i = 0
        for num in nums:
            if num == 1:
                count1s += 1

            else:
                has0 = True
                count1s -= last1Count
                last1Count = count1s

            if count1s > max1:
                max1 = count1s

            # print(f"i, count1s, lastC: {i} {count1s} {last1Count} max: {max1}")
            i += 1

        if not has0:
            max1 -= 1

        return max1