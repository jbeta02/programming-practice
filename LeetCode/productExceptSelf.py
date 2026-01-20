
# LeetCode 238
# time: O(n^2)
# class Solution:
#     def productExceptSelf(self, nums):
#         target = 0
#         product = [1] * len(nums)
        
#         for target in range(len(nums)):
#             for i in range(len(nums)):
#                 if i == target:
#                     continue
#                 product[target] *= nums[i]

#         return product

# time: O(n)  
class Solution:
    def productExceptSelf(self, nums):
        product = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            product[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            product[i] *= suffix
            suffix *= nums[i]

        return product
    
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))