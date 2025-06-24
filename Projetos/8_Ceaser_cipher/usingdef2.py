def calculate_love_score(name_1, name_2):
    true = 0
    love = 0
    for letters in name_1.lower():
        if letters in ["t","r","u","e"]:
            true += 1
        if letters in ["l","o","v","e"]:
            love += 1

    for letters in name_2.lower():
        if letters in ["t","r","u","e"]:
            true += 1
        if letters in ["l","o","v","e"]:
            love += 1

    print(str(true) + str(love))

calculate_love_score(input("Name 1: "), input("Name 2: "))
    