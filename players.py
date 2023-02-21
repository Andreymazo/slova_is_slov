class Player():
    def __init__(self, name, used_words):
        self.name = name
        self.used_words = used_words

    def __repr__(self):
        return f'Podobrali {self.counter} slov)'


class Player:
    def __init__(self, name, used_words: set):
        self.name = name
        self.used_words = used_words if used_words else set()

    def word_count(self):
        Вернуть кол-во слов которое было отгадано

    def add_word(self, word):
        добавить к нашему used_words отгаданное слово

    def word_repeat_yes_or_no(self, word):
        проверить на повтор отгаданного слова

    def __repr__(self):
        return f"Игрок с именем {self.name}"

