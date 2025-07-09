print("helllo")

try:
    name = int(input("what is your name? "))
except EOFError:
    print("No input received (EOF).")
except KeyboardInterrupt:
    print("input cancelled (cntrl+C).")
print("welcome ", name)