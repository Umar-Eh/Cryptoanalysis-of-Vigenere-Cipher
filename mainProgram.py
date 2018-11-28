import vigenereCipher
import kasiskiMethod
import checkForEnglish
import psoMethod

def main():
	plainText = "This book also contains several data structures. A data structure is a way to store and organize data in order to facilitate access and modifications. No single data structure works well for all purposes, and so it is important to know the strengths and limitations of several of them. Not every problem solved by algorithms has an easily identified set of candidate solutions. For example, suppose we are given a set of numerical values representing samples of a signal, and we want to compute the discrete Fourier transform of these samples. The discrete Fourier transform converts the time domain to the frequency domain, producing a set of numerical coefficients, so that we can determine the strength of various frequencies in the sampled signal. In addition to lying at the heart of signal processing, discrete Fourier transforms have applications in data compression and multiplying large polynomials and integers. Electronic commerce enables goods and services to be negotiated and exchanged electronically, and it depends on the privacy of personal information such as credit card numbers, passwords, and bank statements. A political candidate may want to determine where to spend money buying campaign advertising in order to maximize the chances of winning an election. An airline may wish to assign crews to flights in the least expensive way possible, making sure that each flight is covered and that government regulations regarding crew scheduling are met. An Internet service provider may wish to determine where to place additional resources in order to serve its customers more effectively. They have practical applications. Of the problems in the above list, finding the shortest path provides the easiest examples. A transportation firm, such as a trucking or railroad company, has a financial interest in finding shortest paths through a road or rail network because taking shorter paths results in lower labor and fuel costs. Or a routing node on the Internet may need to find the shortest path through the network in order to route a message quickly."

	key = "sun"
	
	encryptedText = vigenereCipher.vigenereEncrypt(key, plainText)

	print()
	print("Starting brute force attack...")
	foundKey = kasiskiMethod.bruteForceMethod(encryptedText)
	print()
	if (foundKey == ""):
		print("Brute force method could not find the key.")
	else:
		print("Brute Force found key : " + foundKey)
		
	print()

	foundKey = psoMethod.psoAttack(len(key), encryptedText)
	print()
	if (foundKey == ""):
		print("Particle swarm optimization method could not find the key.")
	else:
		print("Particle swarm optimization found key : " + foundKey)
	print()

main()
