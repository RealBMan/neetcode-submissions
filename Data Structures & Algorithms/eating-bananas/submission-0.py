import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1

        while left < right:
            middle = (left + right) // 2
            total_sum = 0
            for i in range(len(piles)):
                total_sum += math.ceil(piles[i] / middle) 
            if total_sum <= h:
                right = middle
            else:
                left = middle + 1    
        return left          