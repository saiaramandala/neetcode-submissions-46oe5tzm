class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counter = [[] * i for i in range(len(nums))]

        for i in range(len(nums)):
            counter[i].append(math.prod(nums[:i] + nums[i + 1:]))

        res = [ lis.pop(0) for lis in counter] 
        return res   









        
        