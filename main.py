#!/usr/bin/python3

import os
import binascii
import data


# Run program
def run_program():
    src_path = 'D:\MODMIES\MeowRealFile\TESTING FOLDER'
    dst_path = 'D:\MODMIES\MeowRealFile\DST FOLDER'
    #
    for root, directories, filenames in os.walk(src_path):
        for filename in filenames:
            fileLink = os.path.join(root, filename)
            print(fileLink)
            newFileName = check_the_sign(readFile(fileLink), fileLink)
            print(newFileName)
            re_extension(fileLink, newFileName)

# Menu program
def menu_program():
    choice = '0'
    while choice == '0':
        print('----- WELCOME TO MEOW-REAL-FILE -----')
        print('Source please: ')
        print('Destination please: ')
        print('CHOOSE OPTION:')
        print('1. Cut file')
        print('2. Copy file')

        choice = input('OPTION: ')

        if (choice == '1'):
            print('FIRST')
        elif (choice == '2'):
            print('SECOND')
        else:
            print('DO NOT UNDERSTAND')


# Modify file extension
def re_extension(fileLink, newExtension):
    os.rename(fileLink, newExtension)


# Check signature of file
def check_the_sign(fileSign, fileLink):
    for data_Header in data.data_Header_And_Extension:
        if data_Header['header'] == str(fileSign):
            newFileName = fileLink + '.' + data_Header['extension']
            return newFileName


# Read file with hex output and get 4 byte of file
def readFile(fileLink):
    fileSign = binascii.hexlify(open(fileLink, 'rb').read()).decode('utf-8').upper()[:8]
    return fileSign


if __name__ == '__main__':
    run_program()
