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
class Solution:
    def simplifyPath(self, path):
        """
        use "." as intermediate

        :param path: a string
        :return: a string
        """
        path = path.split("/")
        path = filter(lambda x: x not in ("", " ", "."), path)

        for ind, val in enumerate(path):  # some unexpected error in memory
            if val=="..":
                path[ind] = "."

                i = 1
                while ind-i>=0 and path[ind-i]==".": i += 1
                if ind-i>=0: path[ind-i] = "."  # avoid unexpected path[-1]

        path = filter(lambda x: x not in (".",), path)

        if not path:
            return "/"

        path = map(lambda x: "/"+x, path)
        return "".join(path)

if __name__=="__main__":
    assert Solution().simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///")=="/e/f/g"
    assert Solution().simplifyPath("/a/./b/../../c/")=="/c"
    assert Solution().simplifyPath("/../")=="/"