def greet_me (name):
    print("Hello ", name)
    print("I see you, ", name)
    print("Whaha ", name)

def life_in_weeks(age):
    age = 90 - int(age)
    weeks = int(age) * 52
    print(f"You have {weeks} weeks left.")

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


greet_me("Pedro")

life_in_weeks(input("How old are you? "))



calculate_love_score("Kanye West", "Kim Kardashian")
    
    
