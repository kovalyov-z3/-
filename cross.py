print("*"*30 + " Крестики Нолики "+ "*"*30)

board = []
steps = {}
win_cords = ((1,2,3), (1,5,9), (1,4,7), (2,5,8,), (3,6,9), (3,5,7), (4,5,6), (7,8,9))
for i in range(1,10):
    steps[i] = ""

for i in range(1,10):
    board.append(i)
    

def draw_board(board):
    print("-"*13)
    for i in range(0, len(board), 3):
        print("|",board[i], "|", board[i+1], "|",  board[i+2], "|")
        print("-"*13)
    
draw_board(board)

def make_choise(PlayerNumber):
    if (PlayerNumber == 1):
        
        step = input("Куда ставим X? ")

        try:
            step = int(step)
            steps[step] = "X"
            board[step-1] = "X"
            
        except:
            step = input("Некорректный ввод!")

    if (PlayerNumber == 2):
        
        step = input("Куда ставим O? ")

        try:
            step = int(step)
            steps[step] = "O"
            board[step-1] = "O"
            
        except:
            step = input("Некорректный ввод!")

def check_win(steps):
    for i in win_cords:
        
        if((steps[i[0]] == steps[i[1]] == steps[i[2]]) and (steps[i[0]] != '') and (steps[i[1]] != '') and (steps[i[2]] != '')):
            return True
    return False
            

IsWin = False
counter = 0
while(not IsWin):
    if(counter % 2 == 0):
        make_choise(1)
        counter += 1
        draw_board(board)
    else:
        make_choise(2)
        counter += 1
        draw_board(board)
    if (counter > 4):
        if(check_win(steps)):
            if(counter%2 == 0):
                print("Победил Второй Игрок!")
            if(counter%2 != 0):
                print("победил Первый Игрок!")
            break
    if (counter >= 9):
        print('ничья!')
        break
    
