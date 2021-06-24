import random

abc = [
    "A",
    "a",
    "B",
    "b",
    "C",
    "c",
    "D",
    "d",
    "E",
    "e",
    "F",
    "f",
    "G",
    "g",
    "H",
    "h",
    "I",
    "i",
    "J",
    "j",
    "K",
    "L",
    "l",
    "M",
    "m",
    "N", 
    "n",
    "O",
    "o",
    "P",
    "p",
    "Q",
    "q",
    "R",
    "r", 
    "S",
    "s",
    "T",
    "t",
    "U",
    "u",
    "V",
    "v",
    "W",
    "w",
    "X",
    "x",
    "Y",
    "y",
    "Z",
    "z"]

for i in range(1,3):
    print("use numbers")
    print("Use letters")
    print("Pick one!")
choice = input("> ")

if choice in ("number","numbers"):
    password = []
    for i in range(0,21):
        x = ["1","2","3","4","5"]
        password.extend(random.choice(x))
if choice in ("letter","letters"):
    password = []
    for i in range(0,21):
        password.extend(random.choice(abc))

print("".join(password))
