class Crossword:
    def __init__(self, size):
        """
        Initialize the crossword grid.

        Parameters:
        size (int): The size of the grid (size x size).
        """
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]

    def display(self):
        """Display the crossword grid."""
        for row in self.grid:
            print(' '.join(row))
        print()

    def add_word_horizontal(self, word, row, col):
        """
        Add a word to the grid horizontally.

        Parameters:
        word (str): The word to be added.
        row (int): The row index where the word starts.
        col (int): The column index where the word starts.
        """
        if col + len(word) <= self.size:
            for i in range(len(word)):
                self.grid[row][col + i] = word[i]
        else:
            print(f"Cannot add word '{word}' horizontally at ({row}, {col}). Out of bounds.")

    def add_word_vertical(self, word, row, col):
        """
        Add a word to the grid vertically.

        Parameters:
        word (str): The word to be added.
        row (int): The row index where the word starts.
        col (int): The column index where the word starts.
        """
        if row + len(word) <= self.size:
            for i in range(len(word)):
                self.grid[row + i][col] = word[i]
        else:
            print(f"Cannot add word '{word}' vertically at ({row}, {col}). Out of bounds.")

# Example usage
if __name__ == "__main__":
    size = 10  # Define the size of the crossword grid
    crossword = Crossword(size)

    # Add words to the crossword
    crossword.add_word_horizontal("hello", 1, 1)
    crossword.add_word_vertical("world", 1, 1)
    crossword.add_word_horizontal("python", 2, 2)
    crossword.add_word_vertical("python", 2, 2)
    crossword.add_word_vertical("grid", 4, 4)
    crossword.add_word_horizontal("Daniel", 3, 3)
    crossword.add_word_vertical("Daniel", 3, 3)
    crossword.add_word_horizontal("Samuel", 5, 5)
    crossword.add_word_vertical("Samuel", 5, 5)

    # Display the crossword
    crossword.display()
