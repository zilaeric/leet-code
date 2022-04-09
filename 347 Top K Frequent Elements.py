class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        low = min(nums) # array minimum
        high = max(nums) # array maximum
        
        bins = [0] * (high - low + 1) # prepare integer count bins
        
        for i in nums:
            bins[i-low] += 1 # count integers
            
        sort = sorted(range(len(bins)), key=lambda x: bins[x])[-k:] # get k largest indices
        ret = [num + low for num in sort] # transform indices to original values
            
        return ret

