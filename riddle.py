print("I'm black when i'm young, red in my teens and grey when i die.\nWhat am i?")
print("N.B: you have only three trials")
Riddle = "charcoal"
guessno = 0
guesslimit = 3
ans = ""
while guessno < guesslimit and ans != Riddle:
    ans= input("Enter your guess: ")
    guessno += 1
if ans == Riddle:
    print("YOU WIN!")
else:
    print("Uhhh, YOU LOSE")