class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = (nums)
        return [x for x in range(min(nums) + 1, max(nums)) if x not in s]
        