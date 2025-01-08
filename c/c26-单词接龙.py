# 127. 单词接龙
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        self.length = len(beginWord)
        wordSet = set(wordList)

        beginQueue = [(beginWord, 1)]
        endQueue = [(endWord, 1)]
        beginVis = {beginWord: 1}
        endVis = {endWord: 1}

        while beginQueue and endQueue:
            if len(beginQueue) > len(endQueue):
                beginQueue, endQueue = endQueue, beginQueue
                beginVis, endVis = endVis, beginVis

            currentWord, currentStep = beginQueue.pop(0)

            for word in wordSet:
                if self.geneChange(currentWord, word):
                    if word in endVis:
                        return currentStep + endVis[word]
                    if word not in beginVis:
                        beginVis[word] = currentStep + 1
                        beginQueue.append((word, currentStep + 1))
        return 0

    def geneChange(self, s1, s2):
        return sum([s1[i] != s2[i] for i in range(self.length)]) == 1


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))
