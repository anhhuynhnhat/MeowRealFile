#!/usr/bin/python3

from shutil import move, copyfile
import os
import binascii
import data

sign_file_and_name_file_unk_path = 'C:\MEO_RESULT\SignUnknown'
data_header_after_156_exe = '546869732070726F6772616D2063616E6E6F742062652072756E20696E20444F53206D6F6465'

# valid directory
def valid_direc(directory):
    return os.path.exists(directory)


# Run program
def run_program(option):
    try:
        # Source file
        src_path = 'C:\Users\NGUYENXUANBANG\Desktop\MeowRealFile\APT-sample'
        dst_path = 'C:\Users\NGUYENXUANBANG\Desktop\MeowRealFile\DSTFolder'
        unk_path = 'C:\Users\NGUYENXUANBANG\Desktop\MeowRealFile\UNKNOWN'
        # --------------------------------------------------------------------------------------
        if not valid_direc(src_path):
            print('SOURCE NOT FOUND')
            return
        if os.listdir(src_path) == []:
            print('FOLDER IS EMPTY')
            return
        # Check distination path is not exit
        # Create new directory
        if not valid_direc(dst_path):
            os.makedirs(dst_path)
        # Check unk path is not exit
        # Create new directory
        if not valid_direc(unk_path):
            os.makedirs(unk_path)
        # Check file data path is not exit
        # Create new directory
        if not valid_direc(sign_file_and_name_file_unk_path):
            os.makedirs(sign_file_and_name_file_unk_path)
        # ----------------------------------------------------------------------------------------
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
                    newFileLink = make_new_file_link(fileLink, filename, real_file_extension, dst_path, unk_path, fileSign)
                else:
                    COUNT_FILE_SUCCESS += 1
                    newFileLink = make_new_file_link(fileLink, filename, real_file_extension, '-1', unk_path, fileSign)
                handling(option, fileLink, newFileLink)
        print("------------------------ COUNT PERSEN SUCESSFULL ----------------------------------")
        print("COUNT_FILE_SUCCESS/TOTAL_FILE = " + str(COUNT_FILE_SUCCESS) + " / " + str(TOTAL_FILE))
        print("-----------------------------------------------------------------------------------")
    except Exception as e:
        print("ERROR " + str(e))


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
            run_program(option)

        else:
            print('DO NOT UNDERSTAND')


# Create new file link
def make_new_file_link(fileLink, filename, real_file_extension, dst_path, unk_path, fileSign):
    try:
        COUNT_FILE_SUCCESS = 0
        file_new_name = ''
        file_real_name_cut_extension = ''
        if len(real_file_extension) > 1:
            for file_extension in real_file_extension:
                if file_extension.lower() in filename.lower():
                    file_new_name = file_extension
                    # if file_new_name == "" :
                    #   file_new_name = ""
        elif len(real_file_extension) == 1:
            file_new_name = real_file_extension[0]
        if file_new_name.upper() is "EXE":
            if str(fileSign)[155:] in data_header_after_156_exe:
                file_new_name = 'EXE'
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
                # Add data file unknow to file
                with open(sign_file_and_name_file_unk_path + '\\result.txt', 'a') as the_file:
                    the_file.write('File Link ' + fileLink + ' Sign ' + get_file_sign_file(fileLink) + '\r\n')
                # Source unknow fle
                return os.path.join(unk_path, filename)
    except Exception as e:
        print("ERROR " + str(e))


# Modify file extension
def handling(option, fileLink, newFileLink):
    try:
        if (option == '1'):
            os.rename(fileLink, newFileLink)
        elif (option == '2'):
            move(str(fileLink), str(newFileLink))
        elif (option == '3'):
            copyfile(fileLink, newFileLink)
    except Exception as e:
        print("ERROR " + str(e))


# Check signature of file
def check_the_sign(fileSign):
    try:
        extension_list = []
        for data_Header in data.data_Header_And_Extension:
            if data_Header['header'].upper() in fileSign.upper():
                extension_list.append(data_Header['extension'])
        return extension_list
    except Exception as e:
        print("ERROR " + str(e))


# Read file with hex output and get 4 byte of file
def get_file_sign_file(fileLink):
    try:
        fileSign = binascii.hexlify(open(fileLink, 'rb').read()).decode('utf-8').upper()[:232]
        return fileSign
    except Exception as e:
        print("ERROR " + str(e))


if __name__ == '__main__':
    menu_program()
