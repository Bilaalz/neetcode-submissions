class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set) # create a key = (r/3 and c/3)

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == '.':
                    continue

                if (value in rows[r] or
                    value in cols[c] or
                    value in boxes[r//3, c//3]):
                    return False
                
                rows[r].add(value)
                cols[c].add(value)
                boxes[r//3, c//3].add(value)
        
        return True


                

                
