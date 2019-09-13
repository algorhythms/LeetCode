#!/usr/bin/python3
"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Round robin distribution of spaces

        Jump and then backtrack
        """
        ret = []
        char_cnt = 0  # char exclude spaces
        cur_words = []

        for w in words:
            cur_words.append(w)
            char_cnt += len(w)
            if char_cnt + len(cur_words) - 1 > maxWidth:
                # break
                cur_words.pop()
                char_cnt -= len(w)
                for i in range(maxWidth - char_cnt):
                    cur_words[i % max(1, len(cur_words) - 1)] += " "

                ret.append("".join(cur_words))

                cur_words = [w]
                char_cnt = len(w)

        # last line
        last = " ".join(cur_words)
        ret.append(last + " " * (maxWidth - len(last)))
        return ret


class Solution2:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Round robin distribution of spaces

        Look before jump
        Look before you leap
        """
        ret = []
        char_cnt = 0
        cur_words = []

        for w in words:
            # len(cur_words) is the space needed with len(cur_words) + 1 words
            if char_cnt + len(w) + len(cur_words) > maxWidth:
                # break, move w into the next line
                # Round robin distribut the spaces except for the last word
                for i in range(maxWidth - char_cnt):
                    cur_words[i % max(1, len(cur_words) - 1)] += " "  # insert in between
                    # len(cur_words) - 1 can be 0
                ret.append("".join(cur_words))

                cur_words = []
                char_cnt = 0

            cur_words.append(w)
            char_cnt += len(w)

        # last line
        last = " ".join(cur_words)
        ret.append(last + " " * (maxWidth - len(last)))
        return ret


if __name__ == "__main__":
    assert Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) == ["This    is    an","example  of text","justification.  "]
    assert Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16) == ["What   must   be","acknowledgment  ","shall be        "]
