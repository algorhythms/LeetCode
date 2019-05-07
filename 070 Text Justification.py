"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left
and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces
' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide
evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
"""
__author__ = 'Danyang'


class Solution:
    def fullJustify(self, words, L):
        """

        :param words: a list of str
        :param L: int
        :return: a list of str
        """
        result = []
        self.break_line(words, L, result)
        return self.distribute_space(L, result)

    def break_line(self, words, L, result):
        if not words:
            return

        cur_length = -1
        lst = []
        i = 0
        while i<len(words):
            word = words[i]
            cur_length += 1 # space in left justified
            cur_length += len(word)
            if cur_length>L: break
            lst.append(word)
            i += 1

        result.append(lst)
        self.break_line(words[i:], L, result)


    def distribute_space(self, L, result):
        new_result = []
        for ind, line in enumerate(result):
            word_cnt = len(line)
            str_builder = []
            space_cnt = L-sum(len(word) for word in line)
            hole_cnt = word_cnt-1
            if ind<len(result)-1:
                if hole_cnt>0:
                    space = space_cnt/hole_cnt
                    remain = space_cnt%hole_cnt

                    for word in line[:-1]:
                        str_builder.append(word)
                        str_builder.append(" "*space)
                        if remain>0:
                            str_builder.append(" ")
                            remain -= 1

                    str_builder.append(line[-1])
                else:
                    str_builder.append(line[-1])
                    str_builder.append(" "*space_cnt)
            else:  # last line, special handling
                str_builder = [" ".join(line)]
                str_builder.append(" "*(space_cnt-hole_cnt))

            new_result.append("".join(str_builder))

        return new_result



if __name__=="__main__":
    print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    print Solution().fullJustify(["What","must","be","shall","be."], 12)
