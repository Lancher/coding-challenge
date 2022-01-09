"""
1. Reservior Sampling

2. Choose 2 number from 0 ~ n - 1

     bucket = [0, 1]

   Now, when it comes to 2, it has 2/3 probability
   to replace into the bucket

 3. Leetcode. 382

-- END --
"""

import random


def sample(n, k):
    bucket = [num for num in range(k)]

    for num in range(k, n):
        rnd = random.randrange(0, num + 1)
        if rnd < k:
            bucket[rnd] = num

    return bucket


print(sample(10, 3))
