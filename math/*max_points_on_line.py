# LEETCODE@ 149. Max Points on a Line
#
# --END--


from fractions import gcd


def max_points(points):
    result = 0
    for i in range(len(points)):
        same = 0
        d = {}
        for j in range(i + 1, len(points)):
            if points[i].x == points[j].x and points[i].y == points[j].y:
                same += 1
            elif points[i].x == points[j].x:
                if '1/0' not in d:
                    d['1/0'] = 0
                d['1/0'] += 1
            elif points[i].y == points[j].y:
                if '0/1' not in d:
                    d['0/1'] = 0
                d['0/1'] += 1
            else:
                div = gcd(points[i].y - points[j].y, points[i].x - points[j].x)
                slope = str((points[i].y - points[j].y) / div) + '/' + str((points[i].x - points[j].x) / div)
                if slope not in d:
                    d[slope] = 0
                d[slope] += 1
        max_val = 0
        for val in d.values():
            if val > max_val:
                max_val = val

        result = max(result, max_val + same + 1)
    return result
