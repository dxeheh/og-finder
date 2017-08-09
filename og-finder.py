#!python3
from urllib.request import Request, urlopen
import urllib.request, os, sys

def clearScreen():
    if sys.platform == 'win32':os.system('cls')
    else:os.system('clear')

clearScreen()
print("Importing edited dictionary...\n")

with open("edited.txt", "r") as f:lines = f.readlines()
lines = [x.strip() for x in lines]

clearScreen()
print("Beginning check for avaliable names...\n")

found = []
for x in lines:
    r = "http://mine.ly/" + x + ".1"
    u = Request(r, headers={'User-Agent': 'Mozilla/5.0'})
    url = urlopen(u).geturl()
    if "profile" not in url:
        print("Name avaliable: " + x)
        found.append(x)

print("\nDone.\n")
input("Press enter to continue...")

