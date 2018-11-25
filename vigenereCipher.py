import string

def removePunctuation(text):
	textArray = []
	
	for i in range(0, len(text)):
		if (text[i].isalpha()):
			textArray.append(text[i])
	
	newText = "".join(textArray)
	return newText

def vigenereEncrypt(key, text):
	alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	keyIndex = 0
	encryptedArray = []
	keyUsed = key.upper()
	
	plainText = removePunctuation(text.upper())
	
	for index in range (0, len(plainText)):
		charCode = alphabets.find(plainText[index])
		if (charCode == -1):
			print("Error, text is not properly stripped of punctuation or letter not found")
			break
		else:
			if (keyIndex >= len(keyUsed)):
				keyIndex = 0

			cipherCode = charCode + ((alphabets.find(keyUsed[keyIndex])) % 26)

			if (cipherCode >= 26):
				cipherCode = cipherCode % 26

			encryptedArray.append(alphabets[cipherCode])			
			keyIndex += 1
	
	encryptedText = "".join(encryptedArray)
	return encryptedText

def vigenereDecrypt(key, text):
	alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	keyIndex = 0
	decryptedArray = []
	keyUsed = key.upper()

	for index in range (0, len(text)):
		charCode = alphabets.find(text[index])
		if (charCode == -1):
			print("Error, supplied text to decrypt is not in proper format.")
			break
		else:
			if (keyIndex >= len(keyUsed)):
				keyIndex = 0

			decipherCode = charCode - ((alphabets.find(keyUsed[keyIndex])) % 26)

			decryptedArray.append(alphabets[decipherCode])			
			keyIndex += 1
	
	decryptedText = "".join(decryptedArray)
	return decryptedText
	
			
