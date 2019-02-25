#!/usr/bin/python3
"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words
have the same frequency, then the word with the lower alphabetical order comes
first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""
import heapq
from collections import defaultdict
from typing import List


class Word:
    def __init__(self, content, count):
        self.content = content
        self.count = count

    def __lt__(self, other):
        if self.count == other.count:
            return self.content > other.content

        return self.count < other.count


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        quick select log n
        heap log k
        """
        h = []
        counter = defaultdict(int)
        for w in words:
            counter[w] += 1

        for w, c in counter.items():
            heapq.heappush(h, Word(w, c))
            if len(h) > k:
                heapq.heappop(h)

        ret = []
        while h:
            w = heapq.heappop(h).content
            ret.append(w)

        return ret[::-1]


if __name__ == "__main__":
    assert Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
