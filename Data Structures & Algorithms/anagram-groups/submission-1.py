class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        answer = {}
        
        for string in strs:
            # since each string is made up of only lower case
            case = [0] * 26

            for c in string:
                case[ord(c) - ord('a')] += 1

            key = tuple(case)

            if key not in answer:
                answer[key] = []

            answer[key].append(string)

        return list(answer.values())

        