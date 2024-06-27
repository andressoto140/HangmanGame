from hangman import Hangman

#Welcome the user
print("Welcome to Florida Hangman: Guess the City edition! ")

#create your word bank using a list
word_bank = ["Orlando", "Miami", "Jacksonville", "Sarasota", "Tampa",
             "Tallahassee", "Naples", "Cleawater",
             "Hollywood", "Largo", "Venice"]

#create new instance
hangman = Hangman(word_bank)

#function to start the game
hangman.play()

