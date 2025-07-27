class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0 
        myset = set(jewels)

        for s in stones:
            if s in myset:
                count+=1
        return count
