class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for x in strs:
            default = str(sorted(x))
            if default in ana:
                ana[default].append(x)
            else:
                ana[default] = [x]
        return list(ana.values())