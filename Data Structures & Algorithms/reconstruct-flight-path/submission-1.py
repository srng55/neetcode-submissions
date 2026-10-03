class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for source, destination in tickets:
            graph[source].append(destination)

        for source in graph:
            graph[source].sort(reverse=True)

        itinerary = []

        def dfs(source):

            while graph[source]:
                destination = graph[source].pop()

                dfs(destination)

            itinerary.append(source)

        
        dfs("JFK")

        return itinerary[::-1]
        