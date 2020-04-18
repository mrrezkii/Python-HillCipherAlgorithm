import sympy as sm
import mysql.connector
import datetime
from beautifultable import BeautifulTable


'''
    +----------------------------------------+
	|        MUHAMMAD REZKI ANANDA           |
    +----------------------------------------+
	|        SI/43/09 (1202190044)	 	     |
    +----------------------------------------+
'''

class HillChiper():
    def __init__(self, x, y, db):
        self.x = x
        self.y = y
        self.db = db

    def getKey(self):
        k = 0
        for i in range(3):
            for j in range(3):
                keyMatrix[i][j] = ord(self.y[k]) % 65
                k += 1

    def encryptData(self, messageMatrix):
        for i in range(3):
            for j in range(1):
                cipherMatrix[i][j] = 0
                for x in range(3):
                    cipherMatrix[i][j] += (keyMatrix[i][x] * messageMatrix[x][j])
                cipherMatrix[i][j] = cipherMatrix[i][j] % 26

        return cipherMatrix

    def processEncrypt(self):
        self.getKey()
        for i in range(3):
            messageMatrix[i][0] = ord(self.x[i]) % 65

        self.encryptData(messageMatrix)

        CipherText = []
        for i in range(3):
            CipherText.append(chr(cipherMatrix[i][0] + 65))
        strCipherText = ''.join(CipherText)
        print("\t>> [Output] Hasil Enkripsi dari", self.x, "adalah \t:", strCipherText)
        print()

        dateTime = datetime.datetime.now()
        cursor = db.cursor()
        sql = "INSERT INTO `enkripsi`( `kata_awal_en`, `hasil_enkripsi`, `tanggal`) VALUES (%s, %s, %s)"
        val = (self.x, strCipherText, dateTime)

        cursor.execute(sql, val)

        db.commit()


class Decrypt(HillChiper):
    def __init__(self, x, y, db):
        super().__init__(x, y, db)

    def getInversKey(self):
        global keyMatrix
        super().getKey()
        convertSM = sm.Matrix(keyMatrix)
        minorCoFactorKeyMatrix = convertSM.adjugate()
        determinantKeyMatrix = convertSM.det()

        keyMatrix = (determinantKeyMatrix * minorCoFactorKeyMatrix % 26)
        keyMatrix = keyMatrix.tolist()

    def decryptData(self, cipherMatrix):
        self.getInversKey()
        for i in range(3):
            for j in range(1):
                messageMatrix[i][j] = 0
                for x in range(3):
                    messageMatrix[i][j] += (keyMatrix[i][x] * cipherMatrix[x][j])
                messageMatrix[i][j] = messageMatrix[i][j] % 26  

        return messageMatrix

    def processDecrypt(self):        
        for i in range(3):
            cipherMatrix[i][0] = ord(self.x[i]) % 65

        self.decryptData(cipherMatrix)

        MessageText = []
        for i in range(3):
            MessageText.append(chr(messageMatrix[i][0] + 65))
        strMessageText = ''.join(MessageText)
        print("\t>> [Output] Hasil Dekripsi dari", self.x, "adalah \t:", strMessageText)
        print()

        dateTime = datetime.datetime.now()
        cursor = db.cursor()
        sql = "INSERT INTO `dekripsi`( `kata_awal_de`, `hasil_dekripsi`, `tanggal`) VALUES (%s, %s, %s)"
        val = (self.x, strMessageText, dateTime)

        cursor.execute(sql, val)

        db.commit()


if __name__ == "__main__":

    keyMatrix = [[0] * 3 for i in range(3)] 
    messageMatrix = [[0] for i in range(3)] 
    cipherMatrix = [[0] for i in range(3)]

    STRING_JUDUL_APPS = " APLIKASI ENKRIPSI HILL CIPHER "
    print()
    print("=" * 20 + STRING_JUDUL_APPS + "=" * 20)
    print()

    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="tubes_kriptografi"
        )
    except mysql.connector.Error as er:
        print("Gagal tersambung dengan database", er)
    else:
        print("\n_____________________________________________________________________\n")
        print("| Menu 1. Enkripsi Data                  | Menu 2. Dekripsi Data     ")
        print("| Menu 3. History Enkripsi               | Menu 4. History Dekripsi  ")
        print("                            [0] Keluar                               ")
        print("_____________________________________________________________________")
        print()
    
        while True:
            try:
                isInputMenu = int(input(">> Masukkan menu yang ingin Anda pilih \t: "))
            except ValueError:
                print('''
                        Input supplied should be of type 'int'
                ''')
            else:
                if isInputMenu < 0:
                    print('''
                           Error Input User
                            ''')
                elif isInputMenu == 1:
                    print("\t** SEMUA KATA YANG DI INPUTKAN AKAN DI UPPERCASE **")
                    isMessage = input("\t>> Masukkan 3 huruf yang ingin di enkripsi \t: ")
                    if any(str.isdigit(c) for c in isMessage):
                        print('''
                            Input supplied should be of type 'str' 
                            ''')
                    else:
                        while len(isMessage) != 3:
                            print('''
                            Error. Only 3 digit allowed
                            ''')
                            exit()
                        msg__ = isMessage.upper()
                        key__ = "GYBNQKURP"

                        ftr = HillChiper(msg__, key__, db)
                        ftr.processEncrypt()
                elif isInputMenu == 2:
                    print("\t** SEMUA KATA YANG DI INPUTKAN AKAN DI UPPERCASE **")
                    isMessage = input(" \t>> Masukkan 3 huruf yang ingin di dekripsi \t: ")
                    if any(str.isdigit(c) for c in isMessage):
                        print('''
                            Input supplied should be of type 'str' 
                            ''')
                    else:
                        while len(isMessage) != 3:
                            print('''
                            Error. Only 3 digit allowed
                            ''')
                            exit()
                        msg__ = isMessage.upper()
                        key__ = "GYBNQKURP"

                        ftr = Decrypt(msg__, key__, db)
                        ftr.processDecrypt()
                elif isInputMenu == 3:
                    cursor = db.cursor()
                    sql = "SELECT * FROM `enkripsi`"
                    cursor.execute(sql)

                    results = cursor.fetchall()

                    table = BeautifulTable()
                    table.column_headers = ['Kode Enkripsi', 'Kata Awal', 'Hasil Enkripsi', 'Tanggal & Waktu']
                    for row in results:
                        table.append_row([row[0], row[1], row[2], row[3]])
                    print(table)
                    print()
                elif isInputMenu == 4:
                    cursor = db.cursor()
                    sql = "SELECT * FROM `dekripsi`"
                    cursor.execute(sql)

                    results = cursor.fetchall()

                    table = BeautifulTable()
                    table.column_headers = ['Kode Dekripsi', 'Kata Awal', 'Hasil Dekripsi', 'Tanggal & Waktu']
                    for row in results:
                        table.append_row([row[0], row[1], row[2], row[3]])
                    print(table)
                    print()
                elif isInputMenu == 0:
                    exit()
                else:
                    print('''
                           Enter the numbers according to the menu options above
                        ''')
    finally:
        print()
        print('''
                ***** Terimakasih sudah menggunakan aplikasi ini *****
        ''')


    


    
   

       

    

    
    


