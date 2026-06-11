class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = len(s);
        b = len(t);
        if a != b:
            return False;
        cnt1 = [0] * 26;
        cnt2 = [0] * 26
        for i in range(a):
            cnt1[ord(s[i]) - 97] += 1;
            cnt2[ord(t[i]) - 97] += 1;
        x = len(cnt1)
        for i in range(x):
            if cnt1[i] != cnt2[i]:
                return False;
        return True;