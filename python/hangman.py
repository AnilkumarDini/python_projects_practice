import random

print("\nHey Player !!\n")
name = input("Enter your name : ")
print("\nWelcome ",name)
print("___________________________________________")
print("Try to guess the word within 10 attempts..")
print("\nGAME BEGINS...\n")

# Game logic

word = random.choice(["dreamcatcher","kingfisher","catfish","pokemon",
"pomegranate","chillisauce","raddish","pasta","mayflower","dahlia","kangaroo","pomegranate"])

valid_letters ='abcdefghijklmnopqrstuvwxyz'

turns = 10
guess_made = ''

while len(word) > 0:
    main = ""
    missed = 0

    for letter in word:
        if letter in guess_made:
            main = main + letter
        else:
            main = main + "-" + " "
    
    if main == word:
        print(main)
        print("\n You Won !!\n")
        break

    print("\nGuess the word : ",main)
    guess = input()

    if guess not in valid_letters:
        print("\nPlease Enter a valid character !!\n")
        guess = input()
    
    if guess in main or guess in guess_made:
        print("\nHey! You already made that guess !!")
        print("Make another guess : ")
        guess = input()

    guess_made = guess_made + guess

    if guess not in word:
        turns = turns - 1

        if turns == 9:
            print("\n9 turns left\n")
            print("  --------  ")
        if turns == 8:
            print("\n8 turns left\n")
            print("  --------  ")
            print("     O      ")
        if turns == 7:
            print("\n7 turns left\n")
            print("  --------  ")
            print("     O      ")
            print("     |      ")
        if turns == 6:
            print("\n6 turns left\n")
            print("  --------  ")
            print("     O      ")
            print("     |      ")
            print("    /       ")
        if turns == 5:
            print("\n5 turns left\n")
            print("  --------  ")
            print("     O      ")
            print("     |      ")
            print("    / \     ")
        if turns == 4:
            print("\n4 turns left\n")
            print("  --------  ")
            print("   \ O      ")
            print("     |      ")
            print("    / \     ")
        if turns == 3:
            print("\n3 turns left\n")
            print("  --------  ")
            print("   \ O /    ")
            print("     |      ")
            print("    / \     ")
        if turns == 2:
            print("\n2 turns left\n")
            print("  --------  ")
            print("   \ O /|   ")
            print("     |      ")
            print("    / \     ")
        if turns == 1:
            print("\n1 turns left\n")
            print("Last breaths counting, Take care!")
            print("  --------  ")
            print("   \ O_|/   ")
            print("     |      ")
            print("    / \     ")
        if turns == 0:
            print("\nYou loose")
            print("\nYou let a kind man die\n")
            print("  --------  ")
            print("     O_|    ")
            print("    /|\      ")
            print("    / \     ")
            break
        


    


