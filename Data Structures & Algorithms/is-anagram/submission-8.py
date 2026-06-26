class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)
        if lenS != lenT:
            return False
        minLength = min(lenS, lenT)
        arr = [0] * 26 
        for i in range(minLength):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1

        for i in range(len(arr)):
            if(arr[i] != 0): 
                return False
        return True