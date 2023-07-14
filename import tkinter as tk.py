import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import random

# Quote Generator
class QuoteGenerator:
    def __init__(self, main_menu_window):
        self.main_menu_window = main_menu_window

        self.quotes = [
            "Believe you can and you're halfway there.",
            "The only way to do great work is to love what you do.",
            "Don't watch the clock; do what it does. Keep going.",
            "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
            "The future belongs to those who believe in the beauty of their dreams.",
            "The best way to predict the future is to create it.",
            "Success is not final, failure is not fatal: It is the courage to continue that counts.",
            "The only limit to our realization of tomorrow will be our doubts of today.",
            "In the middle of every difficulty lies opportunity.",
            "You are never too old to set another goal or to dream a new dream.",
            "The future starts today, not tomorrow.",
            "Your time is limited, don't waste it living someone else's life.",
            "I can't change the direction of the wind, but I can adjust my sails to always reach my destination.",
            "Opportunities don't happen. You create them.",
            "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.",
            "You miss 100% of the shots you don't take.",
            "The harder I work, the luckier I get.",
            "The only person you should try to be better than is the person you were yesterday.",
            "Success usually comes to those who are too busy to be looking for it.",
            "The secret to getting ahead is getting started."
        ]

        self.quote_window = tk.Toplevel(main_menu_window)
        self.quote_window.title("Quote")
        self.quote_window.configure(bg="#E0E0E0")

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 14))

        self.quote_label = tk.Label(self.quote_window, text="", font=("Helvetica", 14), bg="#E0E0E0")
        self.quote_label.pack(pady=20)

        # Next Quote Button
        next_quote_btn = ttk.Button(self.quote_window, text="Next Quote", command=self.get_quote)
        next_quote_btn.pack(pady=10)

        # Exit to Main Menu Button
        exit_btn = ttk.Button(self.quote_window, text="Exit to Main Menu", command=self.exit_to_main_menu)
        exit_btn.pack(pady=10)

        self.get_quote()

    def get_quote(self):
        quote = random.choice(self.quotes)
        self.display_quote(quote)

    def display_quote(self, quote):
        self.quote_label.config(text=quote)

    def exit_to_main_menu(self):
        self.quote_window.destroy()
        self.main_menu_window.deiconify()  # Show the main menu window


# Tic Tac Toe Game
class TicTacToe:
    def __init__(self, main_menu_window):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.moves_left = 9
        self.game_ended = False

        self.main_menu_window = main_menu_window

        self.game_window = tk.Toplevel(main_menu_window)
        self.game_window.title("Tic Tac Toe")
        self.game_window.configure(bg="#E0E0E0")

        # Load and set the background image
        background_image = Image.open("placeholder_image.jpg")
        background_image = background_image.resize((400, 400), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(background_image)
        self.background_label = tk.Label(self.game_window, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 24))

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = ttk.Button(self.game_window, text=" ", width=10, command=lambda x=i, y=j: self.make_move(x, y))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

        # Play Again Button
        play_again_btn = ttk.Button(self.game_window, text="Play Again", command=self.play_again)
        play_again_btn.grid(row=3, column=0, padx=5, pady=10)

        # Exit to Main Menu Button
        exit_btn = ttk.Button(self.game_window, text="Exit to Main Menu", command=self.exit_to_main_menu)
        exit_btn.grid(row=3, column=1, padx=5, pady=10)

    def make_move(self, row, col):
        if self.board[row][col] == " " and not self.game_ended:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state="disabled")

            if self.check_winner():
                self.game_ended = True
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            elif self.moves_left == 1:
                self.game_ended = True
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.moves_left -= 1

            if self.current_player == "O" and not self.game_ended:
                self.make_ai_move()

    def make_ai_move(self):
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    empty_cells.append((i, j))

        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False

    def play_again(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.moves_left = 9
        self.game_ended = False

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state="enabled")

    def exit_to_main_menu(self):
        self.game_window.destroy()
        self.main_menu_window.deiconify()  # Show the main menu window


# Main Menu
def show_main_menu():
    main_menu_window = tk.Tk()
    main_menu_window.title("Game Menu")
    main_menu_window.geometry("400x250")  # Set the size of the main menu window
    main_menu_window.configure(bg="#E0E0E0")

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 18))

    # Tic Tac Toe Button
    tic_tac_toe_btn = ttk.Button(main_menu_window, text="Play Tic Tac Toe", command=lambda: start_tic_tac_toe(main_menu_window))
    tic_tac_toe_btn.pack(pady=10)

    # Quote Generator Button
    quote_generator_btn = ttk.Button(main_menu_window, text="Generate Quote", command=lambda: start_quote_generator(main_menu_window))
    quote_generator_btn.pack()

    main_menu_window.mainloop()

def start_tic_tac_toe(main_menu_window):
    main_menu_window.withdraw()  # Hide the main menu window
    TicTacToe(main_menu_window)

def start_quote_generator(main_menu_window):
    main_menu_window.withdraw()  # Hide the main menu window
    QuoteGenerator(main_menu_window)

# Run the main menu
show_main_menu()
