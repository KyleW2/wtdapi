from wordlist import WordList

class Game:
    def __init__(self, csv_file: str) -> None:
        self.words = WordList(csv_file)

    def run(self) -> None:
        word = self.words.get_random_word()
        print(f"The definition of the word is: {word.definition}")

        done = False
        guesses = 0
        while not done:
            guess = input(">> ")

            if guess.lower() == word.word.lower():
                print("Correct!")
                done = True
            else:
                self.difference(guess, word.word)
                guesses += 1
            
            if guesses == 10:
                print("You're out of guesses.")
                print(f"The word was {word.word}")
                done = True

    def difference(self, A: str, B: str) -> None:
        correct = 0
        for a, b in zip(A.lower(), B.lower()):
            if a == b:
                print(f"The letter {a} is correct!")
                correct += 1
        
        if correct == 0:
            print("None of the letters in your guess were correct.")

if __name__ == "__main__":
    gamer = Game("words.csv")

    gamer.run()