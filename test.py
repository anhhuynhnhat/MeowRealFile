from shutil import move, copyfile
import os
import binascii
import data

# Read file with hex output and get 4 byte of file
def get_file_sign_file(fileLink):
    fileSign = binascii.hexlify(open(fileLink, 'rb').read()).decode('utf-8').upper()[:31]
    return fileSign

# Check signature of file
def check_the_sign(fileSign):
    extension_list = []
    for data_Header in data.data_Header_And_Extension:
        if data_Header['header'] in fileSign:
            extension_list.append(data_Header['extension'])
    return extension_list

# Create new file link
def make_new_file_link(fileLink, filename, real_file_extension, dst_path):
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
        return os.path.join(dst_path, filename) + '.' + file_new_name

# Modify file extension
def handling(option, fileLink, newFileLink):
    if (option == '1'):
        os.rename(fileLink, newFileLink)
    elif (option == '2'):
        move(fileLink, newFileLink)
    elif (option == '3'):
        copyfile(fileLink, newFileLink)

# Run program
def run_program(option):
    # try:
    src_path = 'C:\Users\NGUYENXUANBANG\Desktop\MeowRealFile\data_test'
    dst_path = 'C:\Users\NGUYENXUANBANG\Desktop\MeowRealFile\data_source'
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
                newFileLink = make_new_file_link(fileLink, filename, real_file_extension, dst_path)
            else:
                COUNT_FILE_SUCCESS += 1
                newFileLink = make_new_file_link(fileLink, filename, real_file_extension, '-1')
            handling(option, fileLink, newFileLink)
    print("------------------------ COUNT PERSEN SUCESSFULL ----------------------------------")
    print("COUNT_FILE_SUCCESS/TOTAL_FILE = " + str(COUNT_FILE_SUCCESS) + " / " + str(TOTAL_FILE))
    print("-----------------------------------------------------------------------------------")
    # except:
    #     print("ERROR")
    
run_program(1)