class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        storage={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}


        for row in range(9):
            for col in range(9):
                square = (row // 3)*3 + (col//3)
                value = board[row][col]

                if value == ".":
                    continue
                elif value in storage[square] or value in rows[row] or value in columns[col]:
                    return False
                else:
                    storage[square].append(value)
                    columns[col].add(value)
                    rows[row].add(value)
        return True

                
