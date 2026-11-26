class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_=''.join(c.lower() for c in s if c.isalnum())
        length = len(s_)
        if length > 0:

            l = 0
            r = length - 1
            mid = int(length/2 - 1)
            while l < mid or s_[l] != s_[r]:
                # print(f"l: {s_[l]} r: {s_[r]}")
                print(l)
                if s_[l] == s_[r]:
                    l+=1
                    r-=1
                else:
                    return False

            # while()
            return True
        return True