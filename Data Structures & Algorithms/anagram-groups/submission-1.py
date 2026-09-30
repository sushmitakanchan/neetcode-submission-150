class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

# SORTING Approach: We will create a hash map with sorted String as key and appending it's original string to its corresponding key and return the list of its values
# m = number of strings, n = length of each string.
# Time: O(m × n log n) → sorting each of the m strings takes O(n log n).
# Space: O(m × n) → we store m strings, each with up to n characters.