import numpy as np


'''
    +----------------------------------------+
	|        MUHAMMAD REZKI ANANDA           |
    +----------------------------------------+
	|        SI/43/09 (1202190044)	 	     |
    +----------------------------------------+
'''

class HillChiper():
    def getKey(self):
        return None

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


    ftr = OutputHillChiper()
    ftr.showMenu()

