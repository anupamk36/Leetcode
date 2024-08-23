class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        res = ""
        for i in range(length):
            res += word1[i] + word2[i]
        res += word1[length:] + word2[length:]
        return res
        