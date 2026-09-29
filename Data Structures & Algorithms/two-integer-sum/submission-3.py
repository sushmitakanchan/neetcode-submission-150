class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            need = target - nums[i]
            if need in seen:
                return [seen[need], i]
            seen[num] = i
        return []
        