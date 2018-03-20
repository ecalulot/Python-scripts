# Import the modules
import sys

while True:
	userchoice = input("Encrypt or Decrypt [Enter to quit]?").upper()

	if userchoice.startswith("E"):
		prompt = "What is the plaintext to encrypt?"
		sign = 1
	elif userchoice.startswith("D"):
		prompt = "What is the ciphertext to decrypt?"
		sign = -1	
	else:
		sys.exit()
	
	beforetext = input(prompt).upper()
	if beforetext == "":
		sys.exit()
		
	secretkey=""
	while len(secretkey)==0:
		secretkey = input("What is the secretkey?").upper()
		
	#sk_pos = 0
		
	aftertext = ""
	for position,letter in enumerate(beforetext.upper()):
		if letter.isalpha():
                    #aftertext += (chr(((ord(letter) - 65 + sign*ord(secretkey[sk_pos%len(secretkey)]) +  - 65) % 26) + 65))
		    aftertext += (chr(((ord(letter) - 65 + sign*ord(secretkey[position%len(secretkey)]) +  - 65) % 26) + 65))
		    #sk_pos += 1
		elif letter.isspace():
			pass
		else:
			print ("Invalid character skipped: ", letter)

	print (aftertext,"\n\n")