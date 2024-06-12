import copy
import math
import tkinter as tk
from tkinter import messagebox

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    count = 0
    for i in board:
        for j in i:
            if j:
                count += 1
    if count % 2 != 0:
        return O
    return X

def actions(board):
    res = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                res.add((i, j))
    return res

def result(board, action):
    curr_player = player(board)
    result_board = copy.deepcopy(board)
    (i, j) = action
    result_board[i][j] = curr_player
    return result_board

def get_horizontal_winner(board):
    winner_val = None
    for i in range(3):
        winner_val = board[i][0]
        for j in range(3):
            if board[i][j] != winner_val:
                winner_val = None
        if winner_val:
            return winner_val
    return winner_val

def get_vertical_winner(board):
    winner_val = None
    for i in range(3):
        winner_val = board[0][i]
        for j in range(3):
            if board[j][i] != winner_val:
                winner_val = None
        if winner_val:
            return winner_val
    return winner_val

def get_diagonal_winner(board):
    winner_val = board[0][0]
    for i in range(3):
        if board[i][i] != winner_val:
            winner_val = None
    if winner_val:
        return winner_val
    winner_val = board[0][2]
    for i in range(3):
        if board[i][2 - i] != winner_val:
            winner_val = None
    return winner_val

def winner(board):
    return get_horizontal_winner(board) or get_vertical_winner(board) or get_diagonal_winner(board) or None

def terminal(board):
    if winner(board) != None:
        return True
    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True

def utility(board):
    winner_val = winner(board)
    if winner_val == X:
        return 1
    elif winner_val == O:
        return -1
    return 0

def minimax(board, alpha, beta):
    if terminal(board):
        return None
    curr_player = player(board)
    if curr_player == X:
        v = -math.inf
        best_action = None
        for action in actions(board):
            new_v = min_value(result(board, action), alpha, beta)
            if new_v > v:
                v = new_v
                best_action = action
            if v >= beta:
                break
            alpha = max(alpha, v)
        return best_action
    else:
        v = math.inf
        best_action = None
        for action in actions(board):
            new_v = max_value(result(board, action), alpha, beta)
            if new_v < v:
                v = new_v
                best_action = action
            if v <= alpha:
                break
            beta = min(beta, v)
        return best_action

def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg='light blue')
        self.board = initial_state()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()
        self.update_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text='', font=('normal', 40), width=5, height=2, bg='light blue', command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

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

    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == X:
                    self.buttons[i][j].config(text='X', state='disabled')
                elif self.board[i][j] == O:
                    self.buttons[i][j].config(text='O', state='disabled')
                else:
                    self.buttons[i][j].config(text='', state='normal')

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

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
