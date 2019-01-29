class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def isEven(n):
            return not(n%2)
        low = 0
        high = len(A)-1
        while(low<high):
#             Even first. Odd after
            if (isEven(A[low])):
                low+=1
                continue
            if not(isEven(A[high])):
                high-=1
                continue
            if(isEven(A[high]) and not (isEven(A[low]))):
                A[low], A[high] = A[high], A[low]
        return A
#         This is O(N)
