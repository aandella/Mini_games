class Game():
    def __init__(self, word, letters=None):
        if letters is None:
            self.letters = []
        self.word = word
        self.life = 6
        self.underscore_word = '_' * len(self._word)
        self.hangman = [

            """
              _______
             |/      
             |        
             |        
             |       
             |      
             |
            _|___
            """,

            """
              _______
             |/      |
             |      (_)
             |        
             |       
             |      
             |
            _|___
            """,

            """
              _______
             |/      |
             |      (_)
             |       |
             |       |
             |      
             |
            _|___
            """,

            """
              _______
             |/      |
             |      (_)
             |      /|
             |       |
             |      
             |
            _|___
            """,

            """
              _______
             |/      |
             |      (_)
             |      /|\\
             |       |
             |      
             |
            _|___
            """,

            """
              _______
             |/      |
             |      (_)
             |      /|\\
             |       |
             |      / \\
             |
            _|___
            """
        ]

    def print_hangman(self):
        print(self.hangman[abs(self.life - 6)])

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, new_word):
        if len(new_word) > 1 and new_word.isalpha():
            self._word = new_word
        else:
            raise ValueError("Введенное слово некорректно")

    def start_game(self):
        symbol = self.word_end()
        for i in range(30):
            print()
        print(f'В веденном слове {len(self._word)} {symbol}')
        print(self.underscore_word)
        while self.life > 0 and not self.is_winning():
            self.player_move()

    def word_end(self):
        match len(self._word):
            case [1, 21, 31, 41, 51, 61, 71, 81, 91]:
                return 'символ'
            case [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 52, 53, 54, 62, 63, 64, \
                  72, 73, 74, 82, 83, 84, 92, 93, 94]:
                return 'символа'
            case _:
                return 'символов'

    def player_move(self):
        print()
        print(f'Использованные буквы: {self.letters}')
        letter = input("Введите букву: ")
        self.letter = letter
        self.letters.append(self._letter)
        if self._letter in self._word:
            print("Вы угадали!")
            self.replace_letter(self._letter)
            print()
            print(self.underscore_word)

        else:
            print()
            print('Вы не угадали')
            self.print_hangman()
            self.life = self.life - 1
            print(f'Оставшиеся жизни - {self.life}')
            if self.life == 0:
                print('Вы проиграли!')

    def is_winning(self):
        return self.underscore_word == self._word

    @property
    def letter(self):
        return self._letter

    @letter.setter
    def letter(self, new_letter):
        if len(new_letter) == 1 and new_letter.isalpha():
            self._letter = new_letter
        else:
            raise ValueError("Введен некорректный символ")

    def replace_letter(self, letter):
        start = 0
        for i in range(self._word.count(letter)):
            letter_index = self._word[start:].index(letter) + len(self._word[:start])

            start = self._word[start:].index(letter) + 1
            self.underscore_word = self.underscore_word[:letter_index] + letter + self.underscore_word[
                                                                                  letter_index + 1:]


word = input("Введите загаданное слово: ")
new_game = Game(word)
new_game.start_game()
