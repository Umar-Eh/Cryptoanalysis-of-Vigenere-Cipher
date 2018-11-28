import random

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
            self.position.append(random.uniform(0,26))
    
    def updatePosition(self):
        for index in range(self.keyLen):
            self.position[index] = (self.position[index] + self.velocity[index]) % 26
            

    def updateVelocity(self, globalBest):
        for index in range(self.keyLen):
            r1 = random.uniform(0,1)
            r2 = random.uniform(0,1)

            personalVelocity = self.c1 * r1 * (self.personalBest[index] - self.position[index])
            socialVelocity = self.c2 * r2 * (globalBest[index] - self.position[index])
            inertialVelocity = self.weight * self.velocity[index]

            self.velocity[index] = inertialVelocity + personalVelocity + socialVelocity
    