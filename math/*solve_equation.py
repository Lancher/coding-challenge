# LEETCODE@ 640. Solve the Equation
#
# --END--


import re


class Solution:
    def solveEquation(self, equation):
        # regex pattern!!!
        pattern = '(=)|([+-]?)(\d*)(x?)'

        x, a = 0, 0
        side = 1
        for eq, sign, num, is_x in re.findall(pattern, equation):
            print(eq, sign, num, is_x)
            if eq:
                side = -1
            elif is_x:
                # num might be '', we should give it 1
                x += side * int(sign + (num or '1'))
            elif num:
                a -= side * int(sign + num)

        # return solutions
        if x:
            return 'x={}'.format(int(a / x))
        elif a:
            return 'No solution'
        else:
            return 'Infinite solutions'

