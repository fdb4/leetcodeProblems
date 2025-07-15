class Solution(object):
    def isValid(self, word):
        if(len(word) < 3):
            return False
        vow=False
        cons=False
        for l in word:
            if l.isalnum():
                if l.isdigit():
                    continue
                if l.lower() in "aeiou":
                    vow=True
                else:
                    cons=True
            else:
                return False
                

        return vow and cons
        """
        :type word: str
        :rtype: bool
        """
        
