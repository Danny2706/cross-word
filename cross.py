
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
    def create_clues(self):
        # Create a list of clues for the player to solve
        clues = [
            {"direction": "across", "number": 1, "clue": "Flower", "answer": "ROSE"},
            {"direction": "down", "number": 2, "clue": "Animal", "answer": "CAT"},
            {"direction": "across", "number": 3, "clue": "City", "answer": "PARIS"},
           
        ]
        return clues

    def print_board(self):
        # Print the current state of the board
        for row in self.board:
            print(" ".join(row))
    def play(self):
            # Main game loop
        while True:
            self.print_board()
            print("Score:", self.player_score)
            print("Enter 'solve' to solve a clue, or 'quit' to quit the game.")