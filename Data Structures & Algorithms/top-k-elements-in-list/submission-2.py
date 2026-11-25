from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        print(counter)
        sorted_value = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
        print (sorted_value)
        k_items = []
        first_n_2d = [list(item) for item in list(sorted_value.items())[:k]]
        print(first_n_2d)
        for i in range(k):
            k_items.append(first_n_2d[i][0])
        print (k_items)
        return k_items