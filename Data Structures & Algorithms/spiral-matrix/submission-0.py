class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        answer = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # R
            for j in range(left, right + 1):
                answer.append(matrix[top][j])
            top += 1

            # D
            for i in range(top, bottom + 1):
                answer.append(matrix[i][right])
            right -= 1

            # L
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    answer.append(matrix[bottom][j])
                bottom -= 1

            # U
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    answer.append(matrix[i][left])
                left += 1

        return answer
