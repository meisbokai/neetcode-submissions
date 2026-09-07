class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutated substring
        # sliding window - fixed len = shorter str
        # hashmap char:count

        # s2 must contain s1
        if len(s2) < len(s1):
            return False
        
        # s1 hashmap
        s1_map = {}
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1

        # print(s1_map)

        # window size
        window = len(s1)

        # window approach
        l=0
        s2_map = {}
        for r in range(len(s2)):
            # Add right character
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1

            # Window is too large
            if r - l + 1 > window:
                if s2_map[s2[l]] == 1:
                    del s2_map[s2[l]]
                else:
                    s2_map[s2[l]] -= 1

                l += 1

            # Check current window
            if s1_map == s2_map:
                return True

        return False
