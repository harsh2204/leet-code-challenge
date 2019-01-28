class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lst = [".-","-...","-.-.","-..",".","..-.","--.","....",
               "..",".---","-.-",".-..","--","-.","---",".--.",
               "--.-",".-.","...","-","..-","...-",".--","-..-",
               "-.--","--.."]        

        return len(set([''.join([lst[ord(letter)-97]for letter in word]) for word in words]))
