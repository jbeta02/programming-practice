# LeetCode 70.
# time: O(n) 
# could also be done recursively

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: 
            return n

        left = 3
        right = 2

        for i in range(3, n):

            new = left + right
            
            right = left

            left = new
        return left
    

    

# recursive approach O(2^n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 1:
#             return 1

#         return self.climbStairs(n-1) + self.climbStairs(n-2)



# recursive with memory O(n)
# class Solution:
    # def climbStairs(self, n: int) -> int:
        
    #     # create a memoization table and initialize with -1
    #     mem = [-1] * (n + 1)

    #     return self.fib(n, mem)


    # def fib(self, n, mem):
    #     if n <= 1:
    #         return 1

    #     # check if val was already calculated
    #     if mem[n] != -1:
    #         return mem[n]

    #     mem[n] = self.fib(n-1, mem) + self.fib(n-2, mem)

    #     return mem[n]