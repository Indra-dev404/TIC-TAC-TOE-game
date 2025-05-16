import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("600x650")
        
        # Game state variables
        self.current_player = 'X'
        self.board = ['' for _ in range(9)]
        self.game_over = False
        
        # Create status label
        self.status_label = tk.Label(
            master, 
            text="Player X's Turn", 
            font=('Arial', 16)
        )
        self.status_label.pack(pady=10)
        
        # Create game board frame
        self.board_frame = tk.Frame(master)
        self.board_frame.pack()
        
        # Create buttons for the game board
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.board_frame, 
                    text='', 
                    font=('Arial', 20), 
                    width=5, 
                    height=2,
                    command=lambda row=i, col=j: self.on_click(row, col)
                )
                button.grid(row=i, column=j, padx=2, pady=2)
                self.buttons.append(button)
        
        # Reset button
        self.reset_button = tk.Button(
            master, 
            text="Reset Game", 
            font=('Arial', 12),
            command=self.reset_game
        )
        self.reset_button.pack(pady=10)
    
    def on_click(self, row, col):
        # Calculate the index in the board list
        index = 3 * row + col
        
        # Check if the game is over or the cell is already filled
        if self.game_over or self.board[index]:
            return
        
        # Mark the cell
        self.board[index] = self.current_player
        self.buttons[index].config(
            text=self.current_player, 
            fg='blue' if self.current_player == 'X' else 'red'
        )
        
        # Check for win
        if self.check_win():
            messagebox.showinfo(
                "Game Over", 
                f"Player {self.current_player} wins!"
            )
            self.game_over = True
            self.update_status(f"Player {self.current_player} Wins!")
            return
        
        # Check for draw
        if all(self.board):
            messagebox.showinfo("Game Over", "It's a Draw!")
            self.game_over = True
            self.update_status("Draw!")
            return
        
        # Switch players
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.update_status(f"Player {self.current_player}'s Turn")
    
    def check_win(self):
        # Winning combinations
        win_combinations = [
            # Rows
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            # Columns
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            # Diagonals
            (0, 4, 8), (2, 4, 6)
        ]
        
        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]) and self.board[combo[0]]:
                return True
        return False
    
    def update_status(self, message):
        self.status_label.config(text=message)
    
    def reset_game(self):
        # Reset board
        self.board = ['' for _ in range(9)]
        
        # Reset buttons
        for button in self.buttons:
            button.config(text='')
        
        # Reset game state
        self.current_player = 'X'
        self.game_over = False
        
        # Update status
        self.update_status("Player X's Turn")

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()