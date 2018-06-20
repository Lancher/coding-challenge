# LEETCODE@ 68. Text Justification
#
# --END--


def fullJustify(self, words, maxWidth):
    res = []

    cnt = 0
    row = []
    for word in words:
        # 1) previous words + current word + blanks
        if cnt + len(word) + len(row) > maxWidth:
            for i in range(maxWidth - cnt):
                row[i % (len(row) - 1 or 1)] += ' '
            res.append(''.join(row))
            cnt = len(word)
            row = [word]
        else:
            cnt += len(word)
            row.append(word)

    # 2) last line
    line = ' '.join(row)
    res.append(line + ' ' * (maxWidth - len(line)))
    return res
