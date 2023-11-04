class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26 # since constraints says only lowercase a . . . . z
            for c in s:
                count[ord(c)-ord("a")] += 1 # getting ascii values

            res[tuple(count)].append(s)
        return res.values()

