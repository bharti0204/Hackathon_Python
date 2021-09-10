#first read the file and create the players hands
#then make an if that checks what does each playes has

P1_hand = "8C TS KC 9H 4S"
P1_suits = ["C", "S", "C", "H", "S"]
P1_num = ["8", "T", "K", "9", "4"]
P2_hand = "7D 2S 5D 3S AC"
P2_suits = ["D", "S", "D", "S", "C"]
P2_num = ["7", "2", "5", "3", "A"]

def convert_to_number(input_list):
    output_list = [0,0,0,0,0]
    j = 0
    x = 0
    for i in input_list:
        if i not in ["T","J","Q","K","A"]:
            x = int(i)
        elif i == "T":
            x = 10
        elif i == "J":
            x = 11
        elif i == "Q":
            x = 12
        elif i == "K":
            x = 13
        elif i == "A":
            x = 14
        output_list[j] = x
        j = j + 1

    return output_list


def flush(suit):
    if (suit[0] == suit[1] == suit[2] == suit[3] == suit[4]):
        return True
    else:
        return False

suit_test = ['H', 'H', 'H','H','H']
print(flush(suit_test))

print(convert_to_number(P1_num))

