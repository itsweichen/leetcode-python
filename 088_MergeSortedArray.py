class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        # 5/27/2016
        # 60 ms [12%]

        i = m + n
        p = m - 1
        q = n - 1

        while i > 0:
            i -= 1
            if p < 0 and q > -1:
                nums1[i] = nums2[q]
                q -= 1
                continue
            if q < 0 and p > -1:
                nums1[i] = nums1[p]
                p -= 1
                continue

            np, nq = nums1[p], nums2[q]
            if np > nq:
                nums1[i] = np
                p -= 1
            else:
                nums1[i] = nq
                q -= 1
