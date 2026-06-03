from sys import argv
# argv é muito usado para criar programas q recebem parâmetros pelo terminal
# argv é uma lista, argv[0]= <nome do arquivo>, argv[1]=arg1, argv[2]=arg2, ...
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)