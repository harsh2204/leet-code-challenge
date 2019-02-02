class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count = 0
        
        for items in zip(*A):  # The * operator can be used in conjuncton with zip() to unzip the list.
            if sorted(items) != list(items):
                count += 1
                
        return count
