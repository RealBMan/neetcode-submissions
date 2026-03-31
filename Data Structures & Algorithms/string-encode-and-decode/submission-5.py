class Solution:

    def encode(self, strs: List[str]) -> str:
        sub_char = "@"
        emp_str = ""
        print(strs)
        for word in strs:
            if len(emp_str) == 0:
                emp_str = str(len(word)) + sub_char + word
            else:
                emp_str = emp_str + str(len(word)) + sub_char + word
        return emp_str

    def decode(self, s: str) -> List[str]:
        list_str = []
        sizes = []
        empty = ""
        i = 0
        ptr = 0
        prev = 2
        num = ""

        while i < len(s):
            while s[i] != "@":
                i += 1
            length = int(s[ptr:i])
            position = i + 1
            end_position = length + position
            list_str.append(s[position:end_position])
            i = end_position
            ptr = end_position

        # while i < len(s):
        #     if s[i].isdigit():
        #         ptr = i
        #     if s[i] == "@":
        #         position = i + 1
        #         end_position = int(s[ptr:i]) + position
        #         list_str.append(s[position:end_position])
        #         num = ""
        #     i += 1
        
        return list_str
