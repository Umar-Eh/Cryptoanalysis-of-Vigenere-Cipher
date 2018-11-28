import string
#import particle
import random
import vigenereCipher

class Particle():
    
    def __init__ (self, keyLen):
        self.personalBest = []
        self.velocity = []
        self.position = []
        self.keyLen = keyLen
        self.fitnessError = 1
        self.vmax = 1
        self.vmin = 0
        self.c1 = 2.05
        self.c2 = 2.05
        self.weight = 0.9

        for index in range(keyLen):
            velocity = self.vmin + (self.vmax - self.vmin) * (random.uniform(0,1))
            self.velocity.append(velocity)
            self.position.append(int(random.uniform(0,26)))
            self.personalBest.append(int(random.uniform(0,26)))
    
    def updatePosition(self):
        for index in range(self.keyLen):
            self.position[index] = int((self.position[index] + self.velocity[index]) % 26)
            

    def updateVelocity(self, globalBest):
        for index in range(self.keyLen):
            r1 = random.uniform(0,1)
            r2 = random.uniform(0,1)

            personalVelocity = self.c1 * r1 * (self.personalBest[index] - self.position[index])
            socialVelocity = self.c2 * r2 * (globalBest[index] - self.position[index])
            inertialVelocity = self.weight * self.velocity[index]

            self.velocity[index] = inertialVelocity + personalVelocity + socialVelocity

def getFrequencies(text):
    frequencies = [0] * 26
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in text:
        frequencies[alphabets.find(letter)]  = text.count(letter)
    return frequencies

def fitnessError(particle, text, globalBest):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    englishFrequencies = [8.17,1.49,2.78,4.25,12.70,2.23,2.02,6.09,6.97,0.15,0.77,4.03,2.41,6.75,7.51,1.929,0.095,5.99,6.33,9.06,2.76,0.98,2.36,0.15,1.97,0.074]
    #for index in range(len(englishFrequencies)):
    #    englishFrequencies[index] /= 100
    for index in range(particle.keyLen):
        particleFrequencies = getFrequencies(vigenereCipher.vigenereDecrypt(alphabets[particle.position[index]], text))
    sum = 0
    for frequency in range(len(particleFrequencies)):
        sum += abs(englishFrequencies[frequency] - (particleFrequencies[frequency] / len(text) * 100))
    fitnessError = 0.23 * sum
    if (fitnessError < particle.fitnessError):
        particle.fitnessError = fitnessError
        particle.personalBest[index] = particle.position[index]
    globalFrequencies = getFrequencies(vigenereCipher.vigenereDecrypt(alphabets[globalBest[index]], text))
    sum = 0
    for frequency in range(len(globalFrequencies)):
        sum += abs(englishFrequencies[frequency] - (globalFrequencies[frequency] / len(text) * 100))
    fitnessError = 0.23 * sum
    if (fitnessError > particle.fitnessError):
        globalBest[index] = particle.position[index]

def initializeBest(particles, text, globalBest, keyLen):
    for index in range(keyLen):
        globalBest[index] = int(random.uniform(0,26))
    for particle in particles:
        fitnessError(particle, text, globalBest)


def psoAttack(keyLen, cipherText):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    globalBest = [""] * keyLen
    particles = []
    key = ""
    for index in range(100):
        particles.append(Particle(keyLen))
    initializeBest(particles, cipherText, globalBest, keyLen)
    for index in range(100):
        for particle in particles:
            particle.updatePosition()
            particle.updateVelocity(globalBest)
            fitnessError(particle, cipherText, globalBest)
    stri = ""
    for i in range(keyLen):
        stri += alphabets[globalBest[i]]
    print(stri)
   
    return key

