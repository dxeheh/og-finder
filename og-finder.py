#!python3
from urllib.request import Request, urlopen
import os, sys

def clearScreen():
    if sys.platform == 'win32':os.system('cls')
    else:os.system('clear')
    print("og-finder v1.3\ndeveloped by dxeheh\n\n")

def end():
    input("\nPress enter to continue...")
    quit()

def edit():
    clearScreen()

    if not os.path.isfile("original.txt"):
        print("original.txt is missing from the current directory. Please restart when it is present.")
        end()

    mi = input("Enter minimum name length (min. 3):\n")
    ma = input("Enter maximum name length (max. 16):\n")
    
    with open("original.txt", "r") as f:lines = f.readlines()
    lines = [x.strip() for x in lines]
    out = []
    for x in lines:
        if len(x) >= int(mi):
            if len(x) <= int(ma):
                out.append(x)
    with open("edited.txt", "w+") as f:
        for x in out:
            f.write(x + "\n")

    clearScreen()
    print("Dictionary successfully created")
        
def search():
    clearScreen()

    if not os.path.isfile("edited.txt"):
        print("You have not yet created a dictionary. Please select the first option.")
        return
    
    with open("edited.txt", "r") as f:lines = f.readlines()
    lines = [x.strip() for x in lines]

    print("Beginning check for avaliable names...\n")

    found = []
    for x in lines:
        r = "http://mine.ly/" + x + ".1"
        u = Request(r, headers={'User-Agent': 'Mozilla/5.0'})
        url = urlopen(u).geturl()
        if "profile" not in url:
            if "Blocked" not in str(urlopen(u).read()):
                print("\n************** AVALIABLE **************: " + x + "\n")
                with open("found.txt", "w+") as f:f.write(x + "\n")
            else:
                print("   Blocked: " + x)
                continue
        else:print("Unavaiable: " + x)

    print("\nDone.\nNames found have been written to found.txt.\n")
    end()


def main():    
    clearScreen()
    while True:
        c = input("1. Create dictionary\n2. Begin search\n")
        if c == "1":
            edit()
        elif c == "2":
            search()
        else:
            clearScreen()
            print("Please select a valid option.")
        
if __name__ == "__main__":
    main()

