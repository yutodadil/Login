import getpass, os, subprocess, time, sys, requests
print("imported Module")
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
print("Getting HWID")

#ここは分かりやすくpastebinを使用していますが、repl.itでtxtとかを使ってやった方が絶対いいです。	

HWIDList = requests.get("https://pastebin.com/raw/wZwDKRyU")

if HWIDList.status_code == 200:

    print("Connected HwidDataBase")

else:

    print("Network Error, or HwidDataBase is Down.\n if your Network is Not Downd to Please Contact me \nDiscord YourName#Tag\nTelegram t.me/YourID\nTwitter @YourAccount") 
    os._exit(1)

Usernames = requests.get("https://pastebin.com/raw/RKjW2Qkr") 

if Usernames.status_code == 200:

    print("Connected UserNameDataBase")

else:

    print("Network Error, or UserNameDataBase is Down.\n if your Network is Not Downd to Please Contact me \nDiscord YourName#Tag\nTelegram t.me/YourID\nTwitter @YourAccount") 
    os._exit(1)

Passwords = requests.get("https://pastebin.com/raw/CrMXVjAY")

if Passwords.status_code == 200:

    print("Connected PasswordDataBase")

else:

    print("Network Error, or PasswordDataBase is Down.\n if your Network is Not Downd to Please Contact me \nDiscord YourName#Tag\nTelegram t.me/YourID\nTwitter @YourAccount") 
    os._exit(1)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

l = ['|', '/', '-', '\\']
for i in l+l+l:
    clear()
    print("Loading..." + i)
    time.sleep(0.2)

clear()
Username = input("Enter a Username -> ")
Password = getpass.getpass("Enter a Password -> ")
# if Username == "User":
if Username in str(Usernames.text):

   pass

else:

    print("UserName or Password is Invalid")
    os._exit(1)

print("Checking Your hwid...")

if hwid in str(HWIDList.text):

   print("hwid - Ok.")

else:

   print("HWID is Attempt")
   os._exit(1)

# if Password == "Y0u are H4cker?":
if Password in str(Passwords.text):

   print("Welcome to Program")

else:

   print("UserName or Password is Invalid")
   os._exit(1)

#Code Here
