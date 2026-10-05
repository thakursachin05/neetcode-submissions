from typing import List

class Twitter:

    def __init__(self):
        # Stores globally posted tweets as [userId, tweetId]
        self.posts = []
        # Maps a userId to a SET of userIds they are following: { userId: {followeeId1, followeeId2} }
        self.following = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append([userId, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        # Get the set of users this person follows (default to empty set if none)
        followed_users = self.following.get(userId, set())
        
        # Scan backward from the most recent tweet
        idx = len(self.posts) - 1
        
        # Fetch up to 10 tweets
        while idx >= 0 and len(res) < 10:
            tweet_author, tweet_id = self.posts[idx]
            
            # Include if it's their own tweet OR a tweet from someone they follow
            if tweet_author == userId or tweet_author in followed_users:
                res.append(tweet_id)
                
            idx -= 1
            
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
