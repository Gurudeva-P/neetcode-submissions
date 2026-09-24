class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s={}
        freq_t={}
        for i in range(len(s)):
            if s[i] in freq_s:
                freq_s[s[i]]+=1
            else:
                freq_s[s[i]]=1
        for j in range(len(t)):
            if t[j] in freq_t:
                freq_t[t[j]]+=1
            else:
                freq_t[t[j]]=1      
        if freq_s==freq_t:
            return True
        else : 
            return False