class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 0
        while left < len(nums) - 1:
            right = left + 1
            while right < len(nums):
                if nums[left] == nums[right]:
                    return nums[right]
                right += 1
            left += 1
        

        