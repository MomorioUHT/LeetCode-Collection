class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            if len(ch) == len(word):
                return word
            else:
                for x in range(0,len(word)):
                    if word[x] == ch:
                        res = word.replace(word[0:x+1], word[0:x+1][::-1])
                        return res
        else:
            return word