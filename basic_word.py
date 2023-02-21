
class BasicWord():
    counter = 0
    set_of_words = []
    word = ''
    def __init__(self, word, set_of_words, counter):
        self.word = word
        self.set_of_words = set_of_words
        self.counter = counter
    def if_word_in_set(self):
        if self.word in self.set_of_word:
            return True
        return False
    def set_of_words_counter(self, counter):
        if self.if_word_in_set:
            counter += 1

    class BasicWord:
        def __init__(self, word, valid_word_array):
            self.word = word
            self.valid_word_array = valid_word_array

        def chek_word_in_valid_array(self):
            """Проверить, что такое слово есть для угадывания"""
            if self.word in self.set_of_word:
                return True
            return False
        def __repr__(self):
            return f"{self.word} - слово из которого надо составить слова\n" \
                   f"{self.valid_word_array} - набор допустимых подслов"

        def count_subword(self):
            вернуть
            кол - во
            слов, которое
            надо
            отгадать
    def __repr__(self):
        return f'Podobrali {self.counter} slov)'





