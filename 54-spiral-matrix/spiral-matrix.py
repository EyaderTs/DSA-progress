class Solution(object):
    def spiralOrder(self, matrix):
        
        ret = []

        while matrix:
            #step 1 - remove the top
            ret += matrix.pop(0)

            if matrix and matrix[0]:
                #removet the outer right (from top to bottom)
                for row in matrix:
                    ret.append(row.pop())
                #remove the bottom (in reverse order)
                # last_row = matrix[-1]
                for _ in range(len(matrix[-1])):
                    ret.append(matrix[-1].pop())
                matrix.pop()

            if matrix and matrix[0]:
                rev = matrix [::-1]
                print(rev)
                print(matrix)
                #remove the outer left (from bottom to top)
                for row in rev:
                    ret.append(row[0])
                    row.pop(0)
        return ret

        
        