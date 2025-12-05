# LeetCode 67.
# time: O(n) where n is len of longest str
# space: O(n)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        curr = 0
        output = ''
        a, b = self.sameLen(a, b)
        # print(a)
        # print(b)
        size = len(a)
        while curr < size:
            out, currCarry = self.add(a[(size-1)- curr], b[(size-1)- curr])
            nextCarry = False

            if carry == True:
                out, nextCarry = self.add(out, '1')
            
            carry = currCarry or nextCarry

            output = out + output

            # print("---")
            # print("out", out)
            # print("output", output)

            curr += 1
        
        if carry == True:
            output = '1' + output
        
        return output

    def add(self, a, b): # return (add_out, carry)
        if a == '0' and b == '0':
            return ('0', False)
        elif a == '1' and b == '1':
            return ('0', True)
        else:
            return ('1', False)

    def sameLen(self, a, b):
        while len(a) - len(b) != 0:
            if len(a) - len(b) > 0:
                b = '0' + b

            elif len(a) - len(b) < 0:
                a = '0' + a

            else:
                break

        return (a, b)
    
s = Solution()

print(s.addBinary('10', '1'))