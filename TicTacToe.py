class Tic_Tac_Toe:

    def __init__(self):
        self.field=[]
        for row in range(3):
            r = []
            for col in range(3):
                r.append('-')
            self.field.append(r)
        self.move_x = True
        self.end_game = False
        self.winner = None
        self.win = ' '
        self.first_move = True

    def new_game(self):
        self.field = []
        for row in range(3):
            r = []
            for col in range(3):
                r.append('-')
            self.fieled.append(r)
        self.field.append(r)
        self.move_x = True
        self.end_game = False
        self.winner = None
        self.win = ' '
        self.first_move = True

    def get_field(self):
        return self.field

    def check_field(self):
        if self.win == 'ничья':
            return 'D'
        elif self.win == 'X':
            return 'X'
        elif self.win == 'O':
            return 'O' 
        else: return None

    def make_move(self,row,col):
        if self.end_game and not self.first_move:
            return 'игра завершена'
        else: 
            if self.field[row-1][col-1] != '-':
                return f'Клетка {row},{col} занята'
            else:
                if self.move_x:
                    self.field[row-1][col-1]='X'
                    self.move_x=False
                    self.first_move =False
                else:
                    self.field[row-1][col-1]='O'
                    self.move_x = True
                    self.first_move = False
                for row in range(len(self.field)):
                    if self.field[row].count(self.field[row][0])==3 and self.field[row][0]!='-':
                        self.end_game = True
                        self.win = self.field[row][0]
                        return f'Выйграл игрок {self.field[row][0]}'
                    elif self.field[0].count('-')==3 and self.field[1].count('-')==3 and self.field[2].count('-')==3:
                        self.end_game = True
                        self.win = 'ничья'
                        return 'ничья'
                    for col in range(len(self.field)):
                        if self.field[row][col]== self.field[col][col]==self.field[2][col] and self.field[row][col]!= '-':
                            self.end_game = True
                            self.win=self.field[row][col]
                            return f'выйграл игрок {self.field[row][col]}'
                        elif self.field[row][col] == self.field[1][1]== self.field[2][2] and self.field[row][col]!='-' or self.field[row][2]==self.field[1][1]==self.field[2][row] and self.field[row][2]!='-':
                            self.end_game = True
                            self.win = self.field[1][1]
                            return f'выйграл Игрок {self.field[1][1]}'
                    else:
                        return 'продолжить игру'

            
