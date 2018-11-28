import vigenereCipher
import checkForEnglish
import math

def mostCommonLetters(keyLength, text):
	alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	substrings = getSubstrings(keyLength, text)
	letters = []
	for string in range(keyLength):
		if (string > 20):
			break
		letters.append([])
		matches = []
		for letter in alphabets:
			matches.append([letter, checkForEnglish.stringCorrelation(vigenereCipher.vigenereDecrypt(letter, substrings[string]))])
		matches.sort(key = getSecond, reverse = True)
		for i in range(len(matches)):
			if (i == 3):
				break
			letters[string].append(matches[i][0])
	return letters

def findFactors(num):
	factors = []
	for i in range(3, num + 1):
		if ((num % i) == 0 and i < 10):
			factors.append(i)
	return factors

def findUniqueFactors(factorsList):
	uniqueFactors = []
	for factors in factorsList:
		for factor in factors:
			if (factor not in uniqueFactors):
				uniqueFactors.append(factor)
	uniqueFactors.sort()
	return uniqueFactors
	
def getMostCommonFactors(factorsList):
	uniqueFactors = findUniqueFactors(factorsList)
	factorFrequencies = []
	resultFactors = []
	for factor in uniqueFactors:
		factorFrequencies.append([factor, 0])
	for factors in factorsList:
		for factor in factors:
			if (factor in uniqueFactors):
				factorFrequencies[uniqueFactors.index(factor)][1] += 1
	factorFrequencies.sort(key = getSecond, reverse = True)
	for i in range(len(factorFrequencies)):
		if (i == 3):
			break
		resultFactors.append(factorFrequencies[i][0])
	return resultFactors

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
	for i in range(len(text) - 3):
		checkString = text[i:i+4]
		if (len(checkString) == 4):
			for j in range(i+4, len(text) - 3):
				duplicateString = text[j:j+4]
				if (checkString == duplicateString):
					if ((j - i) <= 26):
						distances.append(j - i)
	for i in range(len(text) - 4):
		checkString = text[i:i+5]
		if (len(checkString) == 5):
			for j in range(i+5, len(text) - 4):
				duplicateString = text[j:j+5]
				if (checkString == duplicateString):
					if ((j - i) <= 26):
						distances.append(j - i)
	return distances

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
	
def getSecond(item):
	return item[1]

def buildKeys(letters):
	keyLength = len(letters)
	numKeys = 1
	for index in range(keyLength):
		numKeys *= len(letters[index])
	keys = []
	for index in range(numKeys):
		key = ""
		modulusNum = numKeys
		for count in range(keyLength):
			letterIndex = index % modulusNum
			modulusNum //= len(letters[count])
			letterIndex //= modulusNum
			key += letters[count][letterIndex]
		keys.append(key)
	return keys

def detectKeyLength(lengths, text):
	keyLength = 0
	minDifference = 1
	for length in lengths:
		subStrings = getSubstrings(length, text)
		sum = 0
		for subString in subStrings:
			sum += checkForEnglish.frequencyCheck(subString)
		coIncidence = sum / length
		if (coIncidence > 0.06 and coIncidence < 0.07):
			if (abs(coIncidence - 0.067) < minDifference):
				minDifference = abs(coIncidence - 0.067)
				keyLength = length
	return keyLength

def kasiskiExamination(cipherText):
	distances = stringDistances(cipherText)
	factors = []
	for distance in distances:
		factors.append(findFactors(distance))
	keyLengths = getMostCommonFactors(factors)
	keyLengths.sort()
	keyLength = detectKeyLength(keyLengths, cipherText)
	return keyLength

def bruteForceMethod(cipherText):
	keyLength = kasiskiExamination(cipherText)
	maxMatch = 0
	key = ""
	letters = mostCommonLetters(keyLength, cipherText)
	keys = buildKeys(letters)
	keys.sort()
	numKeys = len(keys)
	for currentKey in range(numKeys):
		if (keys[currentKey] == ""):
			continue
		print("Checking for: " + keys[currentKey] + "(Totat: " + str(numKeys) + ", Current: " + str(currentKey) + ")")
		currentMatch = checkForEnglish.stringCorrelation(vigenereCipher.vigenereDecrypt(keys[currentKey], cipherText))
		if (currentMatch >= maxMatch):
			maxMatch = currentMatch
			key = keys[currentKey]
	
	return key