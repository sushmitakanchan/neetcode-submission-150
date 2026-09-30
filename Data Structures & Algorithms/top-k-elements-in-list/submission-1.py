class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        arr = []
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

# SORTING SOLUTION
# Time complexity is O(n log n) because counting and building the array take O(n), but sorting the frequency array takes O(n log n), which dominates. 
# Space complexity is O(n) because the frequency map, frequency array, and result can all grow proportional to n.  



        
