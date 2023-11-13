class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        dic = collections.defaultdict(list)
        res = []
        for employee, access_time in access_times:
            dic[employee].append(int(access_time[:2]) * 60 + int(access_time[2:]))
        for employee, time in dic.items():
            time.sort()
            for i in range(len(time) - 2):
                if time[i + 2] - time[i] <= 59:
                    res.append(employee)
                    break
        return res
