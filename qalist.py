import csv
import random

class QAPair:
    def __init__(self, question: str, answer: str) -> None:
        self.question = question
        self.answer = answer
    
    def fromCSV(line: str, answer: int = 0, question: int = 3) -> object:
        d = line[question].strip('"').strip('\\').replace("  ", " ")
        return QAPair(line[answer], d)

class QAList:
    def __init__(self, csv_file: str, answer_index: int = 0, question_index: int = 3) -> None:
        self.answer_index = answer_index
        self.question_index = question_index

        self.QAs = self.load_qa_list(csv_file)

        self.day = -1
        self.counter = 0

        self.random_indexes = [i for i in range(0, len(self.QAs))]
        random.shuffle(self.random_indexes)
    
    def load_qa_list(self, csv_file: str) -> list:
        QAs = []

        with open(csv_file, newline='') as csvfile:
            r = csv.reader(csvfile)

            try:
                for line in r:
                    QAs.append(QAPair.fromCSV(line, self.answer_index, self.question_index))
            except UnicodeDecodeError:
                pass
        
        return QAs

    def get_random_pair(self) -> QAPair:
        return random.choice(self.QAs)
    
    def get_todays_pair(self, day: int) -> QAPair:
        if not self.day == day:
            self.day = day
            self.counter += 1
        
        return self.QAs[self.random_indexes[self.counter]]