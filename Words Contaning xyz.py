#words containg xyz
#Modes:1,2,3
#contains exact string xyz
#contains xyz in any order
#contains xyz in specific places  _X__YZ
dictionary = open("words_alpha.txt")

def Mode1(): #contains exact string xyz
    target = input("Specify the exact letters you are looking for: ")
    length = int(input("Specify the length for any word answers: "))
    found = False
    for word in dictionary:
        word = word.strip()
        if len(word)==length :
            if target in word:
                print(word)
                found = True
    if found == False:
        print("Nothing found :(")
def Mode2():
    target = input("Specify the exact letters you are looking for: ")
    length = int(input("Specify the maximum length for any word answers: "))
    found = False
    allLetterCheck = False
    for word in dictionary:
        word = word.strip()
        if len(word)<=length :
            for letter in target:
                if letter in word:
                    allLetterCheck = True
                else:
                    allLetterCheck = False
                    break
            if allLetterCheck == True:
                print(word)
                found = True
    if found == False:
        print("Nothing found :(")
def Mode3():
    targetA = input("Specify the exact letters you are looking for before the space: ")
    targetB = input("Specify the exact letters you are looking for after the space: ")
    numSpaces = int(input("Specify the number of spaces between the letters: "))
    length = int(input("Specify the length for any word answers: "))
    found = False
    for word in dictionary:
        word = word.strip()
        if len(word)==length :
            if targetA in word:
                if targetB in word[(word.find(targetA)+len(targetA)+numSpaces):(word.find(targetA)+len(targetA)+numSpaces+len(targetB))]:
                    print(word)
                    found = True
    if found == False:
        print("Nothing found :(")
    
print("REMEMBER TO TYPE PROPER PARAMETERS, THERE ARE ABOUT 400k WORDS THAT COULD BE OUTPUT")
print("Mode 1: Find words containing an exact match to your input (typing act will bring words like actual or fact)")
print("Mode 2: Find words containg all the letters you input in any order typing ")
print("Mode 3: Finds words containing an exact match with gaps in your input (typing i e will find words like bile or time) \n")
modeChoice = int(input("Please select which mode you wish to use: "))
if modeChoice == 1:
    Mode1()
elif modeChoice == 2:
    Mode2()
elif modeChoice == 3:
    Mode3()
else:
    print("Input error. Ensure you are typing only 1,2 or 3")