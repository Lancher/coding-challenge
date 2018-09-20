# LEETCODE@ 635. Design Log Storage System
#
# --END--


class LogSystem:
    def __init__(self):
        self.logs = []

    def put(self, tid, timestamp):
        self.logs.append((tid, timestamp))

    def retrieve(self, s, e, gra):
        index = {'Year': 5, 'Month': 8, 'Day': 11,
                 'Hour': 14, 'Minute': 17, 'Second': 20}[gra]
        start = s[:index]
        end = e[:index]

        # truncate the timestamp[:index] to remove redundant infos
        return sorted(tid for tid, timestamp in self.logs
                      if start <= timestamp[:index] <= end)
