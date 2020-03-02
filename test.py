import rarfile
import zipfile

# zFile = zipfile.ZipFile('/Users/deng/Desktop/network attack&defense/program/zipcrack/1.zip')
rFile = rarfile.RarFile('/Users/deng/Desktop/network attack&defense/program/zipcrack/password.rar')
# passFile = open('/Users/deng/Desktop/network attack&defense/program/zipcrack/pass.txt')
passFile = open('/Users/deng/Desktop/network attack&defense/program/zipcrack/password.txt')
for line in passFile.readlines():
    password = line.strip ('\n')
    passwd_list=password.split()
    for i in range(4):
        try:
            # print(passwd_list[i])
            # zFile.extractall(pwd=passwd_list[i].encode("ascii"))
            rFile.extractall(pwd=passwd_list[i])
            print ('[+] Password ='+ passwd_list[i] +'\n')
            exit(0)
        except Exception as e:
            pass
