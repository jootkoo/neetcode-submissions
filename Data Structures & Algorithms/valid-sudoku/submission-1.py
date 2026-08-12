class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashm = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        columns = [set() for _ in range(9)] #initialize the columns
        rows = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                value = board[row][col] #row picks the list, col pick the item inside the list
                if value == ".":
                    continue
                box_row = row // 3
                box_col = col // 3
                box_index = (box_row)*3 + box_col #0-9 index
                

                if value in hashm[box_index] or value in rows[row] or value in columns[col]:
                    return False
                else:
                    hashm[box_index].append(value)
                    columns[col].add(value) #column checker
                    rows[row].add(value) #row checker
        return True

