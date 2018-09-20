# LEETCODE@ 722. Remove Comments
#
# --END--


def removeComments(self, source):
    res, buffer, block_comment_open = [], '', False
    for line in source:
        i = 0
        while i < len(line):
            char = line[i]

            # "//" -> Line comment.
            if char == '/' and (i + 1) < len(line) and line[i + 1] == '/' and not block_comment_open:
                i = len(line)  # Advance pointer to end of current line.

            # "/*" -> Start of block comment.
            elif char == '/' and (i + 1) < len(line) and line[i + 1] == '*' and not block_comment_open:
                block_comment_open = True
                i += 1

            # "*/" -> End of block comment.
            elif char == '*' and (i + 1) < len(line) and line[i + 1] == '/' and block_comment_open:
                block_comment_open = False
                i += 1

            # Normal character. Append to buffer if not in block comment.
            elif not block_comment_open:
                buffer += char
            i += 1
        if buffer and not block_comment_open:
            res.append(buffer)
            buffer = ''
    return res
