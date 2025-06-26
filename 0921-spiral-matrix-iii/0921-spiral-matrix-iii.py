class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        a = []
        d = 0
        tb = bb = rStart
        rb = cStart
        lb = cStart
        a.append([rStart,cStart])
        i = tb
        cycle = 0
        while len(a) < rows*cols:
            if d == 0 and len(a) < rows*cols:
                j = lb+1
                while j<= rb+1:
                    if -1 < i < rows and -1 < j < cols:
                        a.append([i,j])
                    j += 1
                j -= 1
                d = 1
                rb += 1
            if d == 1 and len(a) < rows*cols:
                i = tb+1
                while i <= bb+1:
                    if -1 < i < rows and -1 < j < cols:
                        a.append([i,j])
                    i += 1
                i-=1
                d = 2
                bb += 1
            if d == 2 and len(a) < rows*cols:
                j = rb-1
                while j >= lb-1:
                    if -1 < i < rows and -1 < j < cols:
                        a.append([i,j])
                    j-=1
                j+=1
                lb-=1
                d = 3
            if d==3 and len(a) < rows*cols:
                i = bb-1
                while i >= tb-1:
                    if -1 < i < rows and -1 < j < cols:
                        a.append([i,j])
                    i-=1
                i+=1
                tb -= 1
                d = 0
            
            cycle += 1
        return a