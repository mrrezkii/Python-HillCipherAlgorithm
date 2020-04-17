import numpy as np
import sympy as sm


'''
    +----------------------------------------+
	|        MUHAMMAD REZKI ANANDA           |
    +----------------------------------------+
	|        SI/43/09 (1202190044)	 	     |
    +----------------------------------------+
'''

class HillChiper():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getKey(self):
        k = 0
        for i in range(3):
            for j in range(3):
                keyMatrix[i][j] = ord(self.y[k]) % 65
                k += 1

    def getInversKey(self):
        self.getKey()
        convertSM = sm.Matrix(keyMatrix)
        minorCoFactorKeyMatrix = convertSM.adjugate()
        determinantKeyMatrix = convertSM.det()

        inverseKeyMatrix = (determinantKeyMatrix * minorCoFactorKeyMatrix % 26)
        inverseKeyMatrix = inverseKeyMatrix.tolist()
        print(inverseKeyMatrix)
        
        
        

        
        
    def encryptData(self, messageMatrix):
        for i in range(3):
            for j in range(1):
                cipherMatrix[i][j] = 0
                for x in range(3):
                    cipherMatrix[i][j] += (keyMatrix[i][x] * messageMatrix[x][j])
                cipherMatrix[i][j] = cipherMatrix[i][j] % 26

    def decryptData(self):
        return None

    def processEncrypt(self):
        self.getKey()
        for i in range(3):
            messageMatrix[i][0] = ord(self.x[i]) % 65

        self.encryptData(messageMatrix)

        CipherText = []
        for i in range(3):
            CipherText.append(chr(cipherMatrix[i][0] + 65))
        print("Ciphertext: ", "".join(CipherText)) 



    def processDecrypt(self):
        return None

class OutputHillChiper(HillChiper):
    def showMenu(self):
        return None

if __name__ == "__main__":

    isMessage = "ACT"
    isKey = "GYBNQKURP"

    keyMatrix = [[0] * 3 for i in range(3)] 
    messageMatrix = [[0] for i in range(3)] 
    cipherMatrix = [[0] for i in range(3)]

    ftr = HillChiper(isMessage, isKey)
    ftr.getInversKey()

