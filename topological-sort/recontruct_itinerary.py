

# LEETCOD@ 332. Reconstruct Itinerary
#
# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the
# itinerary in order.
def findItinerary(self, tickets):
    res = []
    d = {}
    for s, e in sorted(tickets)[::-1]:
        if s not in d:
            d[s] = [e]
        else:
            d[s].append(e)

    def dfs(cur):
        while cur in d and d[cur]:
            dfs(d[cur].pop())
        res.append(cur)

    dfs('JFK')
    return res[::-1]
