class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
# Sorting Approach: First we'll check if the length of both strings are equal, if not return false. Then compare the sorted strings to check if they are identical.
# Time: O(n log n + m log m) — sorted() sorts both strings, taking O(n log n) and O(m log m) respectively.
# Space: O(n + m) — Python's sorted() creates new lists containing the characters of both strings.
  
