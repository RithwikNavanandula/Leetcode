class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        p = []
        n = len(graph)
        def dfs(i, k):
            if i not in k: k.append(i)
            for j in graph[i]:
                if j != n-1:
                    dfs(j, deepcopy(k))
                else:
                    b = deepcopy(k)
                    b.append(n-1)
                    if b not in p: p.append(b)
        dfs(0, [])
        return p