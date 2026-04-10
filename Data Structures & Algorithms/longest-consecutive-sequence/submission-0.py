class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = {}
        sequence = []
        max_length = 0

        for num in nums: 
            if num not in seq: 
                seq[num] = 0

        for key in seq: 
            if key - 1 not in seq:
                counter = 1
                num = key + 1
                while num in seq:
                    counter +=1
                    num += 1
                max_length = max(max_length, counter)
        return max_length
