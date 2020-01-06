import os

def getIndexByName(name,src):
    for i in range(len(src)):
        if name in src[i]:
            return i
def getLanguage():
    with open("1.txt","r") as f:
        src=f.readlines()
        start=getIndexByName("Language",src)
        for i in range(start,len(src)):
            if "*" in src[i]:
                return src[i].strip()[1:]
def getSataEmu():
    with open("1.txt","r") as f:
        src=f.readlines()
        start=getIndexByName("SATA Emulation",src)
        for i in range(start,len(src)):
            if "*" in src[i]:
                return src[i].strip()[1:]
def getRemoveMedia():
    with open("1.txt","r") as f:
        src=f.readlines()
        start=getIndexByName("Removable Media Boot",src)
        for i in range(start,len(src)):
            if "*" in src[i]:
                return src[i].strip()[1:]
def getVersion():
    with open("1.txt","r") as f:
        src=f.readlines()
        start=getIndexByName("Version",src)
        return src[start+1].strip()
def getProductName():
    with open("1.txt","r") as f:
        src=f.readlines()
        start=getIndexByName("Product Name",src)
        return src[start+1].strip()
def getManufacturer():
    with open("1.txt","r") as f:
        src=f.readlines()
        start=getIndexByName("Manufacturer",src)
        return src[start+1].strip()
def setVersion():
    src1=""
    os.rename("1.txt","tmp.txt")
    with open("tmp.txt",'r') as f:
        src=f.read()
        sizesrc=len(src)
        print(sizesrc)
        src1=src.replace("L01 v02.33","L01 v02.44")
        f.close()
    os.remove("tmp.txt")
    with open("1.txt",'a') as f1:
        f1.write(src1)
        f.close()
def setLang():
    os.rename("1.txt","tmp.txt")
    with open("tmp.txt",'r') as f:
        src=f.readlines()
        start=getIndexByName("Setup Language",src)
        for i in range(start,len(src)):
            if "*" in src[i]:
                src[i]=src[i].replace("*","")
                break
        for i in range(start,len(src)):
            if "French" in src[i]:
                src[i]=src[i].replace("French","*French")
        f.close()
    with open("1.txt",'a') as f1:
        f1.writelines(src)
        f1.close()
    os.remove("tmp.txt")
def setSataEmu():
    data="AHCI"
    os.rename("1.txt", "tmp.txt")
    with open("tmp.txt", 'r') as f:
        src = f.readlines()
        start=getIndexByName("SATA Emu",src)
        for i in range(start,len(src)):
            if "*" in src[i]:
                src[i]=src[i].replace("*","")
                break
        for i in range(start,len(src)):
            if "AHCI" in src[i]:
                src[i]=src[i].replace("AHCI","*AHCI")
                break
        f.close()
    with open("1.txt",'a') as f1:
        f1.writelines(src)
        f1.close()
    os.remove("tmp.txt")
def setRemoveableMedia():
    os.rename("1.txt", "tmp.txt")
    with open("tmp.txt", 'r') as f:
        src = f.readlines()
        start=getIndexByName("Removable Media",src)
        print(start)
        for i in range(start,len(src)):
            if "*" in src[i]:
                src[i]=src[i].replace("*","")
                break
        for i in range(start,len(src)):
            if "Disable" in src[i]:
                src[i]=src[i].replace("Disable","*Disable")
                break
        f.close()
    with open("1.txt",'a') as f1:
        f1.writelines(src)
        f1.close()
    os.remove("tmp.txt")
setRemoveableMedia()
setSataEmu()
setLang()
