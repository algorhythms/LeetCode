"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""
__author__ = 'Danyang'


class Solution(object):
    def simplifyPath(self, path):
        """
        use "." as intermediate

        :param path: a string
        :return: a string
        """
        path = path.split("/")
        path = filter(lambda x: x not in ("", " ", "."), path)

        # modify the content of the list, not the structure.
        for idx in xrange(len(path)):
            val = path[idx]
            if val == "..":
                path[idx] = "."

                # rm a previous meaningful part
                i = idx-1
                while i >= 0 and path[i] == ".": i -= 1
                if i >= 0: path[i] = "."  # avoid path[-1]

        path = filter(lambda x: x not in (".",), path)

        if not path:
            return "/"

        path = map(lambda x: "/"+x, path)
        return "".join(path)


if __name__ == "__main__":
    assert Solution().simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///") == "/e/f/g"
    assert Solution().simplifyPath("/a/./b/../../c/") == "/c"
    assert Solution().simplifyPath("/../") == "/"