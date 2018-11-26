import vigenereCipher
import math

def readDict(fileName):
	with open(fileName, "r") as dictFile:
		dictionary = []
		for line in dictFile:
			dictionary.append(line.strip('\n'))
		return dictionary 


def findFactors(num):
	factors = []
	for i in range(3, num + 1):
		if ((num % i) == 0 and i < 8):
			factors.append(i)
	
	return factors


def commonFactors(distances):
	commonFactors = []

	for distance in distances:
		distanceFactors = findFactors(distance)
		
		for factor in distanceFactors:
			if (factor not in commonFactors and factor > 2 and factor < 8):
				commonFactors.append(factor)
	commonFactors.sort()
	return commonFactors


def findGCD(distances):
	sums = []

	for i in range(min(distances),max(distances)+1):
		sums.append(0)

		for j in range(len(distances)):
			if ((distances[j] % i) == 0):
				sums[i - min(distances)] += 1

	maxNum = sums[0]
	gcd = min(distances)
	for k in range(1,len(sums)):			
		if (sums[k] > maxNum):
			maxNum = sums[k]
			gcd = k + min(distances)

	return gcd


def stringDistances(text):
	distances = []
	for i in range(len(text) - 2):
		checkString = text[i:i+3]
		if (len(checkString) == 3):
			for j in range(i+3, len(text) - 2):
				duplicateString = text[j:j+3]
				if (checkString == duplicateString):
					if ((j - i) <= 26):
						distances.append(j - i)
	return distances


def keyPermutations(keyLength, keyLetters):
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	length = 1
	keys = []
	totalSize = 1
	counter = 0
	for i in range(keyLength):
		totalSize *= (len(letters) - i) 
	numConsecutive = totalSize // len(letters)
	if (keyLength > 0):
		index = 0
		for i in range(totalSize):
			keys.append([letters[index]])
			counter += 1
			if (counter == (numConsecutive)):
				counter = 0
				index += 1
	while (length < keyLength):	
		index = 0
		i = 0
		counter = 0
		numConsecutive = numConsecutive // (len(letters) - length)
		while (i < totalSize):	
			if (letters[index] not in keys[i]):
				keys[i].append(letters[index])
				i += 1	
			counter += 1
						
			if (counter == numConsecutive):
				index += 1
				counter = 0
				if(index == len(letters)):
					index = 0
		length += 1
	return keys


def decryptText(keyLength, text):
	decryptedText = ""
	currentKey = ""
	if (keyLength > 0):
		allKeys = keyPermutations(keyLength)
		for i in range(0, len(allKeys)):
			currentKey = ''.join(allKeys[i])
			print("Checking for: " + currentKey)
			decryptedText = vigenereCipher.vigenereDecrypt(currentKey, text)	
			if (checkforEnglish(decryptedText) == True):
				break
			else:
				decryptedText = ""

	return (decryptedText, currentKey)


def getSubstrings(keyLength, text):
	substrings = []
	subarray = []
	
	if (keyLength > 0):
		for j in range(keyLength):
			subarray.append([])
			for k in range(len(text)):
				if (((k - j) % keyLength) == 0):
					subarray[j].append(text[k])
			substrings.append("".join(subarray[j]))
	return substrings


def frequencyCheck(text):
	englishFrequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	frequencyTable = []
	matchCount = 0

	for i in range(len(alphabet)):
		frequencyTable.append([])
		frequencyTable[i].append(alphabet[i])
		frequencyTable[i].append(0)
		for j in range(len(text)):
			if (alphabet[i] == text[j]):
					frequencyTable[i][1] += 1

	frequencyTable.sort(key = getSecond, reverse = True)
	
	for letters in range(len(alphabet)):
		if (englishFrequency[letters] == frequencyTable[letters][0]):
			matchCount += 1
	return matchCount
	

def getSecond(item):
	return item[1]




def kasiskiExamination(cipherText):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	distances = stringDistances(cipherText)
	gcd = findGCD(distances)
	keyLengths = findFactors(gcd)
	decryptedText = ""
	success = False
	matchTable = []
	possibleKeys = []

	for keyLength in keyLengths:
		print("Trying key length: " + str(keyLength))
		substrings = getSubstrings(keyLength, cipherText)

		for i in range(keyLength):
			possibleKeys.append([],[],[])
			for letter in range(len(alphabet)):
				matchTable.append([])
				matchTable[letter].append(alphabet[letter])
				matchTable[letter].append(0)

				matchTable[letter][1] = frequencyCheck(vigenereCipher.vigenereDecrypt(alphabet[letter], substrings[i]))
			
			matchTable.sort(key = getSecond, reverse = True)
			for matchedChars in range(3):
				possibleKeys[i][matchedChars] = matchTable[matchedChars][1]

		keys = keyPermutations(keyLength, possibleKeys)
		
		result = decryptText(keyLength,cipherText)
		decryptedText = result[0]
		if (decryptedText != ""):
			print("Key found!")
			print("Decrypted text: " + decryptedText)
			print()
			print("Key: " + result[1])
			success = True
			break
	
	if (success == False):
		print("Brute force could not find a key for this cipher text.")
	

def checkforEnglish(text):

	dictionary = readDict("dictionary.txt")
	














