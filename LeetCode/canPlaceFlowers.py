# time: O(n)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # edge cases
        if len(flowerbed) == 1 and n <= 1:
            if flowerbed[0] == 0:
                return True
        elif len(flowerbed) == 2 and flowerbed[0] == 0 and flowerbed[1] == 0 and n == 1:
            return True
        elif len(flowerbed) == 2 and flowerbed[0] == 0 and flowerbed[1] == 0 and n < 1:
            return False

        for i in range(len(flowerbed)):
            if n == 0:
                break
            f0 = flowerbed[i]
            f1 = -1
            f2 = -1
            f0Index = i
            f1Index = i + 1
            f2Index = i + 2

            if f1Index <= len(flowerbed) - 1:
                f1 = flowerbed[f1Index]

            if f2Index <= len(flowerbed) - 1:
                f2 = flowerbed[f2Index]

            # [100]
            #    ^
            if f0 == 1 and f1 == 0 and f2 == 0:
                if f2Index + 1 <= len(flowerbed) - 1:
                    if flowerbed[f2Index + 1] == 0:
                        flowerbed[f2Index] = 1
                        n -= 1
                else:
                    flowerbed[f2Index] = 1
                    n-= 1
            
            # [001]
            #  ^
            if f0 == 0 and f1 == 0 and f2 == 1:
                if f0Index - 1 >= 0:
                    if flowerbed[f0Index - 1] == 0:
                        flowerbed[f0Index] = 1
                        n -= 1
                else:
                    flowerbed[f0Index] = 1
                    n-= 1
        
            # [000]
            #  ^ ^
            #   ^
            failA = False
            failB = False
            if f0 == 0 and f1 == 0 and f2 == 0:
                if f0Index - 1 >= 0:
                    if flowerbed[f0Index - 1] == 0:
                        flowerbed[f0Index] = 1
                        n -= 1
                    else:
                        failA = True
                else:
                    flowerbed[f0Index] = 1
                    n-= 1

                if f2Index + 1 <= len(flowerbed) - 1:
                    if flowerbed[f2Index + 1] == 0:
                        flowerbed[f2Index] = 1
                        n -= 1
                    else:
                        failB = True
                else:
                    flowerbed[f2Index] = 1
                    n-= 1

                if failA and failB:
                    flowerbed[f1Index] = 1
                    n -= 1

        return n <= 0
    
sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1,0,0], 2))