# 1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0

        len1 = len(word1)
        len2 = len(word2)

        combo = ""

        while i < len1 or j < len2:
            if i < len1:
                combo += word1[i] # concatination is not very eff, next time use list to append then convert list of char to string with "".join(combo)
            if j < len2:
                combo += word2[j]

            i += 1
            j += 1

        return combo