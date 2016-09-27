"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the
10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be
posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
"""
from collections import defaultdict
import heapq

__author__ = 'Daniel'


SZ = 10


class Tweet(object):
    central_clk = 0

    def __init__(self, id, nxt=None):
        self.timestamp = Tweet.central_clk
        self.id = id
        self.next = nxt  # LinkedList
        Tweet.central_clk += 1

    def __cmp__(self, other):
        return - (self.timestamp - other.timestamp)


class Twitter(object):
    """
    need assumption about the frequency of calls of each method

    most efficient heap of list
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(lambda: None)
        self.followees = defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        nxt = self.tweets[userId]  # previous post
        self.tweets[userId] = Tweet(tweetId, nxt)

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        h = []
        if userId not in self.followees[userId] and self.tweets[userId]:
            # possible following oneself
            heapq.heappush(h, self.tweets[userId])

        for followee in self.followees[userId]:
            if self.tweets[followee]:
                heapq.heappush(h, self.tweets[followee])

        ret = []
        while h and len(ret) < SZ:
            tweet = heapq.heappop(h)
            ret.append(tweet.id)
            if tweet.next:
                heapq.heappush(h, tweet.next)

        return ret

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followees[followerId].discard(followeeId)  # no KeyError compared to .remove()


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.unfollow(1, 1)
