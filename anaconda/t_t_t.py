board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    global board
    board2 = []
    for row in board:
        board2.append('|'.join(row))
    board3 = '\n-----\n'.join(board2)
    print(board3)

def is_draw():
    global board
    for row in board:
        if ' ' in row:
            return False
    return True

def is_game_over():
    global board
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return False

def dfs(player):
    global board
    winner = is_game_over()
    if winner:
        if winner == 'X':
            return {'score': 1}
        else:
            return {'score': -1}
    elif is_draw():
        return {'score': 0}

    if player == 'X':
        best = {'score': -float('inf')}
    else:
        best = {'score': float('inf')}

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                score = dfs('O' if player == 'X' else 'X')
                board[i][j] = ' '
                score['row'] = i
                score['col'] = j

                if player == 'X' and score['score'] > best['score'] or player == 'O' and score['score'] < best['score']:
                        best = score
    return best

def play():
    player = 'X'
    while True:
        print_board()
        winner = is_game_over()
        if winner:
            print(winner, " wins!")
            break
        if is_draw():
            print("Draw!")
            break
        if player == 'X':
            best_move = dfs('X')
            board[best_move['row']][best_move['col']] = 'X'
            print('-'*20)
        else:
            while True:
                row = int(input("Row number: "))
                col = int(input("Column number: "))
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    break
                else:
                    print("Invalid move. Try again.")
            print('-'*20)
        player = 'O' if player == 'X' else 'X'
    print("Game Over.")

play()
