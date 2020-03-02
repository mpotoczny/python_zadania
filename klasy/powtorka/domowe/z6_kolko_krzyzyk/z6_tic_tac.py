# Gra w kółko i krzyżyk

# Do terminala czyszczenie ekranu
# import os
# os.system("cls")

class Board():
    def __init__(self):
        self.cells = [" "] * 10 # 10 pustych miejsc, 9 pol do gry (ignoruję indeks 0)

    # def display(self):
    #      print(f'{self.cells[1]} | {self.cells[2]} | {self.cells[3]}\n'
    #            f'----------\n'
    #            f'{self.cells[4]} | {self.cells[5]} | {self.cells[6]}\n'
    #            f'----------\n'
    #            f'{self.cells[7]} | {self.cells[8]} | {self.cells[9]}')

    def __str__(self):
        return (f'{self.cells[1]} | {self.cells[2]} | {self.cells[3]}\n'
               f'----------\n'
               f'{self.cells[4]} | {self.cells[5]} | {self.cells[6]}\n'
               f'----------\n'
               f'{self.cells[7]} | {self.cells[8]} | {self.cells[9]}')

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    # def is_winner(self, player) -> bool:
    #     if self.cells[1] == self.cells[2] == self.cells[3] == player:
    #         return True
    #     if self.cells[4] == self.cells[5] == self.cells[6] == player:
    #         return True
    #     if self.cells[7] == self.cells[8] == self.cells[9] == player:
    #         return True
    #     if self.cells[1] == self.cells[4] == self.cells[7] == player:
    #         return True
    #     if self.cells[2] == self.cells[5] == self.cells[8] == player:
    #         return True
    #     if self.cells[3] == self.cells[6] == self.cells[9] == player:
    #         return True
    #     if self.cells[1] == self.cells[5] == self.cells[9] == player:
    #         return True
    #     if self.cells[3] == self.cells[5] == self.cells[7] == player:
    #         return True
    #
    #     return False

    def is_winner(self, player) -> bool:
        combinations = [[1,2,3],
                        [4,5,6],
                        [7,8,9],
                        [1,4,7],
                        [2,5,8],
                        [3,6,9],
                        [1,5,9],
                        [3,5,7]]

        for combo in combinations:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False

            # przerywa funkcję i grę jeśli ktoś spełni warunki wygranej
            if result is True:
                return True

        return False

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1

        if used_cells == 9:
            return True
        return False

    def reset(self):
        self.cells = [" "] * 10 # ponowna inicjalizacja pustej planszy

# utworzenie planszy
board = Board()

def print_header():
    print("\nWelcome to TIC-TAC Toe")

def refresh_screen():
    # os.system("cls")
    print_header()
    print(board)

def enter_move():
    choice = int(input(" Please choose 1-9. > "))
    if 1 <= choice <= 9:
        return choice
    else:
        raise ValueError("Bad move. Game over.\n")

def new_game() -> bool:
    option = input("Would you like to play again? (Y/N) > ").upper()
    if option == "Y":
        return True
    elif option == "N":
        print("Thanks for playing! See you.")
        return False
    else:
        raise ValueError("Bad selection. Good bye.")

while True:
    refresh_screen()

    #Gracz X
    print("\nX)", end="")
    x_choice = enter_move()
    board.update_cell(x_choice, "X")
    refresh_screen()

    if board.is_winner("X"):
        print("\nX wins!\n")
        if new_game() is True:
            board.reset()
            continue
        else:
            break

    #Sprawdzenie remisu
    if board.is_tie():
        print("\nTie game!\n")
        if new_game() is True:
            board.reset()
            continue
        else:
            break

    #Gracz O
    print("\nO)", end="")
    o_choice = enter_move()
    board.update_cell(o_choice, "O")

    if board.is_winner("O"):
        print("\nO wins!\n")
        if new_game() is True:
            board.reset()
            continue
        else:
            break

    #Sprawdzenie remisu
    if board.is_tie():
        print("\nTie game!\n")
        if new_game() is True:
            board.reset()
            continue
        else:
            break