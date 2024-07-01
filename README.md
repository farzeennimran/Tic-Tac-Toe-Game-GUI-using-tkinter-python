# Tic Tac Toe Game GUI using Tkinter and Alpha-Beta Pruning 

## Introduction

This project implements a Tic Tac Toe game with a graphical user interface (GUI) using Tkinter in Python. The game uses the Minimax algorithm with Alpha-Beta Pruning to provide an AI opponent that makes optimal moves. The GUI allows players to interact with the game easily, making it a fun and engaging way to play Tic Tac Toe against an AI.

## Alpha-Beta Pruning in Minimax Algorithm

Alpha-Beta Pruning is an optimization technique for the Minimax algorithm. It reduces the number of nodes evaluated by the Minimax algorithm in its search tree, allowing it to search deeper and make more efficient decisions. The idea is to eliminate branches in the game tree that do not need to be explored because they cannot affect the final decision. 

Here's a high-level overview of how Alpha-Beta Pruning is used in this project:

1. **Minimax Algorithm**: This algorithm evaluates all possible moves to determine the optimal one by simulating the game to the end.
2. **Alpha-Beta Pruning**: During the Minimax evaluation, Alpha (the best value the maximizing player can guarantee) and Beta (the best value the minimizing player can guarantee) are used to cut off branches that don't need to be explored.

## GUI using Tkinter

Tkinter is the standard Python library for creating graphical user interfaces. It is used here to create a simple, interactive interface for the Tic Tac Toe game.

### Key Components of the GUI

- **Root Window**: The main window of the application.
- **Buttons**: Each cell of the Tic Tac Toe board is represented by a button.
- **Message Box**: Displays the game result when the game ends.

![image](https://github.com/farzeennimran/Tic-Tac-Toe-Game-GUI-using-tkinter-python/assets/136755585/40584158-6f69-46e4-9033-9a84d9581a49)

![game over](https://github.com/farzeennimran/Tic-Tac-Toe-Game-GUI-using-tkinter-python/assets/136755585/767c7074-9f5a-411d-933e-6a15272f6f35)

## Code Explanation

### Importing Libraries

```python
import copy
import math
import tkinter as tk
from tkinter import messagebox
```

### Constants

```python
X = "X"
O = "O"
EMPTY = None
```

### Game Logic Functions

- **Initial State**: Returns the initial empty board.
- **Player**: Determines whose turn it is.
- **Actions**: Returns the set of possible actions.
- **Result**: Returns the board resulting from a move.
- **Winner**: Determines the winner of the game.
- **Terminal**: Checks if the game is over.
- **Utility**: Returns the utility value of a terminal state.
- **Minimax with Alpha-Beta Pruning**: Determines the optimal move for the current player.

### GUI Class

#### Initialization

The `TicTacToeGUI` class initializes the main window, the board, and the buttons:

```python
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg='light blue')
        self.board = initial_state()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()
        self.update_buttons()
```

#### Creating Buttons

Buttons for each cell are created and placed on the grid:

```python
def create_buttons(self):
    for i in range(3):
        for j in range(3):
            button = tk.Button(self.root, text='', font=('normal', 40), width=5, height=2, bg='light blue', command=lambda row=i, col=j: self.on_button_click(row, col))
            button.grid(row=i, column=j)
            self.buttons[i][j] = button
```

#### Button Click Handler

Handles the logic when a button (cell) is clicked:

```python
def on_button_click(self, row, col):
    if self.board[row][col] == EMPTY and not terminal(self.board):
        self.board = result(self.board, (row, col))
        self.update_buttons()
        if terminal(self.board):
            self.end_game()
            return
        self.board = result(self.board, minimax(self.board, -math.inf, math.inf))
        self.update_buttons()
        if terminal(self.board):
            self.end_game()
```

#### Updating Buttons

Updates the button text to reflect the current board state:

```python
def update_buttons(self):
    for i in range(3):
        for j in range(3):
            if self.board[i][j] == X:
                self.buttons[i][j].config(text='X', state='disabled')
            elif self.board[i][j] == O:
                self.buttons[i][j].config(text='O', state='disabled')
            else:
                self.buttons[i][j].config(text='', state='normal')
```

#### End Game Handling

Displays the game result and resets the board:

```python
def end_game(self):
    winner_val = winner(self.board)
    if winner_val:
        messagebox.showinfo("Game Over", f"Winner: {winner_val}")
    else:
        messagebox.showinfo("Game Over", "It's a tie!")
    self.reset_board()

def reset_board(self):
    self.board = initial_state()
    self.update_buttons()
```

### Main Loop

Runs the Tkinter main loop to start the game:

```python
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
```

