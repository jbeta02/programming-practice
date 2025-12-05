# LeetCode 58
# time: O(n) where n is len of string
# space: O(n)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        token_lst = s.split(' ')
        # print(token_lst)

        for i in range(len(token_lst), 0, -1):
            # print(i, token_lst[i-1])
            if token_lst[i-1] != '':
                return len(token_lst[i-1])

        # if len 1
        return len(token_lst)