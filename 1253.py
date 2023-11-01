#this is the solution of Question 1253 on Leetcode
#O(n) time complexity, O(1) space complexity

# we need to create a working matrix. it has 2 rows and some columns have both 1s, and some other columns have only 1 or 0 1s
# we first go through the columns with both 1s, label them and decrease upper and lower variables accordingly.
# then we go through matrix again to fill columns with only one 1. we start with upper row and when upper row is finished
# we continue with lower row and that gives the result.


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper+lower != sum(colsum):
            return []
        m,n = 2, len(colsum)

        matrix = [[0]*n for i in range(m)]
        #go through cols with both rows will be 1. decrease both upper and lower variable.
        for c in range(n):
            if colsum[c] == 2:
                matrix[0][c] = 1
                matrix[1][c] = 1
                upper -= 1
                lower -= 1
                if upper < 0 or lower < 0:
                    return []
        #go through cols again to label remaining cols with only one 1 inside.
        for c in range(n):
            if colsum[c] == 1:
                if upper > 0:
                    matrix[0][c] = 1
                    upper -= 1
                else:
                    matrix[1][c] = 1
                    lower -= 1
        return matrix
