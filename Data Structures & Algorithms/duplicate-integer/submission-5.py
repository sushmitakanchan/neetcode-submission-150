class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
    
# Time: O(n) — creating set(nums) requires going through all n elements.
# Space: O(n) — the set can store up to n unique elements.