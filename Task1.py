# Task1.Week3 HOMEWORK ----> ATABEK

# 1)
# year = input('Enter a vysokosnyi god: ')
# a = ('29.02.2019')
# if year == a:
#     print('Год является високосным')
# else:
#     print('Год не является високосным')

# 2)
# give_number = (input('Enter your number: '))
# if give_number.isdigit():
#     give_number = int(give_number)
#     if give_number % 3 == 0 and give_number % 5 == 0:
#         print('HahaHoo')
#     elif give_number % 3 == 0:
#         print('Haha')
#     elif give_number % 5 == 0:
#         print('Hoho')
#     else:
#         print('Aaaa')

# 3)
# number = input('Enter your number: ')
# number2 = input('Enter your second number: ')
# if number.isdigit() and number2.isdigit():
#     number = int(number)
#     number2 = int(number2)
#     number3 = number + number2
#     if number3 < 5:
#         print('Summa chisel menshe 5!')
#     elif number3 == 5:
#         print('Summa chisel ravno 5!')
#     elif number3 > 5:
#         print('Summa chisel bolshe 5!')
#     else:
#         print('Please write correct!')

# 4)
# a. 11 == 11 and 2 == 1 # pervoe vyrojeniye True, Vtoroe False 
# b. 'compare' == 'compare'  # vyrojeniye vernoe True
# c. 11 == 11 or 22 != 100     # Pervoe vyrojeniye True, vtoroe toje True
# d. True and True        # Of course True
# e. False and True      # itog budet False iz za logicheskogo vyrajeniya 'and'
# f. True and 3 == 3     # Pervoe budet True, vtoroe toje budet True
# g. False and 42 != 42    # Pervoe budet False, vtoroe toje False
# h. True or 13 == 13      # pervoe budet True, vtoroe toje budet True.
# i. 'swimming' == 'testing'      # Vyrajeniye budet False
# j. 'tester'!= 'testing'      # vyrajeniye budes True, because 'tester' is not equal to 'testing
# k. 'test' == '123'     # budet False
# l. 12 != 0 and 22 == 1      # pervoe budet True, vtoroe budet False
# m. not (True and False )      # itog budet False
# n. not (1 == 1 and 0 != 1)     # vyrajeniye budet False, because 1==1
# o. not(105 == 4 or 101 == 101)     # Vyrajeniye budet False, because 101 == 101
# p. not (11 != 101 or 7 == 4)      # Budet Ture, because its true that 11!=101 and 7==4
# q. not('testing' =='testing' and 'Ted' == 'Fool guy')    # Pervoe budet False, vtoroe budet True
# r. 8 == 4 and not('wrestling' == 1 or 4 == 0)      # pervoe budet True, vtoroy budet Ture, itog budet false
# s. 'spam' == 'bacon' and not(3 == 4 or 7 == 7)      # pervoe budet False, vtoroe budet False
# t. 6 == 6 and not('tdd' == 'tdd' or 'Python' == 'Super')     # Pervoe budet True, vtoroe budet True, itog budet True

# 5)
# number = input('Enter the number: ')
# if number.isdigit():
#     number = int(number)
#     if number < 0:
#         print(-1)
#     elif number >= 0:
#         print(1)
#     elif number == 0:
#         print(0)
# elif number == 0:
#     print(0)
# elif number.isdigit() is False:
#     print(-1)
# else:
#     print('ERROR')

# 6)
# alphabit = input("Vvedite slovu: ")
# bukva = input("Vvedite bukvu: ")
# if alphabit.count(bukva) == 1:
#     print(f"индекс подстроки {alphabit.find(bukva)}.")
# elif alphabit.count(bukva) >= 2:
#     print(f"индекс первого вхождения {alphabit.find(bukva)}, индекс последнего вхождения {alphabit.rfind(bukva)}")

# 7)
# a = input("введите атора: ").title()
# books = {"Джек Лондон": "Зов природы", "Стивен Кинг": "Темная башня", "Никколо Макиавелли": "Государь"}

# if a in books:
#     print(f"Название книги: {books[a]}")
# elif a not in books:
#     print("назовите книгу: ")
#     naz = input().capitalize()
#     books[a] = naz
#     print(books)
 













