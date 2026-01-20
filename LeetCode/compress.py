# Leetcode 443
# time: O(n^2) due to insertions and deletions of list during iteration
class Solution:
    def compress(self, chars) -> int:
        last = chars[0]
        sum = 1
        i = 0
        if len(chars) == 1:
            return 1
        while i < len(chars):
            if i + 1 >= len(chars): # last loop
                if sum > 1:
                    sumList = list(str(sum))
                    for j in range(len(sumList)):
                        chars.insert(i+1+j, sumList[j])
                break
            elif chars[i+1] == last:
                sum += 1
                last = chars[i+1]
                del chars[i+1]
                i -= 1
            else:
                last = chars[i+1]
                if sum > 1:
                    sumList = list(str(sum))
                    for j in range(len(sumList)):
                        chars.insert(i+1+j, sumList[j])
                    i += len(sumList)
                    sum = 1
            i += 1
        return len(chars), chars
    
sol = Solution()
print(sol.compress(["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]))