class Solution:
    def convert(self, s: str, numRows: int) -> str:
        spaces_count = numRows - 1
        spaces = numRows - 2
        s_index = 0
        row = ""
        while s_index <= len(s) - 1:
            count = 0
            while count != numRows and s_index <= len(s) - 1:
                row += s[s_index]
                s_index += 1
                count += 1
            spaces_c_count = 0
            row += '__SEPARATOR__'
            string_counter = 0
            while spaces_c_count != spaces_count and s_index <= len(s) - 1:
                space_count = 0
                while space_count != spaces and s_index <= len(s) - 1:
                    row += " "
                    space_count += 1
                    string_counter += 1
                    if string_counter == numRows:
                        row += '__SEPARATOR__'
                        string_counter = 0
                spaces_c_count += 1
                if spaces_c_count != spaces_count:
                    row += s[s_index]
                    s_index += 1
                    string_counter += 1
                    if string_counter == numRows:
                        row += '__SEPARATOR__'
                        string_counter = 0
        if row[-13] == '__SEPARATOR__':
            row = row[:-13]
        new_str = ""
        for i in range(numRows):
            for j in row.split('__SEPARATOR__'):
                try:
                    if j[i] != " ":
                        new_str += j[i]
                except IndexError:
                    pass
        return new_str


# PAHNAPLSIIGYIR
if __name__ == '__main__':
    print(Solution().convert("ABCD", 3))
