from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            countS = [0]*26
            for w in word:
                countS[ord(w)-ord("a")]+=1        
            res[tuple(countS)].append(word)

        return list(res.values())
        