class Game():
    """Управляет игровой сессией крестиков-ноликов.

    Содержит игровое поле, отслеживает состояние игры и
    управляет очередностью ходов игроков.

    Attributes
    ----------
    free_positions : list
        Список доступных символов для выбора игроками
    pole : list
        Двумерный список 3x3, представляющий игровое поле
    _last_move : str or None
        Символ последнего игрока, сделавшего ход

    Methods
    -------
    show_pole()
        Отображает текущее состояние игрового поля
    is_winning()
        Проверяет наличие выигрышной комбинации на поле
    next_move()
        Определяет и устанавливает следующего игрока для хода
    """

    def __init__(self):
        """Инициализирует новую игровую сессию с пустым полем."""
        self.free_positions = ['X', 'Y']
        self.pole = [[' ' for _ in range(3)] for _ in range(3)]
        self._last_move = None

    def show_pole(self) -> None:
        """Выводит текущее состояние игрового поля в консоль.

        Отображает все строки игрового поля с текущими ходами игроков.
        """
        for i in self.pole:
            print(i)

    def is_winning(self) -> bool:
        """Проверяет наличие выигрышной комбинации на игровом поле.

        Проверяет все возможные линии: горизонтали, вертикали и диагонали.

        Returns:
            bool: True если обнаружена выигрышная комбинация, иначе False
        """
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

    def next_move(self) -> None:
        """Переключает очередь хода на следующего игрока."""
        if self._last_move == 'X':
            self._last_move = 'Y'
        else:
            self._last_move = 'X'


class Player():
    """Представляет игрока в игре крестики-нолики.

    Каждый экземпляр игрока связан с конкретной игровой сессией
    и играет за определенный символ (X или Y).

    Attributes
    ----------
    position : str
        Символ, за который играет игрок ('X' или 'Y')
    game : Game
        Ссылка на объект игры, к которой привязан игрок

    Methods
    -------
    make_move(x1, x2)
        Позволяет игроку сделать ход на выбранную клетку
    is_your_move()
        Проверяет, очередь ли текущего игрока делать ход
    """

    def __init__(self, position: str, game):
        """Инициализирует нового игрока.

        Args:
            position (str): Символ игрока ('X' или 'Y')
            game (Game): Объект игры, к которой присоединяется игрок
        """
        self.game = game
        self.position = position
        self.game.free_positions.remove(position)

    @property
    def position(self) -> str:
        """str: Символ игрока ('X' или 'Y')."""
        return self._position

    @position.setter
    def position(self, position: str) -> None:
        """Устанавливает символ игрока с валидацией.

        Args:
            position (str): Символ игрока ('X' или 'Y')

        Raises:
            ValueError: Если символ недоступен для выбора
        """
        if position in self.game.free_positions:
            self._position = position
        else:
            raise ValueError(
                "Игрок может играть только за X или Y. Если вы ввели верную букву, возможно она занята, попробуйте другую")

    def make_move(self, x1: int, x2: int) -> None:
        """Совершает ход игрока на указанные координаты.

        Проверяет возможность хода, обновляет игровое поле и
        проверяет, привел ли ход к победе.

        Args:
            x1 (int): Координата строки (0-2)
            x2 (int): Координата столбца (0-2)

        Notes:
            Выводит сообщения в консоль о результате хода
        """
        if self.is_your_move():
            if self.game.pole[x1][x2] == ' ':
                self.game.pole[x1][x2] = self._position
                if self.game.is_winning():
                    print(f"Поздравляю! Выиграл {self._position}")
            else:
                print(f"Это поле уже занято, пожалуйста, выберите другое")
        else:
            print("Cейчас ход другого игрока")

    def is_your_move(self) -> bool:
        """Проверяет, может ли игрок сделать ход в текущий момент.

        Returns:
            bool: True если сейчас очередь хода этого игрока, иначе False
        """
        if self.game._last_move != self._position:
            self.game._last_move = self._position
            return True
        return False
