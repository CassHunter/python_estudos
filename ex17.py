from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}")

# # poderíamos fazer esses dois com uma linha, como?
# in_file = open(from_file)
# indata = in_file.read()

# print(f"The input file is {len(indata)} bytes long.")
# print("Ready, hit ENTER to continue, CTRL-C to abort.")
# input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print('Alright, all done.')

# out_file.close()
# in_file.close()

# formato moderno, fechamento automatico
with open(from_file, 'r') as f:
    indata = f.read()

with open(to_file, 'w') as f:
    f.write(indata)