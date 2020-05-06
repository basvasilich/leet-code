# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        def check(l, r, result):
            if l > r:
                return result
            elif l == r:
                if isBadVersion(l):
                    result = max(result, l)
            else:
                m = l + (r - l) // 2
                if not isBadVersion(m):
                    result = check(m + 1, r, result)
                else:
                    result = check(l, m, result)
            return result

        return check(1, n, 1)
