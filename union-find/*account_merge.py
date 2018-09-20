# LEETCODE@ 721. Accounts Merge


class Union:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def root(self, p):
        while p != self.parent[p]:
            # path compression
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        # smaller tree to bigger tree
        root_p, root_q = self.root(p), self.root(q)
        if root_p != root_q:
            if self.size[root_p] < self.size[root_q]:
                self.parent[root_p] = root_q
                self.size[root_q] += self.size[root_p]
            else:
                self.parent[root_q] = root_p
                self.size[root_p] += self.size[root_q]


class Solution:
    def accountsMerge(self, accounts):
        n = 0
        email_idx = {}
        idx_name = {}

        # build mapping
        for name, *emails in accounts:
            for email in emails:
                if email not in email_idx:
                    email_idx[email] = n
                    idx_name[n] = name
                    n += 1

        # union find
        un = Union(n)
        for name, *emails in accounts:
            for i in range(len(emails) - 1):
                un.union(email_idx[emails[i]], email_idx[emails[i + 1]])

        # root with list of emails
        root_emails = {}
        for name, *emails in accounts:
            for email in emails:
                root = un.root(email_idx[email])
                if root not in root_emails:
                    root_emails[root] = set()
                root_emails[root].add(email)

        # concatenate answer
        res = []
        for root, emails in root_emails.items():
            res.append([idx_name[root]] + sorted(list(emails)))
        return res

