import math


def find_min_pages(pages, days):
    if days < len(pages):
        return -1
    lo, hi = 1, max(pages)

    while lo < hi:
        mi = (lo + hi) // 2
        poss_days = sum(int(math.ceil(float(page) / mi)) for page in pages)
        if poss_days == days:
            hi = mi
        elif poss_days < days:
            hi = mi
        else:
            lo = mi + 1

    return lo


assert find_min_pages([5, 3, 4], 4) == 4 

