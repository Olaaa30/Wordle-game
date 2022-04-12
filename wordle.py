# Wordle
# Task: Make a Wordle game.
# Description: Wordle is a single player game, in which a user is required 
# to guess a 5-letter hidden word in 6 Attempts.
# *The user makes a first guess.( E.G: "Skate").
# * Print out a progress guide, like this. "√××√+",
# * "√" Indicates that the letter at that position was guessed correctly.
# * "+" indicates that the letter at that position is in the hidden word, but in a different position.
# *"×" indicates that the letter at that position is wrong, and isn't in the hidden word.
# *This process is repeated until the user either guesses the hidden word 
# correctly—in which case, he Wins!—, or exhausts his 6 Attempts, losing.
# *The "hidden word" is generated randomly from a list of 5-letter words hard-coded by you.
import random
class CreatePlayer:
    def __init__(self,name):
        self.name = name
        self.lives = 6
words = ['Abuse','Adult','Agent','Anger', 'Apple','Award','Basis'
'Beach','Birth','Block','Blood','Board','Brain','Bread','Break',
'Brown','Buyer','Cause','Chain','Chair','Chest','Chief','Child','China',
'Claim','Class','Clock','Coach','Coast','Court','Cover','Cream','Crime','Cross',
'Crowd','Crown','Cycle','Dance','Death','Depth','Doubt','Draft','Drama','Dream',
'Dress','Drink',"Drive",'Earth','Enemy','Entry','Error','Event','Faith','Fault',
'Field','Fight','Final','Floor','Focus','Force','Frame','Frank','Front','Fruit',
'Glass','Grant','Grass','Green','Group','Guide','Heart','Henry','Horse','Hotel',
'House','Image','Index','Input','Issue','Japan','Jones','Judge','Knife','Laura',
'Layer','Level','Lewis','Light','Limit','Lunch','Major','March','Match','Metal',
'Model','Money','Month','Motor','Mouth','Music','Night','Noise','North','Trust',
'Truth','Uncle','Union','Unity','Value','Video','Visit','Voice','Waste','Watch',
'Water','While','White','Whole','Woman','World','Youth']
def wordle():
    playername = input('What is your name? ')
    player = CreatePlayer(playername)
    word = words[random.randint(0,len(words))].lower()
    word_list = []
    for i in range(len(word)):
        word_list.append(word[i])
    
    while player.lives > 0:
        print(f'You have {player.lives} lives remaining')
        progress_list = ['','','','','']
        print('Guess a five-letter word: ')
        guess = input().lower()
        user_word_list = []
        if len(guess) > 5:
            print('Please check that your word has five letters ')
        for i in range(len(guess)):
            user_word_list.append(guess[i])
        
        for i in range(0,len(user_word_list)):
            if word_list[i] == user_word_list[i]:
                progress_list[i] = '√'
            elif user_word_list[i] in word_list:
                progress_list[i] = '+'
            else:    
                progress_list[i] = 'x'
        print(user_word_list)
        print(('').join(progress_list))
        player.lives -= 1
        if progress_list == ['√','√','√','√','√']:
            print('Print you have correctly guessed the word')
            break
    if player.lives == 0:
        print('Sorry, you ran out of lives.')
        print('The word was: ', word)

wordle()
