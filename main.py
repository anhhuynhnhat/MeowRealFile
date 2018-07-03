import os
import binascii
import data


def runSytem():
    path = 'D:\MODMIES\K0T3Z4\TESTING FOLDER'

    #
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            fileLink = os.path.join(root, filename)
            print(filename)
            fileSign = readFile(fileLink)
            checkTheSign(fileSign)

            for data_Header in data.data_Header_And_Extension:
                if "b'" + data_Header['header'] + "'" == str(binascii.hexlify(fileSign)):
                    print(data_Header['extension'])


def checkTheSign(fileSign):
    for data_Header in data.data_Header_And_Extension:
        if "b'" + data_Header['header'] + "'" == str(fileSign):
            print(data_Header['extension'])


def readFile(fileLink):
    fileSign = open(fileLink, 'rb').read()[:6]
    return fileSign


if __name__ == '__main__':
    runSytem()
