import random
import os

start_message = "Welcome to Hangman! The goal of the game is to complete the secret word by guessing letters. Each incorrect letter chosen will give you one strike. To begin, choose a difficulty: \n Easy - 12 strikes \n Medium - 10 strikes \n Hard - 8 strikes"

def gameStart():
    clear()
    print(start_message)
    strikes = gameDifficulty()
    if strikes == False:
        print("Invalid difficulty. Please enter Easy, Medium, or Hard")
        gameStart()
    else:
        guess_count = 0
        guess_letters = []
        word = random.choice(wordLibrary)
        word = [*word]
        hidden_word = []
        for char in word:
            hidden_word.append('_')
        gameRun(strikes, guess_count, guess_letters, word, hidden_word)
              
def gameDifficulty():
    answer = input()
    answer = answer.lower()
    if answer == 'easy' or answer == 'e':
        strikes = 12
    elif answer == 'medium' or answer == 'm':
        strikes = 10
    elif answer == 'hard' or answer == 'h':
        strikes = 8
    else:
        return False
    return strikes
        
def gameRun(strikes, guess_count, guess_letters, word, hidden_word):
    guess_letters.sort()
    print(" ".join(hidden_word) + "  Strikes: " + str(guess_count) +  "  Guesses: " + ", ".join(guess_letters))
    if "_" in hidden_word and guess_count < strikes:
        answer = input('Enter a letter:')
        answer = answer.lower()
        if len(answer) == 1 and answer.isalpha() and answer not in guess_letters:
            guess_letters.append(answer)
            if answer in word:
                count = 0
                for char in word:
                    if char == answer:
                        hidden_word[count] = answer
                    count += 1        
            else:
                guess_count += 1
            gameRun(strikes, guess_count, guess_letters, word, hidden_word)
        elif len(answer) == 1 and answer.isalpha() and answer in guess_letters:
            print("Letter already guessed.")
            gameRun(strikes, guess_count, guess_letters, word, hidden_word)
        else:
            print("Invalid guess - must be a single letter. Please try again.")
            gameRun(strikes, guess_count, guess_letters, word, hidden_word)
    elif "_" in hidden_word and guess_count == strikes:
        print("You've reached " + str(strikes) + " strikes. Game over!")
        print("The word was '" + "".join(word) + "'")
        print("Hit Enter to play again!")
        input()
        print(start_message)
        gameStart()
        return
    elif "_" not in hidden_word and guess_count < strikes:
        print("You win! Congratulations!")
        print("Hit Enter to play again!")
        input()
        print(start_message)
        gameStart()
        return

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
        
wordLibrary = ['amber', 'aromas', 'autumn', 'blood', 'bonfire', 'bounty', 'brisk', 'broomstick', 'candle', 'candy', 'carving', 'chestnuts', 'chili', 'chilly', 'cider', 'cinnamon', 'cornstalk', 'cornucopia', 'costume', 'cranberry', 'creepy', 'crisp', 'crunching', 'disguise', 'equinox', 'family', 'fangs', 'feast', 'festival', 'foliage', 'frosty', 'gathering', 'generous', 'ghost', 'ghoulish', 'goblin', 'golden', 'gourds', 'grandparents', 'graveyard', 'gravy', 'halloween', 'harvest', 'haunted', 'hayride', 'holiday', 'inviting', 'kernel', 'maize', 'monster', 'mummy', 'november', 'october', 'orchard', 'parade', 'party', 'pirate', 'plenty', 'prince', 'princess', 'pumpkin', 'raking', 'roasting', 'rustling', 'savory', 'scarecrow', 'scary', 'season', 'september', 'skeleton', 'skull', 'slimy', 'spicy', 'spooky', 'sweater', 'thankful', 'thanksgiving', 'trail', 'turkey', 'vampire', 'vibrant', 'werewolf', 'wicked', 'witch', 'zombie']
gameStart()