#!/usr/bin/env python3
from urllib.request import Request, urlopen
from itertools import product
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
    
    #with open("edited.txt", "r") as f:lines = f.readlines()
    #lines = [x.strip() for x in lines]
    alphanum = "abcdefghijklmnopqrstuvwxyz"
    lines = [''.join(i) for i in product(alphanum, repeat = 3)]

    print("Beginning check for avaliable names...\n")

    for x in lines:
        try:
            r = "http://namemc.com/name/" + x
            u = Request(r, headers={'User-Agent': 'Mozilla/5.0'})
            url = str(urlopen(u).read())
            if "Unavailable" not in url:
                if "Blocked" in url:print("   Blocked: " + x)
                elif "Available Later" in url:
                    print("      Soon: " + x)
                    with open("soon.txt", "a+") as f:f.write("{}\n".format(x))
                else:
                    print("\n************** AVALIABLE **************: " + x + "\n")
                    with open("found.txt", "a+") as f:f.write("{}\n".format(x))
                    continue
            else:print("Unavaiable: " + x)
        except Exception as e:
            print(e)

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
