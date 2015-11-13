"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""
import math

__author__ = 'Danyang'


class Solution(object):
    def getPermutation(self, n, k):
        k -= 1

        array = range(1, n+1)
        k %= math.factorial(n)
        ret = []
        for i in xrange(n-1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
            ret.append(array.pop(idx))

        return "".join(map(str, ret))

    def getPermutation(self, n, k):
        """
        Reverse Cantor Expansion

        equation: sum a_i * i! = k
        :param n: integer
        :param k: integer
        :return: String
        """
        # factorial
        fac = [1 for _ in xrange(n)]
        for i in xrange(1, n):
            fac[i] = fac[i-1]*i

        # solve equation
        k -= 1  # index starting from 0
        a = [0 for _ in xrange(n)]
        for i in xrange(n-1, -1, -1):
            a[n-1-i] = k/fac[i]  # a[i] = k/fac[i]
            k %= fac[i]

        # post-process
        candidate = range(1, n+1)  # sorted
        visited = [False for _ in xrange(n)]
        for ind, val in enumerate(a):
            i = 0  # pointer
            cnt = 0  # counter
            while True:
                if visited[i]:
                    i += 1
                else:
                    if cnt == val: break
                    cnt += 1
                    i += 1

            a[ind] = candidate[i]
            visited[i] = True

        return "".join(map(str, a))

    def getPermutation_complicated(self, n, k):
        """
        Mathematics
        Reversed Cantor Expansion

        A = [1, 2, ..., n], where A's index starts from 0
        Suppose for n element, the k-th permutation is:
        [a0, a1, a2, ..., an-1]

        since [a1, a3, ..., an-1] has (n-1)! permutations,
        if k < (n-1)!, a0 = A[0] (first element in array), else a0 = A[k/(n-1)!] (subsequent items)

        recursively, (or iteratively)
        a0 = A[k0/(n-1)!], where k0 = k
        a1 = A[k1/(n-2)!], where k1 = k0%(n-1)! in the remaining array
        a2 = A[k2/(n-3)!], where k2 = k1%(n-2)! in the remaining array
        ...

        :param n: integer
        :param k: integer
        :return: String
        """
        k -= 1  # index starting from 0

        factorial = 1  # (n-1)!
        for i in xrange(1, n):
            factorial *= i

        result = []
        array = range(1, n+1)
        for i in reversed(xrange(1, n)):
            index = k/factorial
            result.append(array[index])
            array = array[:index]+array[index+1:]
            k = k%factorial
            factorial /= i

        # case when factorial=0!
        result.append(array[0])

        return "".join(str(element) for element in result)


class Solution_TLE:
    """
    Time Limit Expected
    """

    def __init__(self):
        self.counter = 0

    def getPermutation(self, n, k):
        """
        dfs, iterate all possibilities
        :param n: integer
        :param k: integer
        :return: String
        """
        if not n:
            return

        sequence = range(1, n+1)
        result = self.get_kth_permutation_dfs(sequence, k, [])
        return "".join(str(element) for element in result)


    def get_kth_permutation_dfs(self, remaining_seq, k, cur):
        """
        dfs until find kth permutation, return that permutation, otherwise return None
        :param remaining_seq:
        :param k:
        :param cur:
        :return:
        """
        if not remaining_seq:
            self.counter += 1
            if self.counter == k:
                return cur

        for ind, val in enumerate(remaining_seq):
            result = self.get_kth_permutation_dfs(remaining_seq[:ind]+remaining_seq[ind+1:], k, cur+[val])
            if result: return result


if __name__ == "__main__":
    assert Solution().getPermutation(4, 6) == "1432"
    assert Solution().getPermutation(2, 2) == "21"
    assert Solution().getPermutation(3, 1) == "123"
    assert Solution().getPermutation(3, 5) == "312"
    print Solution().getPermutation(9, 171669)