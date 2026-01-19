# time:  O(n)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest = 0
        for candy in candies:
            if candy >= largest:
                largest = candy
        
        result = []
        for candy in candies:
            if candy + extraCandies >= largest:
                result.append(True)
            else:
                result.append(False)

        return result