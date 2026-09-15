class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph={i:[] for i in range(numCourses)}
        preCount=[0]*numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            preCount[crs]+=1

        q=deque()
        order=[]

        for crs in range(numCourses):
            if preCount[crs]==0:
                q.append(crs)

        while q:

            crs=q.popleft()
            order.append(crs)

            for nextcrs in graph[crs]:
                preCount[nextcrs]-=1

                if preCount[nextcrs]==0:
                    q.append(nextcrs)

        if len(order)==numCourses:
            return order

        return []

        