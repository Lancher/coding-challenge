# LEETCODE@ 789. Escape The Ghosts
#
# 1. How to intercept ?
#
#    Me ------------------------> Goal
#                    /
#                   /
#           Ghost---
#
#    If dst(Ghost, Goal) < dst(Me, Goal)
#
#
# --END--


def escapeGhosts(ghosts, target):
    steps = abs(target[0]) + abs(target[1])

    for g in ghosts:
        g_steps = abs(g[0] - target[0]) + abs(g[1] - target[1])
        if g_steps <= steps:
            return False
    return True
