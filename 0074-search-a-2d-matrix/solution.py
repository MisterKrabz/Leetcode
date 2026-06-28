class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        combined = []
        for row in matrix: 
            combined.extend(row)
        print(combined)
        
        return target in combined 
