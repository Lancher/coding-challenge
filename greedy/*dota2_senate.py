# LEETCODE@ 649. Dota2 Senate
#
# --END--


import queue


def predictPartyVictory(self, senate):
    # DDRRR
    # 1st Round: DDXRR
    # 2nd Round: DDXXR
    # 3rd Round: DXXXR
    # 4th Round: DXXXX
    # Dire wins.
    n = len(senate)
    qr, qd = queue.Queue(), queue.Queue()
    for i in range(n):
        if senate[i] == 'R':
            qr.put(i)
        else:
            qd.put(i)

    # increment the index as next round
    while not qr.empty() and not qd.empty():
        ri, di = qr.get(), qd.get()
        if ri < di:
            qr.put(ri + n)
        else:
            qd.put(di + n)

    return 'Radiant' if qd.empty() else 'Dire'
