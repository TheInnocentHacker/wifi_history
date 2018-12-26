from winreg import *
import binascii

net=r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
key=OpenKey(HKEY_LOCAL_MACHINE,net)
print("\n[*] Networks You have joined -->>\n")
print("[*]\t\tAccess Point\t|\tMAC Address")
print("--"*40)
for i in range(25):
    try:
        guid=EnumKey(key,i)
        netKey=OpenKey(key,str(guid))
        (n,name,t)=EnumValue(netKey,1)
        (n,addr,t)=EnumValue(netKey,5)
        try:
            addr=binascii.hexlify(addr).decode()
        except TypeError:
            pass
        print("\t[+] "+name+"\t:\t"+str(addr))
        CloseKey(netKey)
    except:
       continue

    
