import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time = 0

        # userID -> [tweetId] (newest at the end)
        self.posts = defaultdict(list)
        
        # userId -> [userIds of ppl they follow]
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posts[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        recent = []
        heap = []

        # PUT OWN MOST RECENT POST
        if self.posts[userId]:
            t, tweetId = self.posts[userId][-1]
            heapq.heappush_max(heap, (t, -1, tweetId, userId))

        # PUT EACH FOLLOWINGS MOST RECENT POST
        following = self.following[userId]
        for follower in following:
            followerPosts = self.posts[follower]
            if followerPosts:
                t, tweetId = self.posts[follower][-1]
                heapq.heappush_max(heap, (t, -1, tweetId, follower))

        while len(recent) < 10 and heap:
            t, idx, tweet_id, user_id = heapq.heappop_max(heap)

            idx -= 1
            if -idx <= len(self.posts[user_id]):
                new_t, new_tweet_id = self.posts[user_id][idx]
                heapq.heappush_max(heap, (new_t, idx, new_tweet_id, user_id))

            recent.append(tweet_id)
        
        return recent


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].discard(followeeId)
        
