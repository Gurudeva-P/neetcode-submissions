class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            group={}
            for wr in strs:
                count=[0]*26
                for ch in wr:
                    pos=ord(ch)-ord("a")
                    count[pos]+=1
                key=tuple(count)
                if key not in group:
                    group[key]=[]
                group[key].append(wr)
            return list(group.values())


            
        