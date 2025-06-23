class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict

        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)

        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

        def dfs(node):
            if visited[node] == 1:
                return False  # cycle detected
            if visited[node] == 2:
                return True   # already processed

            visited[node] = 1  # mark as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2  # mark as visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
