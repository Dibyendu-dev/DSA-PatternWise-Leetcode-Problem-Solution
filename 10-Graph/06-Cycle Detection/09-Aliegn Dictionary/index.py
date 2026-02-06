from collections import deque

class Solution:
    def findOrder(self, words):

        all_chars = set()
        for word in words:
            for char in word:
                all_chars.add(char)

        graph = {c: set() for c in all_chars}
        indegree = {c: 0 for c in all_chars}

        # build graph
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            min_len = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break

        # topological sort (OUTSIDE LOOP)
        q = deque()
        for char in indegree:
            if indegree[char] == 0:
                q.append(char)

        result = []

        while q:
            char = q.popleft()
            result.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(result) != len(all_chars):
            return ""

        return "".join(result)
