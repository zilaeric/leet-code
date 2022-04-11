class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid) # number of rows
        n = len(grid[0]) # number of columns
        
        grid_tp = self.transpose(grid) # transpose original matrix
        
        row_shifts = [k // n] * n # common number of shifts per column
        for i in [j + 1 for j in range(k % n)]:
            row_shifts[-i] += 1 # add shifts in last columns
        
        grid_tp_alt = [self.shiftList(grid_tp[i], row_shifts[i], m) for i in range(n)] # shifts in columns
        grid_shift = self.shiftList(grid_tp_alt, k % n, n) # shifts in matrix
        
        grid_final = self.transpose(grid_shift) # transpose matrix back to original form
        
        return grid_final
    
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(map(list, zip(*matrix)))
    
    def shiftList(self, l, shift, bound):
        """
        :type l: List[]
        :type shift: int
        :type bound: int
        :rtype: List[]
        """
        order_init = range(bound) # initial order
        order_shift = [(i - shift) % bound for i in order_init] # shifted order
        
        return [l[i] for i in order_shift]

