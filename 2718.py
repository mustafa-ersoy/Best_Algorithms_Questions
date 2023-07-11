#This is the solution of Question 2718 on Leetcode
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        #When we think about it, later queries will over-write the initial queries
        #Therefore, most permanent queries will be the last ones, we need to scan through the matrix backwards.
        #When we scan the matrix backwards, we need to keep track of altered rows and columns.
        #if all rows OR all columns have been altered, we need to stop there because this means full content
        #of the matrix is altered starting from that query till the end.


        #keeping track of the altered rows and columns
        covered_rows, covered_cols, total = set(), set(),0
        #scanning backwards in the query matrix because late-comers will over-write previous queries.
        for i in range(len(queries)-1, -1, -1):
            #extracting the type (row or col), index and value
            typ, ind, val = queries[i]
            #if type == 0, we change a full row. If type == 1, we change a full column.
            #Let's say we have 6rows x 8 cols matrix. If I change row 2, that means I'm changing all the cells in
            #row 2 which means 8 cells. However, if 3 of the columns are over-written before, that means current
            #change will not contribute to these 3 cells therefore I will only be able to change 8-3 = 5 cells and
            #if value = 4, total sum I get from this change will be 4*5 = 20 and I will add that to total variable.
            #after that operation I will add row 2 to the covered_rows set because I changed that row currently.
            if typ == 0:
                if ind in covered_rows: continue
                total += (n-len(covered_cols))*val
                covered_rows.add(ind)
            else:
                if ind in covered_cols: continue
                total += (n-len(covered_rows))*val
                covered_cols.add(ind)
            if len(covered_rows) == n or len(covered_cols) == n: return total
        return total