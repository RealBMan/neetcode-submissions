class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indices = []
        final_arr = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if len(indices) == 0:
                indices.append(i)
            else:
                val = indices[-1]
                while len(indices) > 0 and temperatures[i] > temperatures[indices[-1]]:
                    val = indices.pop()
                    final_arr[val] = i - val
                indices.append(i)
        return final_arr