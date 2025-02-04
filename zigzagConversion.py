# 6. Zigzag Conversion
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility).
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
"""


# Memory: Beats 100%
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 0:
            return s

        rows = [[] for i in range(0, numRows)]

        row = 0
        reverse = False
        for i in range(0, len(s)):
            rows[row].append(s[i])
            if reverse:
                row -= 1
            else:
                row += 1
            if row == numRows - 1 or row == 0:
                reverse = not reverse

        rowData = ["".join(x) for x in rows]
        ret = "".join(rowData)

        return ret
