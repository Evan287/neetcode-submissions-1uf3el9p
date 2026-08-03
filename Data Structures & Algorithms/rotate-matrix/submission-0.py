class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        matrix.reverse()                                    # flip vertically
        for r in range(rows):
            for c in range(r + 1, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]