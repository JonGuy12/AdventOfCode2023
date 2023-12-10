file = open("input.txt", "r")
lines = file.readlines()
file.close()

sum = 0
maxR = 12
maxG = 13
maxB = 14

for line in lines:
    flag = True
    id = int(line.split(":")[0].split(" ")[1])
    rounds = line.split(":")[1].split(";")

    for round in rounds:
        colors = round.split(",")

        for color in colors:
            choice = color.strip().split(" ")
            match choice[1]:
                case "red":
                    if int(choice[0]) > maxR:
                        flag = False
                case "green":
                    if int(choice[0]) > maxG:
                        flag = False
                case "blue":
                    if int(choice[0]) > maxB:
                        flag = False
    if flag:
        sum += id

print(sum)