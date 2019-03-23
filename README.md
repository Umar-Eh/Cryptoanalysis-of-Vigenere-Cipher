# Cryptoanalysis of the Vigenere Cipher

This repositoy contains a cryptoanalysis method in order to decipher and analyze<br>
a Vigenere Cipher.<br><br>

# Instructions

1. Clone the repository : git clone https://github.com/Umar-Eh/Cryptoanalysis-of-Vigenere-Cipher.git<br>
2. Run mainprogram.py (python mainprogram.py) to try both brute force and the particle swarm optimization (PSO)<br>
   methods.<br><br>

You may test only one of the aforementioned methods by commenting out the apporpriate lines i.e.<br>
**foundKey = kasiskiMethod.bruteForceMethod(encryptedText)** or **foundKey = psoMethod.psoAttack(len(key), encryptedText)**<br><br>

Please note that the plaintext variable may be replaced by a text file read and stored into a variable instead. <br>
This is a planned modification to the program. 
