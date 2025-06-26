class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        a = [0]*n
        p = []
        for _ in range(n):
            p.append(deepcopy(a))
        
        d = 0
        tb = 0
        bb = n-1
        rb = n-1
        lb = 0
        c = 0
        while c < n**2:
            if d == 0 and c < n**2:
                j = lb
                while j <= rb:
                    c+=1
                    p[tb][j] = c 
                    j += 1
                d = 1
                tb += 1
            if d == 1 and c < n**2:
                i = tb
                while i <= bb:
                    c+=1
                    p[i][rb] = c
                    i += 1
                d = 2
                rb -= 1
            if d == 2 and c < n**2:
                j = rb
                while j >= lb:
                    c+=1
                    p[bb][j] = c
                    j-=1
                bb -= 1
                d = 3
            if d==3 and c < n**2:
                i = bb
                while i >= tb:
                    c+=1
                    p[i][lb] = c
                    i-=1
                lb += 1
                d = 0
        return p