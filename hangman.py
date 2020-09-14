import random
def hangman():
#    words = random.choice( ['superman','spiderman','janneman','jeandre','bhekicele'])
   my_list = []
   for x in open("doc.txt", "r").readlines():
       my_list.append(x.strip())
   words = random.choice(my_list)
   
   validLetters = 'abcdefghijklmnopqrstuvwxyz'
   turns = 10
   guessMade = ''
   
   while len(words) > 0:
       mainWord = ""
       missed = 0
       
       for letter in words:
           if letter in guessMade:
               mainWord = mainWord + letter
           else:
                mainWord = mainWord + "_" + " "
      
       if mainWord == words:
            print(mainWord)
            print('You win!')
            break

       print("Guess the word: ", mainWord)
       guess = input()

       if guess in validLetters:
           guessMade = guessMade + guess
       else:
            print('Invalid letter please, enter a valid letter')
            guess = input()
     
       if guess not in words:
           turns = turns - 1
           if turns == 9:
                print("9 turns left")
                print("  --------- ")
           if turns == 8:
                print("8 turns left")
                print("  --------- ")
                print("      O     ")
           if turns == 7:
                print("7 turns left")
                print("  --------- ")
                print("      O     ")
                print("      |     ")
           if turns == 6:
                print("6 turns left")
                print("  --------- ")
                print("      O     ")
                print("      |     ")
                print("     /      ")
           if turns == 5:
                print("5 turns left")
                print("  --------- ")
                print("      O     ")
                print("      |     ")
                print("     / \    ")
           if turns == 4:
                print("5 turns left")
                print("  --------- ")
                print("    \ O     ")
                print("      |     ")
                print("     / \    ")
           if turns == 3:
                print("3 turns left")
                print("  --------- ")
                print("    \ O /   ")
                print("      |     ")
                print("     / \    ")
           if turns == 2:
                print("2 turns left")
                print("  --------- ")
                print("    \ O|/   ")
                print("      |     ")
                print("     / \    ")
           if turns == 1:
                print("1 turns left")
                print("Last breath counting, Take care!")
                print("  --------- ")
                print("    \ O_|/   ")
                print("      |     ")
                print("     / \    ")
           if turns == 0:
                print("You lose")
                print("You killed duple!!!")
                print("  --------- ")
                print("      O_|   ")
                print("     /|\    ")
                print("     / \    ")
                break

   print(words)



name = input("Enter your name: ")
print("Welcome ", name)
print("=================================================")
print("Guess a word in less than 10 attempts")
hangman()