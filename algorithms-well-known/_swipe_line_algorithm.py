# 1. use BST, to find the intersection.
#
# 2. Example:
#
#             (4, 6)
#               |
#     -------------------
#   (1, 5)      |       (6, 5)
#               |
#          ------------------------
#       (3, 3)  |                (8, 3)
#               |
#             (4, 1)
#
#   In the BST, we store the Y value!!!!
#
#   1) Encounter (1, 2), push Y point 5 to BST.
#   2) Encounter (3, 3), push Y point 3 to BST.
#   3) Encounter vertical line, do the `rank(6 + 1) - rank(1 + 1)` to get
#      number of intersections.
#   4) Encounter (6, 5), delete Y 5 from BST.
#   5) Encounter (8, 3), delete Y 3 from BST.
#
# --END--


