class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        numbers = []
        
        for i in range(left, right+1):
            j = i
            if i < 10:
                numbers.append(i)
                continue
            else:
                self_div = True
                while j:                
                    if not (j % 10) or (i % (j % 10)):
                        self_div = False
                        break                
                    j //= 10

                if self_div:
                    numbers.append(i)
        return numbers
