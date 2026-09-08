class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t in s
        if len(s) < len(t):
            return ""

        # print(len(s), len(t))   

        # counts of c in t
        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1

        # sliding window across s
        s_map = {}
        l = 0
        shortest_l, shortest_r = 0, float("inf")

        key_count = 0

        for r in range(len(s)):

            if s[r] in t_map:
                s_map[s[r]] = s_map.get(s[r], 0) + 1

                # check if s_map and t_map has same count
                if s_map[s[r]] == t_map[s[r]]:
                    key_count += 1

            # while key count == len(t), check window length
            while key_count == len(t_map):

                # update shortest
                if r - l < shortest_r - shortest_l:
                    shortest_r, shortest_l = r, l

                # update count in both maps
                if s[l] in t_map:
                    if s_map[s[l]] == t_map[s[l]]:
                        key_count -= 1

                    s_map[s[l]] -= 1    

                # move left window
                l += 1

        # no solution
        if shortest_r == float("inf"):
            return ""

        # print(f"shortest_l={shortest_l}, shortest_r={shortest_r}")
        return s[shortest_l:shortest_r + 1]  