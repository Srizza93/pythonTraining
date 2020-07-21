import time
import random

print("                                 Hello Welcome to HANGMAN!!!!!")

time.sleep(0)
print("\n")
name = input("What's your name?: ")

time.sleep(0)
print("Hi " + name, "You have 10 attempts to guess the letters in the word")
time.sleep(0)
print("                                        Get ready!!!")
print("\n")
time.sleep(0)
print("                                             3")
time.sleep(0)
print("                                             2")
time.sleep(0)
print("                                             1")
print("\n")
time.sleep(1)
print("                                      GO!!!!!GO!!!!GO!!!!!")
print("\n")
Listword = ["jazz", "coronavirus", "apple", "television", "facebook", "computer", "netherlands", "awkward", "bagpipes", "banjo", "bungler", "dwarves", "fervid", "croquet"]
word = (random.choice(Listword))
guesses = ('')
lives = 10
points = 0

while lives > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("\n")
        print("Great Job!! You won!!")
        print("Final Score:", + points)
        print("Lives: ", + int(lives))
        break
    guess = input("Guess each letter: ").lower()
    print(guess)
    guesses += guess
    if guess in word and char not in guesses:
        points += 1
        print("You scored", + points, "points till now!!")
        print("Lives: ", + int(lives))
        print("_____________________________________________")
        print("\n")
    if guess not in word:
            lives -= 1
            print("\n")
            print("You loose!")
            print("Try again")
    if lives == 9:
            print("\n")
            print("""            
 ___
|   |______
|          |        
|__________|""")
            print("Lives: ", + int(lives))
            print("Score: ", + points)
            print("_____________________________________________")
            print("\n")
    if lives == 8:
            print("""            
  |    
  |    
 _|_
|   |______
|          |
|__________|""")
            print("Lives: ", + int(lives))
            print("Score: ", + points)
            print("_____________________________________________")
            print("\n")
    if lives == 7:
            print("""
  |          
  |         
  |      
  |    
  |    
 _|_
|   |______
|          |
|__________|""")
            print("Lives: ", + int(lives))
            print("Score: ", + points)
            print("_____________________________________________")
            print("\n")
    if lives == 6:
            print("""
  |    |      
  |         
  |      
  |    
  |    
 _|_
|   |______
|          |
|__________|""")
            print("Lives: ", + int(lives))
            print("Score: ", + points)
            print("_____________________________________________")
            print("\n")
    if lives == 5:
            print("""
  |    |      
  |    o     
  |      
  |    
  |    
 _|_
|   |______
|          |
|__________|""")
            print("Lives: ", + int(lives))
            print("Score: ", + points)
            print("_____________________________________________")
            print("\n")
    if lives == 4:
            print("""
  |    |      
  |    o     
  |    |   
  |    
  |    
 _|_
|   |______
|          |
|__________|""")
            print("Lives: ", + int(lives))
            print("Score: ", + points)
            print("_____________________________________________")
            print("\n")
    if lives == 3:
            print("""
  |    |      
  |    o     
  |   /|\  
  |    
  |    
 _|_
|   |______
|          |
|__________|""")
            print("Lives: ", + int(lives))
            print("Score: ", + points)
            print("_____________________________________________")
            print("\n")
    if lives == 2:
            print("""
  |    |      
  |    o     
  |   /|\   
  |    |
  |    
 _|_
|   |______
|          |
|__________|""")
            print("Lives: ", + int(lives))
            print("Score: ", + points)
            print("_____________________________________________")
            print("\n")
    if lives == 1:
            print("""
   ____          
  |    |      
  |    o     
  |   /|\   
  |    |
  |   / 
 _|_
|   |______
|          |
|__________|""")
            print("Lives: ", + int(lives))
            print("Score: ", + points)
            print("_____________________________________________")
            print("\n")
    if lives == 0:
            print("""
   ____      
  |    |      
  |    o     
  |   /|\   
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|""")
            print("Lives: ", + int(lives))
            print("Score: ", + points)
            print("_____________________________________________")
            print("\n")
            print("GAME OVER")
            print("Final Score:", + points)
            print("The Word was", word)

