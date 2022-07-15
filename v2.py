import getpass, os, subprocess, time, sys, requests

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

HWIDList = requests.get("https://pastebin.com/raw/wZwDKRyU")

Usernames = requests.get("https://pastebin.com/raw/RKjW2Qkr") 

Passwords = requsts.get("https://pastebin.com/raw/CrMXVjAY")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

l = ['|', '/', '-', '\\']
for i in l+l+l:
    clear()
    print("Loading..." + i)
    time.sleep(0.2)

clear()
Username = input("Enter a Username -> ")
# if Username == "User":
if Username in str(Usernames.text):

   pass

else:

    print("UserName is Invalid")
    os._exit(1)

print("Checking Your hwid...")

if hwid in str(HWIDList.text):

   print("hwid - Ok.")

else:

   print("HWID is Attempt")
   os._exit(1)

Password = getpass.getpass("Enter a Password -> ")

# if Password == "Y0u are H4cker?":
if Password in str(Passwords.text)

   print("wow, Noice Crack,\nYour so Pro.")

else:

   print("Password is Invalid.")
   os._exit(1)
