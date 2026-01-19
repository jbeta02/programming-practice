# 1071. Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        pattern = ""
        pattern_size = 1

        i = 0
        j = 0

        len1 = len(str1)
        len2 = len(str2)

        biggerStr = ""
        smallerStr = ""

        if len1 > len2:
            pattern = str2
            pattern_size = len2
            biggerStr = str1
            smallerStr = str2
        else:
            pattern = str1
            pattern_size = len1
            biggerStr = str2
            smallerStr = str1

        biggerLen = len(biggerStr)
        smallerLen = len(smallerStr)

        while i < biggerLen:
            if pattern_size == 0:
                return ""
            
            for j in range(pattern_size):
                print("i, ", i)
                if i >= biggerLen or smallerLen % pattern_size != 0:
                    pattern_size -= 1
                    pattern = smallerStr[0:pattern_size]
                    i = 0
                    break
                if i < smallerLen:
                    if smallerStr[i] != pattern[j]:
                        pattern_size -= 1
                        pattern = smallerStr[0:pattern_size]
                        i = 0
                        break
                if biggerStr[i] != pattern[j]:
                    pattern_size -= 1
                    pattern = smallerStr[0:pattern_size]
                    i = 0
                    break
                else:
                    if i < biggerLen:
                        i += 1
                    else:
                        break

        if biggerLen != i:
            return ""
        else:
            return pattern
        

sol = Solution()
print(sol.gcdOfStrings("AA", "A"))

# TAUXXTAUXXTAUXXTAUXXTAUXX
# TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX


# TAUXXTAUXXTAUXX
# TAUXX