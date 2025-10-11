def life_in_weeks(age):
    age = 90 - int(age)
    weeks = int(age) * 52
    print(f"You have {weeks} weeks left.")

print("What if you die with 90 years old?")
print("Do you know how many weeks of life would you have?\n ")

life_in_weeks(input("How old are you? "))