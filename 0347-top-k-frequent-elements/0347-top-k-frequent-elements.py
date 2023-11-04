class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most = {}
        res = []
        for i in nums:
            if i in most:
                most[i] += 1
            else:
                most[i] = 1

        most = dict(sorted(most.items(), key=lambda item: item[1], reverse=True))
        print(most)

        for key in most.keys():
            k -= 1
            if k>=0:
                res.append(key)
        return res

        