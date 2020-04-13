import numpy as np


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
        key = self.y
        k = 0
        for i in range(3):
            for j in range(3):
                keyMatrix[i][j] = ord(key[k]) % 65
                k += 1

    def encryptData(self):
        return None

    def decryptData(self):
        return None

    def processEncrypt(self):
        return None
    
    def processDecrypt(self):
        return None

class OutputHillChiper(HillChiper):
    def showMenu(self):
        return None

if __name__ == "__main__":

    isMessage = "REZ"
    isKey = "GYBNQKURP"

    keyMatrix = np.zeros((3,3))
    messageMatrix = np.zeros((3,1))
    cipherMatrix = np.zeros((3,1))

    ftr = HillChiper(isMessage, isKey)
    ftr.getKey()

