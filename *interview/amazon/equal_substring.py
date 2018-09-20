

def equal_substring1(s, k):
    # initialization
    n = len(s)
    i, j = 0, 0
    cnt = [0] * 26

    # max length
    res = 0

    # count distinct characters
    def count_distinct():
        total = 0
        for num in cnt:
            if num:
                total += 1
        return total

    #
    for i in range(n):
        # j goes to right as much as possible
        while j < n:
            distinct_cnt = count_distinct()
            if distinct_cnt == k:
                if cnt[ord(s[j])-ord('a')]:
                    cnt[ord(s[j]) - ord('a')] += 1
                    j += 1
                else:
                    break
            elif distinct_cnt < k:
                cnt[ord(s[j]) - ord('a')] += 1
                j += 1

        # update max length
        res += j - i

        # decrease cnt if possible
        cnt[ord(s[i]) - ord('a')] -= 1

    return res


print(equal_substring1('abcbcs', 2) - equal_substring1('abcbcs', 1))

