# 321. Create Maximum Number
#
# TLE????
#
# --END--


class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        m, n = len(nums1), len(nums2)
        # dp is defined as current longest string end at here.
        dp1 = [["" for j in range(m + 1)] for i in range(k + 1)]
        # 2) Example:
        #   "" 3, 4, 6, 5
        # 0 "" "" "" "" ""
        # 1 ""
        for i in range(k):
            for j in range(i, m):
                # pre + current char
                s1 = dp1[i][j] + str(nums1[j])
                # we dont need current char
                s2 = dp1[i + 1][j]
                s1_i = 0 if not s1 else int(s1)
                s2_i = 0 if not s2 else int(s2)
                if s1_i < s2_i:
                    dp1[i + 1][j + 1] = s2
                else:
                    dp1[i + 1][j + 1] = s1

        dp2 = [["" for j in range(n + 1)] for i in range(k + 1)]
        for i in range(k):
            for j in range(i, n):
                # pre + current char
                s1 = dp2[i][j] + str(nums2[j])
                # we dont need current char
                s2 = dp2[i + 1][j]
                s1_i = 0 if not s1 else int(s1)
                s2_i = 0 if not s2 else int(s2)
                if s1_i < s2_i:
                    dp2[i + 1][j + 1] = s2
                else:
                    dp2[i + 1][j + 1] = s1

        # 3) match
        res = "0"
        for i in range(k + 1):
            for j in range(k + 1):
                if len(dp1[i][m]) + len(dp2[j][n]) == k:
                    # 4) merge
                    ans = ["0"]
                    s1 = dp1[i][m]
                    s2 = dp2[j][n]
                    print(s1, s2)
                    self.merge(s1, s2, k, 0, 0, "", ans)

                    # 5) cmp
                    if int(res) < int(ans[0]):
                        print(s1, s2)
                        res = ans[0]
        return [int(c) for c in res]

    def merge(self, s1, s2, k, i, j, s, ans):
        if len(s) == k:
            if int(ans[0]) < int(s):
                ans[0] = s
        else:
            if len(s1) <= i:
                self.merge(s1, s2, k, i, j + 1, s + s2[j], ans)
            elif len(s2) <= j:
                self.merge(s1, s2, k, i + 1, j, s + s1[i], ans)
            elif int(s1[i]) < int(s2[j]):
                self.merge(s1, s2, k, i, j + 1, s + s2[j], ans)
            elif int(s2[j]) < int(s1[i]):
                self.merge(s1, s2, k, i + 1, j, s + s1[i], ans)
            else:
                self.merge(s1, s2, k, i + 1, j, s + s1[i], ans)
                self.merge(s1, s2, k, i, j + 1, s + s2[j], ans)


