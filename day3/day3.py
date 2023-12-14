file = open("input.txt", "r")
lines = file.readlines()
file.close()
special = set('''@,#,$,%,&,*,-,+,=,/''')

def get_complete_number(line, index):
    # Known that line[index] is a digit. Check if chars before and chars after are also digits and returns the complete number
    num = int(line[index])
    tens = 1
    if line[index-1].isdigit():
        if 0 < index < len(line):
            while line[index-1].isdigit():
                num = (10*tens)*int(line[index-1]) + num
                index -= 1
                tens *= 10
    elif line[index+1].isdigit():
        if 0 <= index < len(line)-1:
            while line[index+1].isdigit():
                num = 10*num + int(line[index+1])
                index += 1
    return num

for line in lines:
    print(line.strip())
print("="*10)

sum = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char in special:
            # Checks left and right of special character
            if 0 < j < len(line)-2:
                if line[j+1].isdigit():
                    sum += get_complete_number(line, j+1)
                elif line[j-1].isdigit():
                    sum += get_complete_number(line, j-1)

            # Checks top and bottom including diagonals
            if i > 0 and 0 < j < len(line)-2:
                prev_line = lines[i-1][j-1:j+1]
                prev_line_index = j-1
                for n in range(3):
                    if prev_line[prev_line_index + n].isdigit():
                        sum += get_complete_number(prev_line, prev_line_index + n)



            next_line = lines[i+1][j-1:j+1]

print(sum)
