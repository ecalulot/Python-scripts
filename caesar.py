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
		
	rotation = ""
	while rotation.isdigit() == False:
		rotation = input("What is the rotation value?")

	aftertext = ""
	for letter in beforetext:
		if letter.isalpha():
			aftertext += (chr(((ord(letter) + sign*int(rotation) - 65) % 26) + 65))
				# could simplify this by (chr (((ord(letter) + sign*int(rotation)) % 26) + 52))
				# this is because 65 % 26 = 13
		elif letter.isspace():
			pass
		else:
			print ("Invalid character skipped: ", letter)
	print (aftertext,"\n\n")