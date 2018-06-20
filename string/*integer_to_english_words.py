# LEETCODE@ 273. Integer to English Words
#
# --END--


def numberToWords(self, num):
    if num == 0:
        return 'Zero'

    ans = ''
    one_nineteen = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ', 'Ten ',
                    'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ',
                    'Nineteen ']
    ten_ninety = ['', 'Ten ', 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']
    commas = ['Billion ', 'Million ', 'Thousand ', '']

    while num:
        if num % 1000:
            ans = commas[-1] + ans
            digit12 = num % 1000 % 100
            digit3 = num % 1000 / 100
            if digit12 < 20:
                ans = one_nineteen[digit12] + ans
            else:
                ans = ten_ninety[digit12 / 10] + one_nineteen[digit12 % 10] + ans
            if digit3:
                ans = one_nineteen[digit3] + 'Hundred ' + ans
        commas.pop()
        num /= 1000

    return ans.strip()