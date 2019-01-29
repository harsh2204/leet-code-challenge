class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        A = [i[::-1] for i in A]
        for a in A:
            for i, v in enumerate(a):
                a[i] = 1 if v == 0 else 0
        return A
