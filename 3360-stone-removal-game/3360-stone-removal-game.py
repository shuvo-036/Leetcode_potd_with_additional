class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        stone = 10
        alice = True

        while n >= stone:
            n -= stone
            stone -= 1
            alice = not alice
        
        return not alice