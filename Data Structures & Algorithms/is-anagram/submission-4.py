class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        return s==t
        # or better way

        if len(s) != len(t):
            return false
        return sorted(s) == sorted(t)
        # time complexity is O(nlogn)
        """

        """
        # to reduce time complexity to O(n)
        if len(s) != len(t):
            return false

        dict_s: dict[str,int] = {}
        dict_t: dict[str,int] = {}

        for i in s:
            if i in dict_s:
                dict_s[i] +=1
            else:
                dict_s[i] =1
        
        for j in t:
            if j in dict_t:
                dict_t[j] +=1
            else:
                dict_t[j] =1

        return dict_s == dict_t

        # Or better way
        if len(s) != len(t):
            return false

        dict_s: dict[str,int] = {}
        dict_t: dict[str,int] = {}

        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i],0)
            dict_t[t[i]] = 1 + dict_t.get(t[i],0)

        return dict_s == dict_t

        """
        if len(s) != len(t):
            return False

        check: List[int] = [0] * 26

        for i in s:
            check[ord(i) - ord("a")] += 1

        for i in t:
            check[ord(i) - ord("a")] -= 1

        for i in check:
            if i != 0:
                return False
        return True
