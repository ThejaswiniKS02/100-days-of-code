import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
list1=['advert','qwerty','poland','ant','baboon','badger','bat','bear','beaver','camel','cat','clam','cobra','cougar',
         'coyote','crow','deer','dog','donkey','duck','eagle','ferret','fox','frog','goat',
         'goose','hawk','lion','lizard','llama','mole','monkey','moose','mouse','mule','newt',
         'otter','owl','panda','parrot','pigeon','python','rabbit','ram','rat','raven',
         'rhino','salmon','seal','shark','sheep','skunk','sloth','snake','spider',
         'stork','swan','tiger','toad','trout','turkey','turtle','weasel','whale','wolf',
         'wombat','zebra']
chosen_word=random.choice(list1)
lives=0
a=print(f"Your choice is {chosen_word}.\n")
display=[]
for _ in range(len(chosen_word)):
    display += "_"
print(*display,sep='  ')
end_of_game = False
while not end_of_game:
    guess= input("Guess a letter.\n")
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(*display,sep='  ')
    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word. You lose a life\n")
        lives+=1
        if lives==6:
            end_of_game=True
            print("You lose...")
        print(stages[lives])
    if '_' not in display:
        end_of_game=True
        print("You win...")
    


