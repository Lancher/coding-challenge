# LEETCODE@ 71. Simplify Path
#
# --END--


def simplifyPath(self, path):
    stack = []
    path = path.strip('/').split('/')

    for p in path:
        if p == '.':
            continue
        elif p == '..':
            if stack:
                stack.pop()
        else:
            # p might be empty
            if p:
                stack.append(p)
    return '/' + '/'.join(stack)
