import string

def frequencyCheck(text):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    frequencyCount = [0]*26
    textLength = len(text)
    for letter in text:
        if (letter in alphabets):
              frequencyCount[alphabets.find(letter)] += 1
    sum = 0
    for letter in range(len(alphabets)):
        sum += (frequencyCount[letter] * (frequencyCount[letter] - 1))
    coincidence = sum / ((textLength * (textLength - 1)))
    return coincidence

def stringCorrelation(text):
    englishFrequencies = [8.17,1.49,2.78,4.25,12.70,2.23,2.02,6.09,6.97,0.15,0.77,4.03,2.41,6.75,7.51,1.929,0.095,5.99,6.33,9.06,2.76,0.98,2.36,0.15,1.97,0.074]
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    frequency = [0]*26
    for letter in text:
        if (letter in alphabets):
              frequency[alphabets.find(letter)] += 1
    sum = 0
    for i in range(26):
        sum += (frequency[i] / len(text) *100) * (englishFrequencies[i])
    return sum
