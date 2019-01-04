# Import the modules
import sys

while True:
    userchoice = input("Encrypt or Decrypt [Enter to quit]?").upper()
    if userchoice.startswith("E"):
        prompt = "What is the plaintext to encrypt?"
    elif userchoice.startswith("D"):
        prompt = "What is the ciphertext to decrypt?"
    else:
        sys.exit()
	
    beforetext = input(prompt).upper()
    if beforetext == "":
        sys.exit()
		
    secretkey=""
    while len(secretkey)<5:
        secretkey = input("What is the secretkey (min of 5 characters)?").upper()
    order = []
    if (secretkey.isdigit()):
        for el in secretkey:
            if (secretkey.count(el)>1):
                print("Invalid Key")
                sys.exit()
            order.append(el)
    else:
        tempSecret = list(secretkey)
        tempKey = list(tempSecret)
        tempKey.sort()
        #tempKey.reverse()
        for el in tempKey:
            order.append(tempSecret.index(el))
            tempSecret[tempSecret.index(el)] = "."
    textGrid = []
    aftertext = ""
    tempText = ""
    for letter in beforetext.upper():
        if letter.isalpha():
            tempText += letter
        elif letter.isspace():
            pass
        else:
            print ("Invalid character skipped: ", letter)
    while (len(tempText)%len(secretkey) != 0):
        tempText += "X" 			#chr(random.randint(65,90))
    while(len(tempText) > 0):
        textGrid.append(list(tempText[:len(secretkey)]))
        tempText = tempText[len(secretkey):]
        #print (order)
    aftertext = ""
    if userchoice.startswith("E"):
        for mycol in range(0,len(order)):
            for myrow in range(0,len(textGrid)):
                aftertext += textGrid[myrow][order[mycol]]
    else:
        tempGrid = textGrid
        cnum = 0
        for mycol in range(0,len(order)):
            for myrow in range(0,len(textGrid)):
                tempGrid[myrow][order[mycol]] = beforetext[cnum]
                cnum += 1
        for myrow in range(0,len(tempGrid)):
            for mycol in range(0,len(order)):
                aftertext += tempGrid[myrow][mycol]
                        
    print (beforetext," => ",aftertext)
    