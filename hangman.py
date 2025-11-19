


class Game():
    def __init__(self, word, letters = None):
        if letters is None:
            self.letters = []
        self.word = word
        self.user_try = 0
        self.life = 6
        self.underscore_word = '_' * len(self._word)


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
        for i in range(15):
            print('*')
        print(f'В веденном слове {len(self._word)} символов')
        print(self.underscore_word)
        while self.life > 0:
            self.player_move()

    @staticmethod
    def word_end():
        pass

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
            self.life = self.life - 1
            print(f'Оставшиеся жизни - {self.life}')
            if self.life == 0:
                print('Вы проиграли!')

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
            print(self._word[start:].index(letter))
            start = self._word[start:].index(letter)
            self.underscore_word = self.underscore_word[:letter_index] + letter + self.underscore_word[letter_index + 1:]



word = input("Введите загаданное слово: ")
new_game = Game(word)
new_game.start_game()