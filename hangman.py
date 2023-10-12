import random

start_message = "Welcome to Hangman! The goal of the game is to complete the secret word by guessing letters. Each incorrect letter chosen will give you one strike. To begin, choose a difficulty: \n Easy - 10 strikes \n Medium - 8 strikes \n Hard - 6 strikes"

def gameStart():
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
    if answer == 'easy':
        strikes = 10
    elif answer == 'medium':
        strikes = 8
    elif answer == 'hard':
        strikes = 6
    else:
        return False
    return strikes
        
def gameRun(strikes, guess_count, guess_letters, word, hidden_word):
    guess_letters.sort()
    print(" ".join(hidden_word) + "  Strikes: " + str(guess_count) +  "  Guessed letters: " + ", ".join(guess_letters))
    if "_" in hidden_word and guess_count < strikes:
        answer = input('Enter a letter:')
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
    elif "_" not in hidden_word and guess_count < strikes:
        print("You win! Congratulations!")
        
print(start_message)
wordLibrary = ['amber', 'aromas', 'autumn', 'bonfire', 'bounty', 'brisk', 'carving', 'chestnuts', 'chilly', 'chili', 'cider', 'cinnamon', 'cornstalk', 'cornucopia', 'costume', 'cranberry', 'crisp', 'crunching', 'equinox', 'family', 'feast', 'festival', 'foliage', 'frosty', 'gathering', 'generous', 'ghost', 'ghoulish', 'goblin', 'golden', 'gourds', 'gravy', 'grandparents', 'halloween', 'harvest', 'haunted', 'hayride', 'holiday', 'inviting', 'kernel', 'maize', 'mummy', 'november', 'october', 'orchard', 'parade', 'plenty', 'pumpkin', 'raking', 'roasting', 'rustling', 'savory', 'scarecrow', 'season', 'september', 'spicy', 'sweater', 'thankful', 'thanksgiving', 'turkey', 'trail', 'vampire', 'vibrant', 'zombie']
gameStart()
