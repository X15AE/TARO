

date_of_birth = "28.10.1986"
sacral_number = 22
date_items = date_of_birth.split(".")
#print(date_items)
day_of_birth = date_items[0]
print(day_of_birth)


def get_birth_card(day, sacral):
    #print("start")
    day_number = int(day)
    if day_number > sacral:
        return day_number - sacral
    else:
        return day_number

birth_card = get_birth_card(day_of_birth,sacral_number)
print( "Карта рождения" +" =  " + str(birth_card))

def get_numbers_from_string(day):
    # print("start")
    str_len = len(day)
    print (str_len)
    print(day)
    numbers = []
    for i in range (str_len):
        #print(i)
        print(day[i])
        item = day[i]
        if item.isdigit():
            numbers.append(int(item))
    print(numbers)
    return numbers


items_card_of_fate = get_numbers_from_string(date_of_birth)
print(card_of_fate)












