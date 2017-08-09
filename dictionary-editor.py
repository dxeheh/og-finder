with open("original.txt", "r") as f:lines = f.readlines()
lines = [x.strip() for x in lines]
out = []
for x in lines:
    if len(x) > 2:
        out.append(x)
with open("edited.txt", "w+") as f:
    for x in out:
        f.write(x + "\n")
    print("Done")
