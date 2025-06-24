class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        p = [0]*len(rooms)
        p[0] = 1
        def dfs(n):
            for i in n:
                if p[i] == 0: 
                    p[i] = 1
                    dfs(rooms[i])
        dfs(rooms[0])
        for i in p:
            if i ==0:
                return False
        return True