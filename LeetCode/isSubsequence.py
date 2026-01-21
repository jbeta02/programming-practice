# Leetcode 392
# time: O(n)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        onS = 0 # subsequence

        if len(s) == 0:
            return True

        if len(t) == 0:
            return False

        for i in range(len(t)):
            # print("i", i)
            # print("onS", onS)
            if s[onS] == t[i]:
                onS += 1
            if onS == len(s):
                return True

        return False
    

sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))