#words containg xyz
#Modes:1,2,3
#contains exact string xyz
#contains xyz in any order
#contains xyz in specific places  _X__YZ
dictionary = open("words_alpha.txt")

def Mode1(): #finds words that contain exact string xyz (typing act will bring words like actual or fact)
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
        
def Mode2(): #finds words using letters xyz in any order (tca should give act and cat)
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
        
def Mode3(): #finds words using x_yz when there are gaps in the word (typing i e will find words like bile or time)
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
                    #^this long line of code is limit the search so that extra words that dont fit the criteria appear
                    #I'm doing this by only checking if the second part of the word 
                    print(word)
                    found = True
                    
    if found == False:
        print("Nothing found :(")
        
def Mode4(): #Finds words that only contain letters from provided list
    length = int(input("Specify the length for any word answers: "))
    letterList = input("Specify which letters the word can use: ")
    letterListState = []
    found = False
    progress = False
    for letter in letterList:
        letterListState.append(False)
    for word in dictionary:
        word = word.strip()
        if len(word)==length :
            for i in range(0,len(word)): #for every letter in our word...
                for j in range(0,len(letterList)) :#for each letter in our input...
                    if (word[i] == letterList[j]) and not letterListState[j]: #To prevent letters being used twice in target word
                        letterListState[j] = True                             #when double letters aren't provided by the user
                        found = True  
                if found == True:
                    found = False
                    progress = True
                else:
                    progress = False
                    break
                    
            if progress == True:
                print(word)
                found = False
                progress = False
        letterListState = []
        for letter in letterList:
            letterListState.append(False)            
                              
    
print("REMEMBER TO TYPE PROPER PARAMETERS, THERE ARE ABOUT 400k WORDS THAT COULD BE OUTPUT")
print("Mode 1: Find words containing an exact match to your input (typing act will bring words like actual or fact)")
print("Mode 2: Find words containg all the letters you input in any order typing")
print("Mode 3: Finds words containing an exact match with gaps in your input (typing i e will find words like bile or time)")
print("Mode 4: Finds words that only contain letters from provided list\n")
modeChoice = int(input("Please select which mode you wish to use: "))
if modeChoice == 1:
    Mode1()
elif modeChoice == 2:
    Mode2()
elif modeChoice == 3:
    Mode3()
elif modeChoice == 4:
    Mode4()
else:
    print("Input error. Ensure you are typing only 1,2,3 or 4")