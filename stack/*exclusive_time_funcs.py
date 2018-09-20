# LEETCODE@ 636. Exclusive Time of Functions
#
# --END--


def exclusiveTime(self, n, logs):
    #  0   1   2   3   4   5   6
    #  |---|---|---|---|---|---|---|
    res = [0] * n

    # walk through the logs
    stack = []
    for log in logs:
        fid, op, t = log.split(':')
        fid = int(fid)
        t = int(t) if op == 'start' else int(t) + 1

        # If the stack is empty, this is the first job.
        if op == 'start':
            if not stack:
                stack.append([fid, t])
            else:
                res[stack[-1][0]] += t - stack[-1][1]
                stack.append([fid, t])
        else:
            res[stack[-1][0]] += t - stack[-1][1]
            stack.pop()
            # update previous task staring time
            if stack:
                stack[-1][1] = t
    return res
