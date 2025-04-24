
def format_name(f_name, l_name):
    """It makes every name starts with Upper Case"""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"




print(format_name(input("First name: "), input("Last name: ")))


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
               return True
            else:
                return False    
        else: 
            return True
    else:
        return False
        


print(is_leap_year(int(input("Year: "))))

len()

