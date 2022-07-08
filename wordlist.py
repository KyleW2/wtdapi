import csv
import random

class Word:
    def __init__(self, word: str, definition: str) -> None:
        self.word = word
        self.definition = definition
    
    def fromCSV(line: str, word_index: int = 0, def_index: int = 3) -> object:
        d = line[def_index].strip('"').strip('\\').replace("  ", " ")
        return Word(line[word_index], d)

class WordList:
    def __init__(self, csv_file: str) -> None:
        self.words = self.load_word_list(csv_file)

        self.day = -1
        self.counter = 0

        self.random_indexes = [i for i in range(0, len(self.words))]
        random.shuffle(self.random_indexes)
    
    def load_word_list(self, csv_file: str) -> list:
        words = []

        with open(csv_file, newline='') as csvfile:
            r = csv.reader(csvfile)

            for line in r:
                words.append(Word.fromCSV(line))
        
        return words

    def get_random_word(self) -> Word:
        return random.choice(self.words)
    
    def get_todays_word(self, day: int) -> Word:
        if not self.day == day:
            self.day = day
            self.counter += 1
        
        return self.words[self.random_indexes[self.counter]]

if __name__ == "__main__":
    test = WordList("words.csv")

    print(test.get_random_word().definition)