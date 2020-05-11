# 1. one slow node and one fast node
#
# 2. get the beginning of circle: set the slow node to head and run in the same speed
#
# 3. Example:
#
#
#                              ---------------------------|
#                              |
#                        x =>  |  [ 8 ] <-- [ 7 ] <-- [ 6 ]  -
#                              |    |                   ^    |
#                              |    |                   |    |
#                              -    v                   |    |
#   [ 0 ] --> [ 1 ] --> [ 2 ] --> [ 3 ] --> [ 4 ] --> [ 5 ]  |  <= y
#                                                            |
#                                                            |
#   |---------------------------------||----------------------
#                   x
#
#   slow will walk (x + y)
#   fast will walk (x + y) + (x + y)
#
#
# --END--


def cycle_detection(g):
    slow, fast = g[0], g[g[0]]

    # find cycle
    while slow != fast:
        slow = g[slow]
        fast = g[g[fast]]
    print('meet at {}'.format(slow))

    # find the beginning of cycle
    slow = 0
    while slow != fast:
        slow = g[slow]
        fast = g[fast]
    print('circle at {}'.format(slow))

    # circle length
    n = 1
    fast = g[fast]
    while slow != fast:
        fast = g[fast]
        n += 1

    print('circle length {}'.format(n))


g = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 6,
    6: 7,
    7: 8,
    8: 3,
}

cycle_detection(g)
