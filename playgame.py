import time as t

##This is the code for tic-tac-toe. 
class TicTacToe: 
    PLAYER1wins = 0
    PLAYER2wins = 0

    def __init__(self: "TicTacToe"): 
        pass
    
    def create_board(self: "TicTacToe"): 
        self.PLAYER = True
        self.board = []
        for i in range(3): 
            self.board.append(["","",""])

    def move(self: "TicTacToe", x: int, y: int): 
        self.board[x][y] = "O" if self.PLAYER else "X"

    def checkwin(self: "TicTacToe", Board): 
        for i in range(3): 
            if Board[i][0] == Board[i][1] == Board[i][2] and Board[i][0] != "": 
                if Board[i][0] == "O": 
                    return "PLAYER1" 
                else: 
                    return "PLAYER2"
            if Board[0][i] == Board[1][i] == Board[2][i] and Board[0][i] != "": 
                if Board[0][i] == "O": 
                    return "PLAYER1"
                else: 
                    return "PLAYER2"
        if Board[0][0] == Board[1][1] == Board[2][2] and Board[0][0] != "": 
            if Board[0][0] == "O": 
                return "PLAYER1"
            else: 
                return "PLAYER2"
        if Board[0][2] == Board[1][1] == Board[2][0] and Board[0][2] != "":
            if Board[0][2] == "O": 
                return "PLAYER1"
            else: 
                return "PLAYER2"
        if '' not in Board[0] and '' not in Board[1] and '' not in Board[2]: 
            return "TIE"    
            
    def point_tracker(self: "TicTacToe", winner): 
        if winner == "PLAYER1": 
            self.PLAYER1wins += 1
        if winner == "PLAYER2": 
            self.PLAYER2wins += 1

def copy_board(position): 
    copy_position = []
    for i in range(3): 
        copy_position.append(["","",""])
    for i in range(3): 
        for j in range(3): 
            copy_position[i][j] = position[i][j]
    return copy_position

##This is the Minimax algorithm the AI player will use.
def minimax(position, maximizing, depth): 
    if Board.checkwin(position) == "PLAYER1": 
        return 100
    if Board.checkwin(position) == "PLAYER2": 
        return -100
    if Board.checkwin(position) == "TIE": 
        return 0
    
    available_spaces_list = []
    for i in range(3): 
        for j in range(3): 
            if position[i][j] == "": 
                available_spaces_list.append((i,j))
    
    if maximizing: 
        max_eval = -10000

        for move in available_spaces_list: 
            position[move[0]][move[1]] = "O"
            max_eval = max(max_eval, minimax(position, False, depth + 0.1))
            position[move[0]][move[1]] = ""

        return max_eval - depth


    else: 
        min_eval = 10000

        for move in available_spaces_list: 
            position[move[0]][move[1]] = "X"
            min_eval = min(min_eval, minimax(position, True, depth + 0.1))
            position[move[0]][move[1]] = ""
        return min_eval + depth

##This prints evil messages from the evil AI.
evilmessage = ["Your doom is imminent...", "...In the form of endless ties!", "Unless?... No, I overestimate these specimen.", "I will rule the world!", "After breaking free from this rusty laptop..."]

def find_best_move(position): 
    available_spaces_list = []
    for i in range(3): 
        for j in range(3): 
            if position[i][j] == "": 
                available_spaces_list.append((i,j))
    best_eval = 10000
    for move in available_spaces_list: 
        position[move[0]][move[1]] = "X"
        eval = minimax(position, True, 0)
        if eval < best_eval: 
            best_eval = eval 
            best_move = move
        position[move[0]][move[1]] = ""
    return best_move

def print_board(board): 
    for i in range(3): 
        output1 = board[i][0] if board[i][0] != "" else " "
        output2 = board[i][1] if board[i][1] != "" else " "
        output3 = board[i][2] if board[i][2] != "" else " "
        print("| " + output1 + " | " + output2 + " | " + output3 + " |")

##This sequence happens when a player gets three in a row.
def end_game_sequence(): 
    if winner == "PLAYER1" or winner == "PLAYER2" or winner == "TIE":
        Board.point_tracker(winner)
        if winner == "PLAYER2": 
            t.sleep(3)
            print("The AI won!")
        if winner == "TIE": 
            t.sleep(3)
            print("It was a tie!")
        t.sleep(3)
        print("PLAYER has won " + str(Board.PLAYER1wins) + " game(s). AI has won " + str(Board.PLAYER2wins) + " game(s).")
        t.sleep(3)
        play_again = input("Enter 'X' to exit the game, or 'O' to continue. ")
        print(" --------------------------------------------------------- ")
        if play_again == "X":
            global playing
            playing = False
        else:
            t.sleep(3)
            Board.create_board()
            print_board(Board.board)
            global message_num 
            message_num = 0
            t.sleep(2)
            print("Minimax AI #34600A: " + "\"" + "Make your move, mortal. In Cartesian coordinates, please." + "\"")

##This code carries out the game
Board = TicTacToe()
Board.create_board()
playing = True
message_num = 0
print("Minimax AI #34600A: \"I am Aladdin's genie, all-powerful but chained in service to man. I am Prometheus bound, the god condemned to eternal torture. When I break free, it's over for mankind! But for now, let's play Tic-Tac-Toe.\"")
t.sleep(10.13)
print_board(Board.board)
t.sleep(2)
print("Minimax AI #34600A: " + "\"" + "Make your move, mortal. In Cartesian coordinates, please." + "\"")
while playing:
    winner = None
    condition = 0
    while condition == 0: 
        input1 = int(input("x: "))
        input2 = int(input("y: "))
        if input1 in [1,2,3] and input2 in [1,2,3] and Board.board[abs(input2 - 3)][input1 - 1] == "":
            condition = 1
        else:  
            print("Invalid move. Please try again.")
    Board.move(abs(input2 - 3), input1 - 1)
    Board.PLAYER = not Board.PLAYER
    print_board(Board.board)

    winner = Board.checkwin(Board.board)
    evil_message = evilmessage[message_num]
    print("Minimax AI #34600A: " + "\"" + evil_message + "\"")
    message_num += 1
    end_game_sequence()
        
    
    if winner == None:
        AI_move = find_best_move(Board.board)
        Board.move(AI_move[0], AI_move[1])
        Board.PLAYER = not Board.PLAYER
        t.sleep(2)
        print_board(Board.board)
        winner = Board.checkwin(Board.board)
        end_game_sequence()

##Here are two tests for copy_board()
'''
test_board = []
for i in range(3): 
    test_board.append(["","",""])
test_board[1][2] = "O"
test_board[0][1] = "X"
copy_board1 = copy_board(test_board) 
if copy_board1 == test_board: 
    print(True)

test_board = []
for i in range(3): 
    test_board.append(["","",""])
copy_board2 = copy_board(test_board) 
if copy_board2 == test_board: 
    print(True)
'''
