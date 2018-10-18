

def length_of_longest_substr_no_dup(s):
    # init
    n = len(s)
    char_cnt = [0] * 26
    res = 0

    # check if all chars are less than 1
    def check_unique_char():
        for i in range(26):
            if char_cnt[i] > 1:
                return False
        return True

    # iterate through the string
    st = 0
    for ed in range(n):
        char_cnt[ord(s[ed])-ord('a')] += 1

        # if our window contain not unique character, move st forward
        while not check_unique_char():
            char_cnt[ord(s[st])-ord('a')] -= 1
            st += 1

        # update res
        res = max(res, ed - st + 1)

    # return answer
    return res


print(length_of_longest_substr_no_dup(""))

