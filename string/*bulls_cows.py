# LEETCODE@ 299. Bulls and Cows
#
# --END--


def getHint(self, secret, guess):
    nums = [0] * 10
    bull = cow = 0

    # 1) Brilliant
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bull += 1
        else:
            if nums[int(secret[i])] < 0:
                cow += 1
            if nums[int(guess[i])] > 0:
                cow += 1
            nums[int(secret[i])] += 1
            nums[int(guess[i])] -= 1
    return str(bull) + 'A' + str(cow) + 'B'
