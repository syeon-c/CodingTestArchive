def compareWord(word_a, word_b):
    count = 0
    for i in range(len(word_a)):
        if word_a[i] != word_b[i]:
            count += 1

    if count == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    answer = 0
    visited = [0 for _ in range(len(words))]
    stack = [begin]

    if target not in words:
        return 0
    else:
        while stack:
            temp = stack.pop()
            if temp == target:
                break

            else:
                for i in range(len(words)):
                    if compareWord(temp, words[i]) and visited[i] == 0:
                        stack.append(words[i])
                        visited[i] = 1
            answer += 1

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
