import vigenereCipher

def findFactors(num):
	factors = []
	for i in range(2,num + 1):
		if ((num % i) == 0):
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

		for j in range(0,len(distances)):
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
	keyLengths = []
	distances = []

	for i in range(0,len(text) - 2):
		checkString = text[i:i+3]
		if (len(checkString) == 3):
			for j in range(i+3, len(text) - 2):
				duplicateString = text[j:j+3]
				if (checkString == duplicateString):
					if ((j - i) <= 26):
						distances.append(j - i)

	for i in range(0,len(text) - 3):
		checkString = text[i:i+4]
		if (len(checkString) == 4):
			for j in range(i+4, len(text) - 3):
				duplicateString = text[j:j+4]
				if (checkString == duplicateString):
					if ((j - i) <= 26):
						distances.append(j - i)

	return distances


def keyPermutations(keyLength):
	alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	keys = []
	start = len(alphabets)
	length = keyLength
	
	for j in range(0, start):
		if (alphabets[j] not in keys):
			keys.append([alphabets[j]])
		

	return keys

def decryptText(keyLength, text):
	i = 2

	
	
	
















