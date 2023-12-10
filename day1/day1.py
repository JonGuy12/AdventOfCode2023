result = 0
with open("input.txt", "r") as lines:
    for line in lines:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        if len(digits) != 0:
            result += int(digits[0] + digits[-1])
    print(result)