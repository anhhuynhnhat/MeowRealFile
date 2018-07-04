#!/usr/bin/python3

import shutil
import os
import binascii
import data


# Run program
def run_program(option):
    src_path = 'D:\MODMIES\MeowRealFile\TESTING FOLDER'
    dst_path = 'D:\MODMIES\MeowRealFile\DST FOLDER'

    for root, directories, filenames in os.walk(src_path):
        for filename in filenames:
            fileLink = os.path.join(root, filename)
            fileSign = get_file_sign_file(fileLink)
            real_file_extension = check_the_sign(fileSign)

            if (option != '1'):
                newFileLink = make_new_file_link(fileLink, filename, real_file_extension, dst_path)
            else:
                newFileLink = make_new_file_link(fileLink, filename, real_file_extension, '-1')

            print(newFileLink)

            handling(option, fileLink, newFileLink)


# Menu program
def menu_program():
    option = '0'
    while option == '0':
        print('----- WELCOME TO MEOW-REAL-FILE -----\n')
        print('Source please: ')
        print('CHOOSE OPTION:\n')
        print('1. Only rename (DEFAULT)\n')
        print('2. Cut file\n')
        print('3. Copy file\n')

        option = input('OPTION: ')

        if (option == '1'):
            print('11111')
            run_program(option)

        elif (option == '2'):
            print('Destination please: ')
            run_program(option)

        elif (option == '3'):
            print('33333')

        else:
            print('DO NOT UNDERSTAND')


# Create new file link
def make_new_file_link(fileLink, filename, real_file_extension, dst_path):
    if (dst_path == '-1'):
        return fileLink + '.' + real_file_extension
    else:
        return os.path.join(dst_path, filename) + '.' + real_file_extension


# Modify file extension
def handling(option, fileLink, newFileLink):
    if (option != '1'):
        os.rename(fileLink, newFileLink)
    else:
        shutil.move(fileLink, newFileLink)


# Check signature of file
def check_the_sign(fileSign):
    for data_Header in data.data_Header_And_Extension:
        if data_Header['header'] == str(fileSign):
            return data_Header['extension']


# Read file with hex output and get 4 byte of file
def get_file_sign_file(fileLink):
    fileSign = binascii.hexlify(open(fileLink, 'rb').read()).decode('utf-8').upper()[:8]
    return fileSign


if __name__ == '__main__':
    menu_program()
