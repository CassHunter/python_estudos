#----------- 1º versão
# i = 0
# numbers = []

# while i < 6:
#     print(f'At the top i is {i}')
#     numbers.append(i)

#     i += 1
#     print(f'Numbers now: {numbers}')
#     print(f'At the bottom i is {i}')


#     print('The numbers: ')

#     for num in numbers:
#         print(num)


#---------- 2° versão
# numbers = []
# for i in range(6):
#     print(f'At the top i is {i}')
#     numbers.append(i)

#     i += 1
#     print(f'Numbers now: {numbers}')
#     print(f'At the bottom i is {i}')


#     print('The numbers: ')

#     for num in numbers:
#         print(num)

#------------- função
def contagem(limite):
    i = 0
    numbers = []

    while i < limite:
        print(f'At the top i is {i}')
        numbers.append(i)

        i += 1
        print(f'Numbers now: {numbers}')
        print(f'At the bottom i is {i}')


        print('The numbers: ')

        for num in numbers:
            print(num)