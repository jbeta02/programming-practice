# LeetCode 69.
# time: O(n)
# I basically did a linear search but a binary search could have been used instead for log n

class Solution:

    def mySqrt(self, x: int) -> int:
        sum = 0
        count = 1

        if x == 0:
            return 0

        while True:
            sum += (3 + 2 * (count - 1))

            if sum >= x:
                break

            count += 1

        return count