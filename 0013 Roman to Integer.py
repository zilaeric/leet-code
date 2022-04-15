class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {'I' : 1,
                   'V' : 5,
                   'X' : 10,
                   'L' : 50,
                   'C' : 100,
                   'D' : 500,
                   'M' : 1000} # symbols dictionary
        
        acc = 0 # total value accumulator
        last = 1000 # last symbol value
        
        for i in range(len(s)):
            cur = symbols[s[i]] # current symbol value
            acc += cur # add current symbol value to accumulator
            
            if last < cur:
                acc -= 2 * last # rectify subtraction instances
                
            last = cur # update last symbol value
            
        return acc

