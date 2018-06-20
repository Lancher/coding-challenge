# 135. Candy
#
# 1) DP depends on the left and right elements.
#
# --END--


def candy(self, ratings):
    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
        if ratings[i - 1] < ratings[i]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i + 1] < ratings[i] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1

    return sum(candies)
