class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return strs
        
        seen = {}

        for x in strs:
            sortedVal = str(sorted(x))
            if sortedVal not in seen:
                seen[sortedVal] = [x]
            else:
                seen[sortedVal].append(x)
        return [value for value in seen.values()]
            