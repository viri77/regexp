"""проверить содержит ли пароль хотя бы 1 заглавную букву, 1  строчную букву,1  цифру
,имеет длину 10 и  больше,содержит только буквы и  цифры"""

"""one lowercase letter,one uppercase letter,at least one digit,contains only digit and letters"""

from re import findall

password="Djgggggggggg1"
pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[0-9a-zA-Z]{10,}$"
result = findall(pattern,password)
if result:
    print("valid")
else:
    print("invalid")
