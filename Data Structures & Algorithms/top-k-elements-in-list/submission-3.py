class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for x in nums: #
            seen[x] = seen.get(x, 0) + 1
        
        freq = [[] for i in range(len(nums)+1)]

        for key, val in seen.items():
            freq[val].append(key)
        result = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

             