#!python3
import urllib.request
import itertools
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

    for x in lines:
        try:
            r = urllib.request.urlopen("https://api.mojang.com/users/profiles/minecraft/" + x)
            if 'name' in str(r.read()):print("Unavaiable: " + x)
            else:
                print("\n************** AVALIABLE **************: " + x + "\n")
                with open("found.txt", "a+") as f:f.write("{}\n".format(x))
        except Exception as e:print(e)
            

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

