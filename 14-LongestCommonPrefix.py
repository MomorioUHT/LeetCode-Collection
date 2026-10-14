class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return("")
        if len(strs) == 1:
            return(strs[0])

        pref = strs[0]
        plen = len(pref)

        for s in strs[1:]: #check from index 1 to further
            while pref != s[0:plen]:
                pref = pref[0:(plen-1)] #shorten prefix by 1
                plen -= 1
                if plen == 0: #no common prefix
                    return("")

        return(pref)