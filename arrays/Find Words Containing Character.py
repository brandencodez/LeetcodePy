class Solution:
    def findWordsContaining(self, words, x):
        result = []
        for i in range(len(words)):
            if x in words[i]:   # words[i] is the substring in array of words
                result.append(i)
        return result


