file = open("input.txt", "r")
lines = file.readlines()
file.close()

power = 0

for line in lines:
    flag = True
    tempMaxR = 0
    tempMaxG = 0
    tempMaxB = 0
    id = int(line.split(":")[0].split(" ")[1])
    rounds = line.split(":")[1].split(";")

    for round in rounds:
        colors = round.split(",")

        for color in colors:
            choice = color.strip().split(" ")
            match choice[1]:
                case "red":
                    tempMaxR = max(tempMaxR, int(choice[0]))
                case "green":
                    tempMaxG = max(tempMaxG, int(choice[0]))
                case "blue":
                    tempMaxB = max(tempMaxB, int(choice[0]))
    power += tempMaxR * tempMaxG * tempMaxB

print(power)