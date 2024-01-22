#Test it! <-- Shreeraj Shrestha

import time
import re

redirect = "127.0.0.1"
hosts_file = r"C:\Windows\System32\drivers\etc\hosts"

def validate_domain_name(domain_name):
    # Check the overall length of the domain name, should not exceed 253 characters
    if len(domain_name) > 253:
        return False

    # Regular expression pattern to validate domain name:
    #   - (?!-) ensures that the label doesn't start with a hyphen
    #   - [A-Za-z0-9-]{1,63} ensures that the label contains 1 to 63 alphanumeric characters or hyphens
    #   - (?<!-) ensures that the label doesn't end with a hyphen
    #   - \. matches a dot between labels
    #   - [A-Za-z]{2,} matches a two or more character top-level domain (TLD)
    pattern = r'^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,}$'

    # Check if the domain name matches the pattern
    if re.match(pattern, domain_name):
        return True
    else:
        return False


def block(newBlock):

    with open(hosts_file,"r") as file:
        contents = file.read()

    with open(hosts_file,"a") as file:
        if newBlock in contents:
                pass
        #if not blocked then blocked it
        else:
            try:
                file.write(f"{redirect} {newBlock} \n")

            except PermissionError:
                print('\nPlease follow the following steps to grant permission to run this program:\n\n*First try running the program as administrator*\n\n--> Go to C:\\Windows\\System32\\drivers\\etc.\n--> Right click on the "hosts" file.\n--> Click: properties>security>ALL RESTRICTED APPLICATION PACKAGES.\n--> Click on edit and then check all the boxes.\n--> Click "Apply" and then "Ok".\n\n--After following the above steps, try running the program again|!--\n')

def unblock(website):
    with open(hosts_file,"r") as file:
        lines = file.readlines()

    with open(hosts_file,"w") as file:
        check = 0
        for line in lines:
            if website not in line:
                file.write(line)

            else:
                check = 1
        if check != 1:
            print(f"{website} is not in the blocked list!")
            quit()

run = True

while run:
    cmd = input('\nWelcome to website blocker by "Team 7":\n\nb.To block a specific website\nu.To unblock a website\nq.Exit the program\n\n--> ').lower()
    
    if cmd == "b":
        
        newBlock = input("\nEnter the url of the website you want to block:\n")
        if validate_domain_name(newBlock):
            block(newBlock)
            print(f"\nBlocking {newBlock}....")
            time.sleep(5)
            print(f"{newBlock} is now blocked in your system!\n")
            run = False

        else:
            print("\nPlease enter proper domain name:\nwww.example.com....\n")
            time.sleep(2)
            continue

    elif cmd == "u":

        unblock_url = input("\nEnter the url of the website you want to unblock:\n")
        if validate_domain_name(unblock_url):
            unblock(unblock_url)
            print(f"\nunblocking {unblock_url}....")  
            time.sleep(5)
            print(f"{unblock_url} is now accessible!\n")
            run = False

        else:
            print("\nPlease enter proper domain name:\nwww.example.com....\n")
            time.sleep(2)
            continue

    elif cmd == "q":
        print("\nThank you for using this service!")
        quit()

    else:
        print("Please enter a valid command....\n")
        time.sleep(2)
        continue