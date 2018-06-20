

def findMedianSortedArrays(self, nums1, nums2):

    def binary_search(A, B, k):
        m, n = len(A), len(B)
        if m < n: return binary_search(B, A, k)
        if n == 0: return A[k - 1]
        if k == 1: return min(A[0], B[0])

        b_m = min(k >> 1, n)
        a_m = k - b_m
        if A[a_m - 1] < B[b_m - 1]:
            return binary_search(A[a_m:], B, k - a_m)
        elif A[a_m - 1] > B[b_m - 1]:
            return binary_search(A, B[b_m:], k - b_m)
        else:
            return A[a_m - 1]

    t = len(nums1) + len(nums2)
    if t & 1:
        return binary_search(nums1, nums2, (t + 1) >> 1)
    else:
        return (binary_search(nums1, nums2, (t + 1) >> 1) + binary_search(nums1, nums2, ((t + 1) >> 1) + 1)) / 2.0
