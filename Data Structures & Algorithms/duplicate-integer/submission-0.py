class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_set = set(nums)
        if len(check_set) == len(nums):
            return False
        else:
            return True
        