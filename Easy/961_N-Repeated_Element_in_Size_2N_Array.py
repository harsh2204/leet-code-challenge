class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        hash_map = {}
        for i in A:
            if i in hash_map:            
                return i
            else:
                hash_map[i] = 0
