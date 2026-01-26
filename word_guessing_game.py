import random
easy_words=['apple','train','tiger','bike']
medium_words=['html','css','planet','laptop']
hard_words=['elephant','diamond','umbrella','mountain']

print('Welcome to the password guessing game')
print('Choose the difficulty level')

level=input('Enter difficulty:').lower()
if level=='easy':
    secret=random.choice(easy_words)
elif level=='medium':
    secret=random.choice(medium_words)
elif level=='hard':
    secret=random.choice(hard_words)
else:
    print('Invalid choice.Defaulting it to easy level')
    secret=random.choice(easy_words)
    
attempts=0
print('\n Guess the secret password:')

while True:
    guess=input('enter your guess:').lower()
    attempts += 1
    
    if guess== secret:
        print(f'La badai cha!! You guessed in {attempts} attempt.')
        break
    
    hint = ''
    
    for i in range(len(secret)):
        if i < len(guess) and guess[i]== secret[i]:
            hint += guess[i]
        else:
            hint += "_"
            
    print("hint:",hint)
    
print("Game over ")
