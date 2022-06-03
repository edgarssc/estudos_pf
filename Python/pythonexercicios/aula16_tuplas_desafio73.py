tabela = ("santos", "botafogo", "fluminense", "atletico",
 "são paulo", "bahia", "gremio", "internacional", "palmeiras",
  "atletico-pr", "vasco", "corinthians", "flamengo", "cruzeiro")
separador = "-" * 40
print(separador)
print("Os cinco primeiros são: {} ".format(tabela[0:5]))
print(separador)
print("Os quatro últimos são: {} ".format(tabela[-4:]))
print(separador)
print("Os times em ordem alfabética: {} ".format(sorted(tabela)))
print(separador)
print("O Bahia está na posição {} ".format(tabela.index("bahia")))
print(separador)