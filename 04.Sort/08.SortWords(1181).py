import sys

n = int(sys.stdin.readline())
wordsList = []

for _ in range(n):
    word = str(sys.stdin.readline())
    wordLen = len(word)
    wordsList.append((word, wordLen))

wordsList = list(set(wordsList))

wordsList.sort(key=lambda word: (word[1], word[0]))

for word in wordsList:
    print(word[0], end="")
