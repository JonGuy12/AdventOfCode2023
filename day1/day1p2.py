result = 0
with open("input.txt", "r") as lines:
    for line in lines:
        digits = []
        for index, char in enumerate(line):
            if char.isdigit():
                digits.append(int(char))
            else:
                match char:
                    case 'o':
                        if len(line) >= index + 3:
                            if line[index:index + 3] == "one":
                                digits.append(1)
                    
                    case 't': #two and three
                        if len(line) >= index + 3 and line[index:index + 3] == "two":
                                digits.append(2)
                        if len(line) >= index + 5 and line[index:index + 5] == "three":
                            digits.append(3)
                            
                    case 'f': #four and five
                        if len(line) >= index + 4:
                            if line[index:index + 4] == "four":
                                digits.append(4)
                            elif line[index:index + 4] == "five":
                                digits.append(5)

                    case 's': #six and seven
                        if len(line) >= index + 3 and line[index:index + 3] == "six":
                                digits.append(6)
                        if len(line) >= index + 5 and line[index:index + 5] == "seven":
                                digits.append(7)

                    case 'e':
                        if len(line) >= index + 5:
                            if line[index:index + 5] == "eight":
                                digits.append(8)
                    case 'n':
                        if len(line) >= index + 4:
                            if line[index:index + 4] == "nine":
                                digits.append(9)
        print(digits)
        if len(digits) != 0:
            result += 10 * digits[0] + digits[-1]
    print(result)