# Leetcode 1456
# time: O(n)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        maximum = 0
        for i in range(k):
            if s[i] in vowels:
                maximum += 1
        
        curr = maximum
        leftEnd = 0
        for i in range(k, len(s)):

            if s[leftEnd] in vowels:
                curr -= 1
            leftEnd += 1

            if s[i] in vowels:
                curr += 1

            print(f"back {s[leftEnd]}, front {s[i]}, curr {curr}")
            
            if curr > maximum:
                maximum = curr

        return maximum

sol = Solution()
print(sol.maxVowels("abciiidef", 4))