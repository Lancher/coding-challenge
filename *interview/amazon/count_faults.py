import collections


def count_faults(logs):
    res = 0

    svr_fault = collections.defaultdict(int)

    for log in logs:
        svr, status = log.split(' ')
        if status == 'success':
            svr_fault[svr] = 0
        else:
            svr_fault[svr] += 1
        
        if svr_fault[svr] == 3:
            res += 1
            svr_fault[svr] = 0

    return res


assert count_faults(["s1 error", "s1 error", "s2 error", "s1 error", "s1 error", "s2 success"]) == 1
