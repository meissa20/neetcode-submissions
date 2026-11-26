from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        # print(c)
        c_list = list(c.most_common())
        # print(c_list)
        x=[]
        l = len(c_list)
        # print(f"l: {l}, k: {k}")
        for i in range(0,k):
            # print(c_list[i])
            x.append(c_list[i][0])
        # print(x)
        return x
