from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph = defaultdict(set)
        indegree = {char: 0 for word in words for char in word}

        # Build graph
        for i in range(len(words) - 1):

            word1 = words[i]
            word2 = words[i + 1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for j in range(min(len(word1), len(word2))):

                if word1[j] != word2[j]:

                    first = word1[j]
                    second = word2[j]

                    if second not in graph[first]:
                        graph[first].add(second)
                        indegree[second] += 1

                    break

        # Topological sort
        q = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                q.append(ch)

        answer = []

        while q:
            ch = q.popleft()
            answer.append(ch)

            for neighbour in graph[ch]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    q.append(neighbour)

        if len(answer) != len(indegree):
            return ""

        return "".join(answer)