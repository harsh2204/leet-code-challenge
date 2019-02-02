class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        for i in bin(x^y):
            if i == '1':
                ans += 1
        return ans
