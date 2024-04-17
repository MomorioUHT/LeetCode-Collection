class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0;
        
        islands = 0
        rows,cols = len(grid),len(grid[0])
        
        def markIslands(r: int, c: int):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] != "1": return
            
            grid[r][c] = "0"
            
            markIslands(r-1,c)
            markIslands(r+1,c)
            markIslands(r,c+1)
            markIslands(r,c-1)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    markIslands(i,j)
                    
        return islands