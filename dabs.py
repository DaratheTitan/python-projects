#i don't understand why translation works as the phrase when it is stored in an empty string
try:
    def translate(phrase):
        translation = ""
        for letter in phrase:
            if letter in "AEIOUaeiou":
                if letter.isupper():
                    translation = translation + "G"
                else:
                    translation = translation + "g"
            else:
                translation = translation + letter
        return translation
except:
    print("Invalid input")

print(translate(input("Enter a phrase: ")))