class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        rec = [] # record
        
        for i in ops:
            if i == "C":
                rec.pop() #
            elif i == "D":
                rec.append(2 * rec[-1])
            elif i == "+":
                rec.append(rec[-1] + rec[-2])
            else:
                rec.append(int(i))
                
        return sum(rec)

