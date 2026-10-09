board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6: print("---------")

def check_win(p):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in wins)

def minimax(is_max):
    if check_win("O"): return 1
    if check_win("X"): return -1
    if " " not in board: return 0
    best = -100 if is_max else 100
    for i in range(9):
        if board[i]==" ":
            board[i]="O" if is_max else "X"
            score = minimax(not is_max)
            board[i]=" "
            best = max(best, score) if is_max else min(best, score)
    return best

def best_move():
    best_score = -100
    move = 0
    for i in range(9):
        if board[i]==" ":
            board[i]="O"
            score = minimax(False)
            board[i]=" "
            if score > best_score:
                best_score = score
                move = i
    board[move]="O"

print("Tic-Tac-Toe: Aap X ho, AI O hai")
print_board()
while True:
    x = int(input("Aap ki baari (0-8): "))
    if board[x]!=" ": continue
    board[x]="X"
    if check_win("X"): print("Aap jeet gaye!"); break
    if " " not in board: print("Draw!"); break
    best_move()
    print_board()
    if check_win("O"): print("AI jeet gaya! AI kabhi nahi haarta!"); break
    if " " not in board: print("Draw!"); break
