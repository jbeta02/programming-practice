# LeetCode 67. improved version of previous addBinary attempt since I don't force the len of a and b to be the same which saves this solution from having to iterate over the longest string an additional time
# time: O(n) where n is len of longest str
# space: O(n)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        output = ''
        sizeA = len(a) - 1
        sizeB = len(b) - 1
        while sizeA >= 0 or sizeB >= 0 or carry:
            aNum = '0'
            bNum = '0'
            if sizeA >= 0:
                aNum = a[sizeA]
            if sizeB >= 0:
                bNum = b[sizeB]
            
            out, currCarry = self.add(aNum, bNum)
            nextCarry = False

            if carry == True:
                out, nextCarry = self.add(out, '1')
            
            carry = currCarry or nextCarry

            output = out + output

            # print("---")
            # print("out", out)
            # print("output", output)

            sizeA -= 1
            sizeB -= 1
        
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