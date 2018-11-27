import string

def frequencyCheck(text):
	englishFrequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
	alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	frequencyTable = []
	matchCount = 0
	for alphabet in alphabets:
		frequencyTable.append([])
		frequencyTable[alphabets.find(alphabet)].append(alphabet)
		frequencyTable[alphabets.find(alphabet)].append(0)
		for letter in text:
			if (alphabet == letter):
					frequencyTable[alphabets.find(alphabet)][1] += 1
	frequencyTable.sort(key = getSecond, reverse = True)
	for frequency in range(6):
		if (frequencyTable[frequency][0] in englishFrequency[0:6]):
			matchCount += 1	
	for frequency in range(20,26):
		if (frequencyTable[frequency][0] in englishFrequency[20:26]):
			matchCount += 1	
	return matchCount

def getSecond(item):
	return item[1]