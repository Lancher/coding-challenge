# LEETCODE@ 165. Compare Version Numbers
#
# --END--


def compareVersion(self, version1, version2):
    version1 = version1.split('.')
    version2 = version2.split('.')

    i = j = 0
    while i < len(version1) or j < len(version2):
        v1 = v2 = 0
        if i < len(version1):
            v1 = int(version1[i])
        if j < len(version2):
            v2 = int(version2[i])
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        i, j = i + 1, j + 1
    return 0
