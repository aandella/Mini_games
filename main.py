
class Player():
    """Класс Player создает игроков

    Attributes
    ----------
    position : str
        сторона за которую играет игрок

    Methods
    -------
    make_move(x1, x2)
        позволяет игроку сделать ход на выбранную клетку и сообщает если ход привел к победе

    is_your_move()
        проверяет является ли очередь игрока ходить
    """
    def __init__(self, position, game):
        self.game = game
        self.position = position
        self.game.positions.remove(position)


    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if position in self.game.positions:
            self._position = position
        else:
            raise ValueError("Игрок может играть только за X или Y. Если вы ввели верную букву, возможно она занята, попробуйте другую")

    def make_move(self, x1, x2):
        if self.is_your_move():
            if self.game.pole[x1][x2] == ' ':
                self.game.pole[x1][x2] = self._position
                if self.game.is_winning():
                    print(f"Поздравляю! Выиграл {self._position}")
            else:
                print(f"Это поле уже занято, пожалуйста, выберите другое")
        else:
            print("Cейчас ход другого игрока")

    def is_your_move(self):
        if self.game._last_move != self._position:
            self.game._last_move = self._position
            return True
        return False


class Game():
    '''
    Cоздает
    '''
    def __init__(self, positions=None):
        if positions is None:
            self.positions = ['X', 'Y']
        self.pole = [[' ' for _ in range(3)] for _ in range(3)]
        self._last_move = None



    def show_pole(self):
        for i in self.pole:
            print(i)

    def is_winning(self):
        if self.pole[0][0] != ' ':
            if self.pole[0][0] == self.pole[1][1] == self.pole[2][2]:
                return True
            if self.pole[0][0] == self.pole[1][0] == self.pole[2][0]:
                return True
            if self.pole[0][0] == self.pole[0][1] == self.pole[0][2]:
                return True

        if self.pole[1][1] != ' ':
            if self.pole[0][1] == self.pole[1][1] == self.pole[2][1]:
                return True
            if self.pole[1][0] == self.pole[1][1] == self.pole[1][2]:
                return True
            if self.pole[2][0] == self.pole[1][1] == self.pole[0][2]:
                return True

        if self.pole[2][2] != ' ':
            if self.pole[2][0] == self.pole[2][1] == self.pole[2][2]:
                return True
            if self.pole[0][2] == self.pole[1][2] == self.pole[2][2]:
                return True

        return False

    def next_move(self):
        if self._last_move == 'X':
            self._last_move = 'Y'
        else:
            self._last_move = 'X'


