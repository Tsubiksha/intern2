import tkinter as tk
from tkinter import messagebox

def check_winner():
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0]['text'] == board[i][1]['text'] == board[i][2]['text'] != "":
            highlight_winning_line([(i, 0), (i, 1), (i, 2)])
            return board[i][0]['text']
        if board[0][i]['text'] == board[1][i]['text'] == board[2][i]['text'] != "":
            highlight_winning_line([(0, i), (1, i), (2, i)])
            return board[0][i]['text']

    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        highlight_winning_line([(0, 0), (1, 1), (2, 2)])
        return board[0][0]['text']
    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
        highlight_winning_line([(0, 2), (1, 1), (2, 0)])
        return board[0][2]['text']

    return None

def highlight_winning_line(cells):
    for row, col in cells:
        board[row][col]['bg'] = "lightgreen"

def is_draw():
    for row in board:
        for button in row:
            if button['text'] == "":
                return False
    return True

def on_click(row, col):
    global current_player

    if board[row][col]['text'] == "":
        board[row][col]['text'] = current_player
        board[row][col]['fg'] = "blue" if current_player == "X" else "red"
        winner = check_winner()

        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_board()
        elif is_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showwarning("Tic Tac Toe", "Cell already taken! Try another one.")

def reset_board():
    for row in board:
        for button in row:
            button['text'] = ""
            button['fg'] = "black"
            button['bg'] = "SystemButtonFace"
    global current_player
    current_player = "X"

def restart_game():
    reset_board()
    messagebox.showinfo("Tic Tac Toe", "Game restarted!")

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"
board = []

# Create the grid of buttons
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                           command=lambda r=i, c=j: on_click(r, c), fg="black")
        button.grid(row=i, column=j)
        row.append(button)
    board.append(row)

# Add a restart button
restart_button = tk.Button(root, text="Restart", font=("Arial", 14), command=restart_game, bg="yellow", fg="black")
restart_button.grid(row=3, column=0, columnspan=3)

# Start the main loop
root.mainloop()
