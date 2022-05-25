
#1
import random

print("Welcome to the number guessing Game! \nI'm thinking of a number between 1 and 100.")
difficulty_type=input("Choose a difficulty. Type 'easy' or 'hard': ")
#2
list=[]
for i in range(1,101):
  list.append(i)
#3
number = random.choice(list)
#4
live=0
def difficulty(difficulty_type):
  global live
  if difficulty_type=='hard':
    live = 5
    return f"You have {live} attempts remaining to guess the number"
  elif difficulty_type=='easy':
    live=10
    return f"You have {live} attempts remaining to guess the number"
#5
print(difficulty(difficulty_type))   
end_of_game=False
while not end_of_game:
  guess=int(input("Make a guess: "))
#6
  if guess!=number:
    if guess>number:
      
      live-=1
      if live==0:
        print("You've run out of guesses. You lose")
        end_of_game=True
      else:
        print("Too high\nGuess again")
        print(f"You have {live} attempts remaining to guess the number")
      
    else:
      
      live-=1
      if  live==0:
        print("You've run out of guesses.You lose")
        end_of_game=True
      else:
        print("Too low\nGuess again")
        print(f"You have {live} attempts remaining to guess the number")

  else:
      print(f"You got it! The answer was {number}.")
      end_of_game=True
    
    