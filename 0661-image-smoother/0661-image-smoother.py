from copy import deepcopy

class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        def summ(i, j):
            k = 0
            n = 0
            if i != 0:
                n += 1
                k += img[i-1][j]
                if j != 0:
                    n += 1
                    k += img[i-1][j-1]
                if j < len(img[0]) - 1:
                    n += 1
                    k += img[i-1][j+1]    
            if i < len(img) - 1:
                n += 1
                k += img[i+1][j]
                if j != 0:
                    n += 1
                    k += img[i+1][j-1]
                if j < len(img[0]) - 1:
                    n += 1
                    k += img[i+1][j+1]
            n += 1
            k += img[i][j]
            if j != 0:
                n += 1
                k += img[i][j-1]
            if j < len(img[0]) - 1:
                n += 1
                k += img[i][j+1]
            return k // n

        p = deepcopy(img)
        for i in range(len(img)):
            for j in range(len(img[0])): 
                p[i][j] = summ(i, j)
        return p
