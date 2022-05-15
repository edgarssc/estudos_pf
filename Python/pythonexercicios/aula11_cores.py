# \033[ codstyle; codtext; codback m Ex: \033[0;33;44m

# list code style: 0-none; 1-bold; 4-underline; 7-negative
# list code text: 30-branco; 31-vermelho; 32-verde; 33-amarelo; 34-azul; 35-roxo; 36-azulclaro; 37-cinza
# list code back: 40-branco; 41-vermelho; 42-verde; 43-amarelo; 44-azul; 45-roxo; 46-azulclaro; 47-cinza
a=3
b=5
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print("\nOs valor de a e b são \033[1;31m{}\033[m e \033[1;36m{}\033[m!!!\n".format(a,b))
print("Os valor de a e b são {}{}{} e {}{}{}!!!\n".format('\033[1;31m',a,'\033[m','\033[1;31m',b,'\033[m'))
print("Os valor de a e b são {}{}{} e {}{}{}!!!\n".format(cores['azul'],a,cores['limpa'],cores['amarelo'],b,cores['limpa']))