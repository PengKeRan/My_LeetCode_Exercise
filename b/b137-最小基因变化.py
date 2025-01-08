# 433. 最小基因变化
class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        queue = [(startGene, 0)]
        vis = set()
        while queue:
            gene, step = queue.pop(0)
            for mutate in bank:
                if gene != mutate and self.geneChange(gene, mutate):
                    if mutate == endGene:
                        return step + 1
                    if mutate not in vis:
                        vis.add(mutate)
                        queue.append((mutate, step + 1))
        return -1

    def geneChange(self, s1, s2):
        l1 = len(s1)
        diff = 0
        for i in range(l1):
            if s1[i] != s2[i]:
                diff += 1
            if diff > 1:
                return False
        return True


start = "AACCTTGG"
end = "AATTCCGG"
bank = ["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"]
print(Solution().minMutation(start, end, bank))
