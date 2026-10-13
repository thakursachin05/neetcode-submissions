class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        words = set(wordList)
        queue = deque([[beginWord, 1]])

        while queue:
            print(queue)
            word, level = queue.popleft()
            if word == endWord:
                return level

            for i in range(len(word)):
                for j in range(26):
                    newWord = word[:i] + chr(ord('a') + j) + word[i+1:]
                    if newWord in words:
                        queue.append([newWord, level+1])
                        words.remove(newWord)
        
        return 0
        