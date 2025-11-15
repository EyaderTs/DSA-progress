class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        temp = []
        
        while matrix and matrix[0]:
            firstRow = matrix.pop(0)
            temp.extend(firstRow)
            
            if not matrix or not matrix[0]: 
                break

            for row in matrix:
                lastElement = row.pop()
                temp.append(lastElement)

            if not matrix or not matrix[0]:
                break

            lastRow = matrix.pop() 
            lastRow.reverse()      
            temp.extend(lastRow)

            if not matrix or not matrix[0]:
                break
                
            for row_index in range(len(matrix) - 1, -1, -1):
                first_element = matrix[row_index].pop(0)
                temp.append(first_element)
                
        return temp


        