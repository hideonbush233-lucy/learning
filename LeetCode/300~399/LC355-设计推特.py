# 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

#     postTweet(userId, tweetId): 创建一条新的推文
#     getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
#     follow(followerId, followeeId): 关注一个用户
#     unfollow(followerId, followeeId): 取消关注一个用户


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(list)
        self.tweets_time = defaultdict(list)
        self.time = 0
        self.follows = defaultdict(set)
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].insert(0, tweetId)
        self.tweets_time[userId].append([self.time, tweetId])
        self.time+=1

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        news = self.tweets_time[userId].copy()
        for f in self.follows[userId]:
            news+=self.tweets_time[f]
        if news: 
            news.sort(key=lambda x:x[0], reverse=True)
            return [t[1] for t in news][0:10]
        else: 
            return []

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.follows[followerId]: 
            self.follows[followerId].remove(followeeId)
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
