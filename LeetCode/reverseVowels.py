# time: O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:
        words = list(s) # changing string is better done through list
        left = 0
        right = len(words)-1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # find left
        for i in range(left, right):
            if words[i] in vowels:
                left = i
                # find right
                for j in range(right, left, -1):
                    if words[j] in vowels:
                        right = j
                        temp = words[i]
                        words[i] = words[j]
                        words[j] = temp
                        left += 1
                        right -= 1
                        break
        return "".join(words)

sol = Solution()
print(sol.reverseVowels("IceCreAm"))