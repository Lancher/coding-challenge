# LEETCODE@ 301. Remove Invalid Parentheses
#
# 1) BFS
#
# 2) DFS
#
# --END--


def removeInvalidParentheses(self, s):
    res = []
    q = [s]
    visited = set()

    # 1) valid parentheses
    def is_valid(pat):
        cnt = 0
        for c in pat:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0

    # 2) run BFS to check all the possibilities
    while not res:
        next_q = []

        for pat in q:
            if pat in visited:
                continue
            visited.add(pat)
            if is_valid(pat):
                res.append(pat)
            else:
                # check if res is empty
                if not res:
                    for i in range(len(pat)):
                        if pat[i] == '(' or pat[i] == ')':
                            n_pat = pat[:i] + pat[i + 1:]
                            next_q.append(n_pat)
        q = next_q

    return res
