class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def binSearch(A, left, right):
            if left<=right:
                mid = int((left+right)/2)
                if (A[mid-1]<A[mid] and A[mid]>A[mid+1]):
                    return mid
                if (A[mid] < A[mid+1]):
                    return binSearch(A, mid+1,right); 
                else:
                    return binSearch(A, left, mid-1); 
            return -1
        return binSearch(A, 1, len(A)-2)
        
    
