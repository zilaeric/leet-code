class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        acc = '' # roman numeral accumulator
        rest = num # unprocessed part of integer
        
        for i in range(len(vals)):
            acc += symbols[i] * (rest // vals[i]) # add symbol necessary amount of times
            rest = rest % vals[i] # update unprocessed part of integer
            
        return acc

