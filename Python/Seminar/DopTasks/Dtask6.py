""" 
Игра "Крестики-нолики": Реализуйте классическую игру "Крестики-нолики" для двух игроков

"""

# mas = [[" + ", "  ", "   "], ["    ", "        ", "   "], ["      ", "   ", "  "]]
# def print_mas():
#     for i in mas: 
#         print(' '.join(list(map(str, i))))
#     print()


# def my_function(input, idx1, idx2):
#     mas[idx1][idx2] = input

# while True:
#             if ((mas[0][0] == mas[1][1] == mas[2][2]) or (mas[0][0] == mas[0][1] == mas[0][2]) or (mas[0][0] == mas[1][0] == mas[2][0])
#                 or (mas[0][1] == mas[1][1] == mas[2][1]) or (mas[1][0] == mas[1][1] == mas[1][2]) or (mas[2][0] == mas[2][1] == mas[2][2])
#                 or (mas[0][2] == mas[1][1] == mas[2][0]) or (mas[0][1] == mas[1][1] == mas[2][1]) or (mas[0][2] == mas[1][2] == mas[2][2])):
#                 print("Победа")
#                 break
#             elif "+" in mas == False: 
#                 print("Ничья")
#                 break                
#             else:    #try:
#                 player_name = int(input("Введите номер игрока (1 или 2): "))
#                 if player_name == 1:
#                     idx1 = int(input("Игрок 1. Введите номер строки, куда хотите поставить 'X': ")) - 1
#                     idx2 = int(input("Игрок 1. Введите номер столбца, куда хотите поставить 'X': ")) - 1
#                     my_function('X', idx1, idx2)
#                     print_mas()
#                     #break
#                 elif player_name == 2:
#                     idx1 = int(input("Игрок 2. Введите номер строки, куда хотите поставить 'O': ")) - 1
#                     idx2 = int(input("Игрок 2. Введите номер столбца, куда хотите поставить 'O': ")) - 1
#                     my_function('O', idx1, idx2)
#                     print_mas()
#                     #break
                
class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def play_game(self):
        while True:
            self.print_board()
            print(f"Ход игрока {self.current_player}")
            row = int(input("Введите номер строки (1, 2, 3): ")) - 1
            col = int(input("Введите номер столбца (1, 2, 3): ")) - 1

            if self.make_move(row, col):
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    print(f"Игрок {winner} выиграл!")
                    break
                self.switch_player()
            else:
                print("Недопустимый ход. Попробуйте еще раз.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()

    