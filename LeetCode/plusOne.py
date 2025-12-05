# LeetCode 66.
# time: O(n) where n is len of digits list
# space: O(n)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits), 0, -1):
            curr = i-1
            if digits[curr] == 9:
                digits[curr] = 0
                if curr == 0:
                    digits.insert(0, 1)
                    return digits
            else:
                digits[curr] = digits[curr] + 1
                return digits