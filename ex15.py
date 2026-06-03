from sys import argv

script, filename = argv

txt = open(filename)  # abre o arquivo filename

print(f"Here's your file {filename}:")
print(txt.read())   # use o método read (sem parametros ou default) na variavel txt
txt.close()
