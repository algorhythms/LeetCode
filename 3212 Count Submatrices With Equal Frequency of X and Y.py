"""
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.
 

Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]

Output: 3

Explanation:



Example 2:

Input: grid = [["X","X"],["X","Y"]]

Output: 0

Explanation:

No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]

Output: 0

Explanation:

No submatrix has at least one 'X'.

 

Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 'X', 'Y', or '.'.
"""
class Solution:
    def numberOfSubmatrices_error(self, mat: List[List[str]]) -> int:
        """
        1D: initialize as None, +1, -1, the count the total numbers of 0
        [X, Y, .]
        
        [1, 0, 0]

        2D: project to 1D, project by column
        [X, Y, .]
        [Y, X, .]

        [0, 0, .]

        Error: poor handle of .
        """
        M = len(mat)
        N = len(mat)
        ret = 0
        for lo in range(M):
            # frequency for mat[lo:hi][j]
            freq_cols = [None for _ in range(N)]
            for hi in range(lo+1, M+1):
                for j in range(N):
                    freq_cols[j] = self.acc(freq_cols[j], self.val(mat[hi-1][j]))
                
                F = [0 for _ in range(N+1)]
                for j in range(1, N+1):
                    cur = self.acc(None, self.val(freq_cols[j-1]))
                    F[j] = F[j-1] + 1 if cur == 0 else 0
                
                    ret += F[j]
            
            return ret 

    def val(self, a):
        if a == "X":
            return 1
        elif a == "Y":
            return -1
        else:
            None

    def acc(self, a, b):
        if a == None:
            return self.val(b)
        else:
            a += self.val(b) if self.val(b) is not None else 0

    def numberOfSubmatrices_error_2(self, mat: List[List[str]]) -> int:
        """
        To handle ., cout the submatrix with only "."

        Error: must contain grid[0][0]. This solution counts all submatrices
        """
        vals = {
            "X": 1,
            "Y": -1,
            ".": 0,
        }

        M = len(mat)
        N = len(mat)
        ret = 0
        for lo in range(M):
            # frequency for mat[lo:hi][j]
            freq_cols = [0 for _ in range(N)]
            is_dots_cols = [True for _ in range(N)]
            for hi in range(lo+1, M+1):
                for j in range(N):
                    freq_cols[j] += vals[mat[hi-1][j]]
                    is_dots_cols[j] &= mat[hi-1][j] == "."
                
                F = [0 for _ in range(N+1)]
                D = [0 for _ in range(N+1)]
                for j in range(1, N+1):
                    F[j] = F[j-1] + 1 if freq_cols[j-1] == 0 else 0
                    D[j] = D[j-1] + 1 if is_dots_cols[j-1] else 0
                    ret += max(0, F[j] - D[j])
            
            return ret
    
    def numberOfSubmatrices(self, mat: List[List[str]]) -> int:
        """
        Project 2D to 1D, project by column
        
        To handle ., cout the submatrix with only "."
        To contain grid[0][0], just count number of 0s
        """
        vals = {
            "X": 1,
            "Y": -1,
            ".": 0,
        }

        M = len(mat)
        N = len(mat[0])
        ret = 0

        freq_cols = [0 for _ in range(N)]
        is_dots_cols = [True for _ in range(N)]
        for i in range(M):
            for j in range(N):
                freq_cols[j] += vals[mat[i][j]]
                is_dots_cols[j] &= mat[i][j] == "."
            
            all_dots = True
            acc = 0
            for j in range(N):
                all_dots &= is_dots_cols[j]
                acc += freq_cols[j]
                if acc == 0 and not all_dots:
                    ret += 1
        
        return ret
