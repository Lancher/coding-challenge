# LEETCODE@ 609. Find Duplicate File in System
#
# --END--


def findDuplicate(self, paths):
    d = {}
    for path in paths:
        directory, *files = path.split(' ')
        for f in files:
            f_name, f_cont = f.split('(')
            if f_cont not in d:
                d[f_cont] = []
            d[f_cont].append(directory + '/' + f_name)

    # only find duplicate groups
    res = [v for v in d.values() if len(v) > 1]
    return res
