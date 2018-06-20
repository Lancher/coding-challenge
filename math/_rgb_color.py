# 800. Similar RGB Color
#
# --END--


def similarRGB(self, color):
    # 1) build the symbols for easily finding the macth.
    symbols = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']

    res_val = float('-inf')
    res = ''
    d1, d2, d3 = int(color[1], 16), int(color[3], 16), int(color[5], 16)

    # 2)
    for i in range(max(0, d1 - 2), min(16, d1 + 2)):
        for j in range(max(0, d2 - 2), min(16, d2 + 2)):
            for k in range(max(0, d3 - 2), min(16, d3 + 2)):
                n_color = '#' + symbols[i] + symbols[j] + symbols[k]
                val = self.sim(n_color, color)
                if res_val < val:
                    res_val = val
                    res = n_color
    return res


def sim(self, color1, color2):
    a = - (int(color1[1:3], 16) - int(color2[1:3], 16)) ** 2
    b = - (int(color1[3:5], 16) - int(color2[3:5], 16)) ** 2
    c = - (int(color1[5:7], 16) - int(color2[5:7], 16)) ** 2
    return a + b + c
