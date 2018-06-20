# How to construct graph ?


# 1. Directed Graph
#
#   0 --> 1 --> 3
#   |
#   --> 2
#
# --END--
g = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []  # node 2 & 3 should also be add to the graph
}


# 2. Directed Graph with Weights
#      5     7
#   0 --> 1 --> 3
# 9 |
#   --> 2
#
# --END--
g = {
    0: {1: 5, 2: 9},
    1: {3: 7},
    2: {},
    3: {}
}

# 3. Undirected Graph
#
#   0 --- 1 --- 3
#   |
#   --- 2
#
# --END--
g = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}


# 4. Undirected Graph with Weight
#
#      5     7
#   0 --- 1 --- 3
# 9 |
#   ---- 2
#
#
# --END--
g = {
    0: {1: 5, 2: 9},
    1: {0: 5, 3: 7},
    2: {0: 0},
    3: {1: 7}
}


# 5. Linked List
#
#
#                              |  [ 8 ] <-- [ 7 ] <-- [ 6 ]
#                              |    |                   ^
#                              |    |                   |
#                              -    v                   |
#   [ 0 ] --> [ 1 ] --> [ 2 ] --> [ 3 ] --> [ 4 ] --> [ 5 ]
#
#
# --END--
g = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    5: 6,
    6: 7,
    7: 8,
    8: 3,
}