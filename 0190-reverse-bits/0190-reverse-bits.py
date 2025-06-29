class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = str(bin(n)[2:]).zfill(32)
        n = n[::-1]
        return int(n, 2)