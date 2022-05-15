a = input('Digite algo: ') # a função imput sempre retornará uma string por padrão. Se quiser outro tipo primitivo deve converte-lo primeiro. Ex: int(input('teste: '))
print('O tipo primitivo desse valor é: ',type(a)) # valida o tipo primitivo
print('Só tem espaços? {}'.format(a.isspace())) # retorna um bolleano, valida se possue somente espaços
print('Is this a number? {}'.format(a.isnumeric())) # retorna um bolleano, valida se possue somente números
print('Is this a letter? {}'.format(a.isalpha())) # retorna um bolleano, valida se possue somente letras
print('Está em alfanumérico {}'.format(a.isalnum())) # retorna um bolleano, valida se possue somente letras
print('Esta em letras maiúsculas? {}'.format(a.isupper())) # retorna um bolleano, valida se todas as letras são maiúsculas
print('Esta em letras minusculas? {}'.format(a.islower())) # retorna um bolleano, valida se todas as letras são minusculas
print('Esta em letras capitalizado? {}'.format(a.istitle())) # retorna um bolleano, valida se existe letras maiúsculas e minúsculas
