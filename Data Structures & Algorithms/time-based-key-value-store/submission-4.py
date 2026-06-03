class TimeMap:

    def __init__(self):
        self.dict_val = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
            if key in self.dict_val:
                self.dict_val[key].append((timestamp,value))
            else:
                self.dict_val[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
            if key not in self.dict_val:
                return ""
            if len(self.dict_val[key]) == 0:
                return ""
            else:
                l = 0
                r = len(self.dict_val[key]) - 1
                ans = ""
                
                while l <= r:
                    mid = (l + r + 1) // 2
                    if self.dict_val[key][mid][0] > timestamp:
                        r = mid - 1
                    else:
                        ans = self.dict_val[key][mid][1]
                        l = mid + 1
                return ans

        
