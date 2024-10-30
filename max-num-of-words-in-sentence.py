class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        leng = []
        for i in range(len(sentences)):
            m = []
            m = sentences[i].split(' ')
            leng.append(len(m))
        return max(leng)


sol = Solution()

