#TYPE HINTS

def drive_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(drive_check(12))

#Especifica o tipo de dados que o parametro é e que o método retorna