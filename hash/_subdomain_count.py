# LEETCODE@ 811. Subdomain Visit Count
#
# --END--


def subdomainVisits(self, cpdomains):
    d = {}
    for domain in cpdomains:
        cnt, w_d = domain.split(' ')
        cnt = int(cnt)

        sub_d = w_d.split('.')
        for i in range(len(sub_d)):
            m_d = '.'.join(sub_d[i:])
            if m_d in d:
                d[m_d] += cnt
            else:
                d[m_d] = cnt
    res = []
    for k, v in d.items():
        res.append('{} {}'.format(v, k))
    return res
