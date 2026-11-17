class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # print(matrix)

        c_len, r_len = len(matrix), len(matrix[0])

        zero_rows = [0] * r_len

        one_grid = [[1]*r_len for _ in range(c_len)]

        # print(one_grid)

        for c in range(c_len):
            cols = matrix[c]
            for r in range(r_len):
                ele = cols[r]
                # print(ele)
                if ele == 0:
                    # change row
                    one_grid[c] = zero_rows

                    # change col
                    for i in range(c_len):
                        one_grid[i][r] *= 0
        
        # print(one_grid)

        # replace inplace
        matrix[:] = [[a * b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(matrix, one_grid)]

        # print(matrix)

        
