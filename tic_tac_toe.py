import sys
b_values={'TL':' ','TM':' ','TR':' ',
    'CL':' ','CM':' ','CR':' ',
    'BL':' ','BM':' ','BR':' '}

#print"s tic tac toe board
def board(b_values):
    print(b_values['TL']+'|'+b_values['TM']+'|'+b_values['TR'])
    print('-+-+-')
    print(b_values['CL']+'|'+b_values['CM']+'|'+b_values['CR'])
    print('-+-+-')
    print(b_values['BL']+'|'+b_values['BM']+'|'+b_values['BR'])


player1=str(input("Player name of X: "))
player2=str(input("Player name of O: "))
players={player1:'X',player2:'O'}

def winner(win):
    if (win['TL']==win['TM']==win['TR']=='X' or win['CL']==win['CM']==win['CR']=='X' or win['BL']==win['BM']==win['BR']=='X' or
    win['TL']==win['CL']==win['BL']=='X' or win['TM']==win['CM']==win['BM']=='X' or win['TR']==win['CR']==win['BR']=='X' or 
    win['TR']==win['CM']==win['BL']=='X' or win['TL']==win['CM']==win['BR']=='X'):
        return "p1"
    if (win['TL']==win['TM']==win['TR']=='O' or win['CL']==win['CM']==win['CR']=='O' or win['BL']==win['BM']==win['BR']=='O' or
    win['TL']==win['CL']==win['BL']=='O' or win['TM']==win['CM']==win['BM']=='O' or win['TR']==win['CR']==win['BR']=='O' or 
    win['TR']==win['CM']==win['BL']=='O' or win['TL']==win['CM']==win['BR']=='O'):
        return "p2"
    

w=''
turn=players[player1]
for i in range(1,len(b_values)+1):
    board(b_values)
    if turn=='X':
        move=str(input(f"{player1}'s Move: "))
    else:
        move=str(input(f"{player2}'s Move: "))
    b_values[move]=turn
    w=winner(b_values)
    if w=="p1":
        board(b_values)
        print(f"{player1} won")
        sys.exit(0)
    if w=="p2":
        board(b_values)
        print(f"{player2} won")
        sys.exit(0)
    if turn=='X':
        turn=players[player2]
    else:
        turn=players[player1]

print(board(b_values))