class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweet[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []

        self.following[userId].add(userId)

        for followee in self.following[userId]:

            if not self.tweet[followee]:
                continue

            index = len(self.tweet[followee]) - 1
            count, tweetId = self.tweet[followee][index]

            heapq.heappush(
                minHeap,
                (-count, tweetId, followee, index)
            )

        result = []

        while minHeap and len(result) < 10:

            count, tweetId, followee, index = heapq.heappop(minHeap)

            result.append(tweetId)

            if index > 0:
                index -= 1

                count, tweetId = self.tweet[followee][index]

                heapq.heappush(
                    minHeap,
                    (-count, tweetId, followee, index)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)