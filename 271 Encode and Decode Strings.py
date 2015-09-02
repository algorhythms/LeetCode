"""
Premium Question
"""
__author__ = 'Daniel'


class Codec(object):
    def encode(self, strs):
        """
        Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        strs = map(lambda x: x.replace("\x00", "\\x00"), strs)
        ret = ""
        for s in strs:
            ret += s+"\x00"
        return ret

    def decode(self, s):
        """
        Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if "\x00" not in s:
            return []

        s = s[:-1]  # traiing \x00
        strs = s.split("\x00")
        strs = map(lambda x: x.replace("\\x00", "\x00"), strs)
        return strs
