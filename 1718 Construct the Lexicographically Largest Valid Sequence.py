"""
"""
class SolutionTLE:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """
        backtrack enumeration

        brute-force
        * iterate through numbers 
        * iterate through position
        """
        maxa = [-1 for _ in range(2*n-1)]
        self.backtrack(list(maxa), n, 1, maxa)
        return maxa
    
    def backtrack(self, A, n, x, maxa):
        if all(a != -1 for a in A):
            maxa[:] = max(maxa, A)  # modify in place
            return
        
        for j in range(len(A)):
            if A[j] == -1:
                if x == 1:
                    A[j] = x
                    self.backtrack(A, n, x+1, maxa)
                    A[j] = -1
                elif j + x < len(A) and A[j+x] == -1:
                    A[j] = x
                    A[j+x] = x
                    self.backtrack(A, n, x+1, maxa)
                    A[j] = -1
                    A[j+x] = -1 
        

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """
        backtrack enumeration

        brute-force
        * iterate through position first
        * iterate through numbers            
        """
        maxa = [-1 for _ in range(2*n-1)]
        visited = [False for _ in range(n+1)]
        self.backtrack(list(maxa), 0, n, visited, maxa)
        return maxa
    
    def backtrack(self, A, i, n, visited, maxa):
        if all(a != -1 for a in A):
            maxa[:] = max(maxa, A)  # modify in place
            return True
        
        for x in range(n, 0, -1):
            if not visited[x]:
                if A[i] == -1:
                    if x == 1:
                        A[i] = x
                        visited[x] = True
                        if self.backtrack(A, i+1, n, visited, maxa):
                            return True
                        A[i] = -1
                        visited[x] = False
                    elif i+x < len(A) and A[i+x] == -1:
                        A[i] = x
                        A[i+x] = x
                        visited[x] = True
                        if self.backtrack(A, i+1, n, visited, maxa):
                            return True
                        A[i] = -1
                        A[i+x] = -1
                        visited[x] = False
                else:
                    return self.backtrack(A, i+1, n, visited, maxa)
            
        return False
        
        