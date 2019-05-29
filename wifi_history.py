from winreg import *
import binascii


print(" __          ___ ______ _   _    _ _     _                   ")
print(" \ \        / (_)  ____(_) | |  | (_)   | |                  ")
print("  \ \  /\  / / _| |__   _  | |__| |_ ___| |_ ___  _ __ _   _ ")
print("   \ \/  \/ / | |  __| | | |  __  | / __| __/ _ \| '__| | | |")
print("    \  /\  /  | | |    | | | |  | | \__ \ || (_) | |  | |_| |")
print("     \/  \/   |_|_|    |_| |_|  |_|_|___/\__\___/|_|   \__, |")
print("                       ______                           __/ |")
print("                      |______|                         |___/ ")
print()
print("Author: Vaibhav Kush")
print()
try:
	key=OpenKey(HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged',0,KEY_READ | KEY_WOW64_64KEY)
except FileNotFoundError:
	key=OpenKey(HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged',0,KEY_READ | KEY_WOW64_32KEY)
print("[+] Here's the list of networks you have joined till date:\n")
print("[*]\tAccess Point\t|\tMAC Address")
print("--"*30)
for i in range(500):
    try:
        guid=EnumKey(key,i)
        netKey=OpenKey(key,str(guid))
        (n,name,t)=EnumValue(netKey,1)
        (n,addr,t)=EnumValue(netKey,5)
        try:
            addr=binascii.hexlify(addr).decode()
        except TypeError:
            pass
        print("\t[+]",name,":",str(addr))
        CloseKey(netKey)
    except:
       continue

    
