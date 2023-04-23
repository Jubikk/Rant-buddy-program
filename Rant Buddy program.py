#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.4 Exercise 3
filename = "mylife.txt"

with open(filename, "w") as file:
    while True:
        line = input("Hi, how are you? Wanna tell me something? ")
        file.write(line + "\n")
        another_lines = input("Wanna tell me more? y/n? ")
        if another_lines.lower() != "y":
            break

print("TEXT WAS SAVED IN", filename)


