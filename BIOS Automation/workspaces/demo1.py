import os,sys
import ftplib

'''
ftpserver
username/password
items

'''
def runcmd(command):
    rs=os.popen(command).read()
    return rs

def readtxt(path):
    with open(path,'r') as f:
        rs=f.read()
        f.close()
    return rs

def write2txt(src,path):
    with open(path,'w') as f:
        f.write(src)
        f.close()

def changeauto(file_old,file_new,flag):
    src_old=readtxt(file_old)
    #...

    src_new=src_old
    write2txt(src_new,file_new)

def change_usb_type(file,flag):
    pass
def logfile(file,txt):
    pass

def upload2ftp(file):
    username=username
    password=passwd
    #uplaod code
    pass
def report_result(mail_addr,files):
    pass
def checkconfig(file,item):
    runcmd("bcu.exe /get:config.txt")
    if item=="auto":
        pass
    elif item=="usbtype":
        #check config.txt usbtype=="123"
        logfile("result.txt","usbtype:PASS")
        pass
    elif item=="version":
        #check config.txt version=="preset"
        #check local machine version=="preset"
        pass
# changeauto("config.txt","config_auto_enable.txt")
# runcmd("bcu.exe /set:config_auto_enable.txt")
# runcmd("shutdown -r -t 0")
# checkconfig("BiosVersion")
# checkconfig()
s1="v1.0.3"
s2="v1.0.2"
print(s1<s2)