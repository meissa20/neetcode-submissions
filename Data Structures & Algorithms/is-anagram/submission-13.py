class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        freqt = {}
        for chara in s:
            freqs[chara] = freqs.get(chara, 0) + 1
        for chara in t:
            freqt[chara] = freqt.get(chara, 0) + 1
        print(freqt)
        if freqt == freqs:
            return True
        return False

s="jar"
t="jam"
solution = Solution()
solution.isAnagram(s, t)