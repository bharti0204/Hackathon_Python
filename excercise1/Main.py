import os

def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman:
            num += roman[s[i:i + 2]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1
    return num

def int_to_Roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        #print(i)
        for j in range(num // val[i]):
            #print(range(num // val[i]))
            #print(f"in the for loop for {i}")
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

path = f'Hackathon_Python{os.sep}'
filename = 'roman.txt'
print(path+filename)
savings = 0
with open(path + filename, 'r') as input_file:
    for line in input_file.readlines():
        line = line.strip()
        count1 = len(line)
        number1 = romanToInt(line)
        number2 = int_to_Roman(number1)
        count2 = len(number2)
        savings = (count1 - count2)+savings
print('The character savings is: ' +str(savings))


