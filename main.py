#!/usr/bin/python3

from shutil import move, copyfile
import os
import binascii
import data


# Run program
def run_program(option):
    try:
        # Source file
        src_path = 'C:\Users\NGUYENXUANBANG\Desktop\MeowRealFile\data_source'
        dst_path = 'C:\Users\NGUYENXUANBANG\Desktop\MeowRealFile\data_dst'
        unk_path = 'C:\Users\NGUYENXUANBANG\Desktop\MeowRealFile\data_unk'
        # --------------------------------------------------------------------------------------
        TOTAL_FILE = 0
        COUNT_FILE_SUCCESS = 0
        for root, directories, filenames in os.walk(src_path):
            TOTAL_FILE = len(filenames)
            for filename in filenames:
                fileLink = os.path.join(root, filename)
                fileSign = get_file_sign_file(fileLink)
                real_file_extension = check_the_sign(fileSign)
                if (option != '1'):
                    COUNT_FILE_SUCCESS += 1
                    newFileLink = make_new_file_link(fileLink, filename, real_file_extension, dst_path, unk_path)
                else:
                    COUNT_FILE_SUCCESS += 1
                    newFileLink = make_new_file_link(fileLink, filename, real_file_extension, '-1', unk_path)
                handling(option, fileLink, newFileLink)
        print("------------------------ COUNT PERSEN SUCESSFULL ----------------------------------")
        print("COUNT_FILE_SUCCESS/TOTAL_FILE = " + str(COUNT_FILE_SUCCESS) + " / " + str(TOTAL_FILE))
        print("-----------------------------------------------------------------------------------")
    except:
        print("ERROR")


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
            run_program(option)

        elif (option == '2'):
            run_program(option)

        elif (option == '3'):
            print('33333')

        else:
            print('DO NOT UNDERSTAND')


# Create new file link
def make_new_file_link(fileLink, filename, real_file_extension, dst_path, unk_path):
    COUNT_FILE_SUCCESS = 0
    file_new_name = ""
    file_real_name_cut_extension = ""
    if len(real_file_extension) > 1:
        for file_extension in real_file_extension:
            if file_extension.lower() in filename.lower():
                file_new_name = file_extension
        # if file_new_name == "" :
        #   file_new_name = ""
    elif len(real_file_extension) == 1:
        file_new_name = real_file_extension[0]
    if dst_path == '-1':
        # Cut name file "."
        fileLink_cut_extension = fileLink.split(".")
        # cut and get name before "."
        # case exit name have extension
        file_real_name_cut_extension = fileLink_cut_extension[0]
        return file_real_name_cut_extension + '.' + file_new_name
    else:
        if file_new_name is not "":
            # Source file dst
            return os.path.join(dst_path, filename) + '.' + file_new_name
        else:
            # Source unknow fle
            return os.path.join(unk_path, filename)
        


# Modify file extension
def handling(option, fileLink, newFileLink):
    if (option == '1'):
        os.rename(fileLink, newFileLink)
    elif (option == '2'):
        move(str(fileLink), str(newFileLink))
    elif (option == '3'):
        copyfile(fileLink, newFileLink)


# Check signature of file
def check_the_sign(fileSign):
    extension_list = []
    for data_Header in data.data_Header_And_Extension:
        if data_Header['header'].upper() in fileSign.upper():
            extension_list.append(data_Header['extension'])
    return extension_list

# Read file with hex output and get 4 byte of file
def get_file_sign_file(fileLink):
    fileSign = binascii.hexlify(open(fileLink, 'rb').read()).decode('utf-8').upper()[:31]
    return fileSign


if __name__ == '__main__':
    menu_program()
