# Leetcode 724
# time: O(n)
# space: O(n)

class Solution:
    def pivotIndex(self, nums) -> int:
        leftPrefixSum = [0]
        rightPrefixSum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            leftPrefixSum.append(nums[i] + leftPrefixSum[i])
            indexRight = (len(rightPrefixSum)-1) - i
            indexRightNums = (len(nums)-1) - i
            rightPrefixSum[indexRight-1] = (nums[indexRightNums] + rightPrefixSum[indexRight])

        for i in range(1, len(leftPrefixSum)):
            if leftPrefixSum[i] == rightPrefixSum[i-1]:
                return i-1
        return -1
    

# Leetcode 724
# time: O(n)
# space: O(1)

class Solution:
    def pivotIndex(self, nums) -> int:
        totalSum = 0

        for i in range(len(nums)):
            totalSum += nums[i]

        leftSum = 0
        for i in range(0, len(nums)):
            rightSum = totalSum - (nums[i] + leftSum)

            if rightSum == leftSum:
                return i

            leftSum += nums[i]
        return -1
    
sol = Solution()
print(sol.pivotIndex([1,7,3,6,5,6]))