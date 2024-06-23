
import random
class CrosswordGame:
    def init(self):
        self.board = self.create_board()
        self.clues = self.create_clues()
        self.player_score = 0

    def create_board(self):
        # Create a 10x10 board with random letters
        board = []
        for i in range(10):
            row = []
            for j in range(10):
                row.append(chr(ord('A') + random.randint(0, 25)))
            board.append(row)
        return board