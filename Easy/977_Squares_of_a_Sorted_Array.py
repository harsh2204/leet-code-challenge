class Solution:
    
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """        
        x = [(i*i) for i in A]
        return sorted(x)
        #return sorted([(i*i) for i in A])     
        #return [i*i for i in sorted(A, key=abs)]
        #return list(map(lambda x: x*x, sorted(map(abs, A))))
        #return [i*i for i in sorted(map(abs, A))]
