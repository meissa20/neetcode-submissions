class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for stri in strs:
            stri_sorted = "".join(sorted(stri))
            if stri_sorted in strs_dict:
                strs_dict[stri_sorted].append(stri)
            else:
                strs_dict[stri_sorted]=[stri]
        return list(strs_dict.values())