# LEETCODE@ 621. Task Scheduler
#
# 1. Example:
#
#   AAAABBBEEFFGG 3
#   Frame: "AXXXAXXXAXXXA"
#   insert 'B': "ABXXABXXABXXA" <--- 'B' has higher frequency than the other characters, insert it first.
#   insert 'E': "ABEXABEXABXXA"
#   insert 'F': "ABEFABEXABFXA" <--- each time try to fill the k-1 gaps as full or evenly as possible.
#   insert 'G': "ABEFABEGABFGA"
#
#   AACCCBEEE 2
#   3 identical chunks "CE", "CE CE CE" <-- this is a frame
#   insert 'A' among the gaps of chunks since it has higher frequency than 'B' ---> "CEACEACE"
#   insert 'B' ---> "CEABCEACE" <----- result is tasks.length;
#
# --END--


def leastInterval(self, tasks, n):
    # find chars
    chars = [0] * 26
    for t in tasks:
        chars[ord(t ) -ord('A')] += 1

    # find the max frequency chars
    mx = float('-inf')
    for i in range(26):
        if mx < chars[i]:
            mx = chars[i]

    # find number of the same frequency as mx
    mx_same_n = 0
    for i in range(26):
        if chars[i] == mx:
            mx_same_n += 1

    # we dont have to care the last section, so it will be mx - 1.
    # the mx_same_n is the number of last section
    return max(sum(chars), (mx - 1) * (n + 1) + mx_same_n)