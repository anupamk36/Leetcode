class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        k = nums[0]
        for i in range(len(nums)-1):
            if nums[i] > k:
                k = nums[i]
            k = k -1
            if k<0:
                return False
        return True