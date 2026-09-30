class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1
            countT[t[i]] = countT.get(t[i],0) + 1
        
        return countS == countT

# Time: O(n + m) — we scan s and t once.
# Space: O(1) — there can be at most 26 different characters, so the hash maps never grow with input size.

        