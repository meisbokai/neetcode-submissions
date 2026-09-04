class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            output += f"{len(s)}#{s}"

        # print(output)
        
        return output


    def decode(self, s: str) -> List[str]:
        answer = []
        i=0
        while i <  len(s):
            l_string = "" 
            while s[i] != '#':
                l_string += s[i]
                i += 1
            # print(l_string)
            l = int(l_string)

            # skip #
            i += 1
            
            word = s[i:i+l]
            # print(word)
            answer.append(word)
            i += l
               
            





        return answer