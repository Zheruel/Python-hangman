import requests
import random
from bs4 import BeautifulSoup
from typing import List


def getwords() -> List[str]:
    s = requests.session()
    response = s.get("https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/")

    soupcontent = BeautifulSoup(response.content, 'html.parser')
    element1 = soupcontent.find("h1", text="3000 most common words in English")
    scrapedwords: List[str] = element1.parent.find("div").find_all("p")[1].contents

    return scrapedwords[2::2]


def playhangman(guessword: str):
    tries: int = 6
    guessedletters: List[str] = []
    print(guessword, len(guessword))
    print("I have your word! It's {} letters long".format(len(guessword)), end="\n \n \n")

    while tries > 0:
        if  all(elem in  guessedletters for elem in guessword):
            break

        print("You have {} lives".format(tries))

        for letter in guessword:
            if guessedletters.__contains__(letter):
                print(letter, end=" ")

            else:
                print("_", end=" ")
        print("\n")

        choice = input("Do you want to guess the word? Enter to keep going 'yes' to try to guess: ")

        if choice == "yes":
            guess = input("Enter your guess: ")

            if guess != guessword:
                print("Wrong guess", end="\n\n")
                tries -= 1

                print(tries)
            else:
                break

        else:
            guessedletter = input("Enter your guess letter: ")

            while guessedletters.__contains__(guessedletter):
                print("Please enter a letter you haven't used before")
                guessedletter = input("Enter your guess letter: ")

            guessedletters.append(guessedletter)

            if not(guessword.__contains__(guessedletter)):
                print("Wrong guess", end="\n\n")
                tries -= 1

            else:
                print("Correct guess", end="\n\n")

    if tries == 0:
        print("You lose!", end="\n\n")
    else:
        print("You win!", end="\n\n")


if __name__ == '__main__':
    words: List[str] = getwords()

    while True:
        word: str = random.choice(words)
        playhangman(word.lower())
        
        # removes word from list so it doesn't repeat in the next round
        words.remove(word.lower())
