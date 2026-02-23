def solveNQueens(self, n):
        def func (row,ds,cols,diag1,diag2):
            if row == n:
                ans.append(["".join(r) for r in ds])
                return
            
            for col in range(n):
                if col not in cols and (row+col) not in diag1 and (row-col) not in diag2:
                    ds[row][col] = 'Q'
                    cols.add(col)
                    diag1.add(row+col)
                    diag2.add(row-col)
                    
                    func(row+1,ds,cols,diag1,diag2)
                    
                    ds[row][col] = '.'
                    cols.remove(col)
                    diag1.remove(row+col)
                    diag2.remove(row-col)
        
        ans = []
        ds = [['.' for _ in range(n)] for _ in range(n)]
        func(0,ds,set(),set(),set())
        return ans