class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0
        ans = 0
        m = n
        while m !=0:
            
            m = n>>count
            if m % 2 ==1:
                ans += 1
            # print(m)
            count += 1


        return ans
        