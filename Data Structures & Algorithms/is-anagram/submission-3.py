class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        return s==t
        '''
        
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
        
        '''
        if len(s) != len(t):
            return False
        
        ascii_sum_s = sum(ord(char) for char in s)
        ascii_sum_t = sum(ord(char) for char in t)

        return ascii_sum_s == ascii_sum_t
        '''


        