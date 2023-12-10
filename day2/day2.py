with open("input.txt", "r") as lines:
    maxR = 12
    maxG = 13
    maxB = 14

    for line in lines:
        id = int(line.split(":")[0].split(" ")[1])
        colors = line.split(":")[1].split(";")

        for color in colors:
            print(color)