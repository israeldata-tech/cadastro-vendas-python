# tam = int(input("digite o tamanho da lista "))
# lista = []
# for i in range(tam):
#     num = int(input(f"digite o número {i+1}"))
#     lista.append(num)
# maior = max(lista)
# menor = min(lista)


# soma = sum(lista)
# media = soma / tam
# print(f"soma {soma} media {media} maior {maior} menor {menor}")

# linguagens = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go"]
# print(f"{linguagens[0]}, {linguagens[5]}")
# print(f"{linguagens[1:4]}")
# print(f"{linguagens[::-1]}")

# frutas = ["maçã", "banana", "laranja"]
# frutas.append("uva")
# frutas.insert(0, "morango")
# frutas.remove("banana")
# removido = frutas.pop()
# print(f"{frutas} e {removido}")

# notas = [8.5, 4.0, 10.0, 7.5, 4.0, 9.0]
# notas.sort()
# print(f"{notas.count(4.0)} {notas.index(10.0)} {notas}")

# tarefas = ["Estudar Python", "Fazer compras", "Lavar o carro", "Treinar"]
# for indice in enumerate(tarefas):
#     print(f"{indice[0]+1}, {indice[1]}")

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# q = [num ** 2 for num in numeros]
# p = [num for num in numeros if num % 2 == 0]
# print(f"{q} {p}")

# tam = int(input("digite quantos números quer digitar "))
# lista = []
# for i in range(tam):
#     num = int(input(f"digite o numero {i+1}"))
#     lista.append(num)
# md = [num for num in lista if num > 10]
# m2 = [num * 2 for num in lista]
# print(f"{md} {m2}")

# q = int(input("quantas nomes quer cadastrar "))
# nomes = []
# for i in range(q):
#     nome = input(f"digite o nome {i+1}")
#     nomes.append(nome)
# f = [nome.capitalize() for nome in nomes]
# m5 = [nome for nome in nomes if len(nome) > 5]
# print(f"{f} {m5}")

# q = int(input("digite quantos números quer digitar "))
# numeros = []
# soma = 0
# for i in range(q):
#     num = float(input(f"digite o número {i+1} "))
#     numeros.append(num)
#     soma += num
# media = soma / q
# am = [num for num in numeros if num > media]
# print(f"{numeros} , {media:.2f} , {soma}, {am}")

# q = int(input("quantos números  "))
# nume = []
# for i in range(q):
#     num = float(input(f"digite o número {i+1}"))
#     nume.append(num)
# p = [num for i, num in enumerate(nume) if i % 2 == 0]
# print(f"{nume} {p}")

# q = int(input("quantos numeros "))
# nume = []
# for i in range(q):
#     num = float(input(f"{i+1}  "))
#     nume.append(num)
# c = [num * 10 if num % 2 == 0 else num for num in nume]
# print(f"{nume}, {c}")

# q = int(input("quantos produtos "))
# produtos = []
# for i in range(q):
#     p = float(input("digite o preço "))
#     produtos.append(p)
# promocao = [p * 0.9 if p > 100 else p for p in produtos]
# print(f"{produtos}, {promocao}")

# q = int(input("quantos nomes "))
# nomes = []
# for i in range(q):
#     n = input("digite o nome ")
#     nomes.append(n)
# nn = [n for n in nomes if n.lower().startswith("a") and len(n) > 3]
# print(f"{nomes} , {nn}")

# q = int(input("quantos alunos "))
# notas = []
# for i in range(q):
#     nota = float(input(f"digite a nota {i+1} "))
#     while nota < 0 or nota > 10:
#         print("nota invalida")
#         nota = float(input(f"digite a nota {i+1} "))

#     notas.append(nota)
# a = ["aprovado" if nota >= 7.0 else "reprovado" for nota in notas]
# b = [nota for nota in notas if nota > 8.0]
# print(f"original {notas}, situação {a}, bons {b}")

# q = int(input("digite o tamanho 1 "))
# a = int(input("digite o tamanho 2 "))

# b = []
# c = []

# for i in range(1, q+1):
#     num = float(input(f"digite {i} "))
#     b.append(num)
# for i in range(1, a+1):
#     num = float(input(f"digite {i} "))
#     c.append(num)

# l3 = b + c
# l3uni = []
# for num in l3:
#     if num not in l3uni:
#         l3uni.append(num)

# print(f"{b} {c} {l3} {l3uni}")

# q = int(input("digite o tamanho "))
# lista = []
# for i in range(1, q+1):
#     num = float(input(f"digite {i} "))
#     lista.append(num)
# nl = lista.copy()
# nl.pop()
# print(f"{lista} {nl[::-1]}")

# q = int(input("digite quantas pessoas tem a fila "))
# fila = []
# for i in range(1, q+1):
#     nome = input(f"digite o nome {i}")
#     fila.append(nome)
# print(f"{fila}")
# for i in range(q):
#     atendido = fila.pop(0)
#     print(f"atendido {atendido}, fila atual {fila}")

# q = int(input("digite  o tamanho "))
# lista = []
# for i in range(1, q+1):
#     num = float(input("digite um número "))
#     lista.append(num)
# print(f"{lista}")
# for i in range(q):
#     num = lista.pop()
#     print(f"{num} , {lista} ")

# q = int(input("quantidade "))
# fila = []
# for i in range(1, q+1):
#     nome = input(f"digite o nome {i}")
#     fila.append(nome)
# print(f"fila: {fila}")
# up = [nome.upper() for nome in fila]
# print(f"fila: {up}")
# for i in range(q):
#     atendido = fila.pop(0)
#     print(f"atendido {atendido} , fila atual {fila}")


# q = int(input("quantidade "))
# fila = []
# for i in range(1, q+1):
#     nome = input(f"digite o nome {i}")
#     fila.append(nome)
# print(f"fila: {fila}")
# for i in range(q):
#     atendido = fila.pop()
#     print(f"atendido {atendido} , fila atual {fila}")

# q = int(input("quantidade "))
# pilha = []
# for i in range(1, q+1):
#     nomel = input("digite o nome do livro ")
#     pilha.append(nomel)
# print(f"pilha: {pilha}")
# m = [nomel for nomel in pilha if len(nomel) > 5]
# for i in range(q):
#     livro = pilha.pop()
#     print(f"livro {livro} pilha atual {pilha}")
# print(f"{m}")

# corredores = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda"]
# historico = corredores.copy()
# for i, corredor in enumerate(corredores):
#     print(f"{i+1}, {corredor}")
# del corredores[2]
# print(f"{historico}, {corredores}")

# q = int(input("quantidade "))
# b = float(input("contar "))
# p = float(input("primeira aparição "))
# lista = []
# for i in range(1, q+1):
#     num = float(input("digite um número "))
#     lista.append(num)
# i = lista.count(b)
# s = lista.index(p)
# copia = lista.copy()
# copia.sort(reverse=True)
# print(f"o:{lista}, q a: {i}, p a:{s}, a c: {copia}")

# q = int(input("quantidade "))
# s1 = int(input("começo "))
# s2 = int(input("fim "))
# lista = []
# for i in range(1, q+1):
#     num = float(input("numero "))
#     lista.append(num)
# subv = lista[s1:s2+1]
# subv = subv[::-1]
# del lista[-2:]
# print(f"{lista}, {subv}")

# q = int(input("digite a quantidade de numeros "))
# a = int(input("digite ate onde quer ver "))

# lista = []
# for i in range(q):
#     num = float(input(f"número {i}"))
#     lista.append(num)
# pn = lista[:a]
# ln = lista[1:-1]
# print(f"{lista}, {pn}, {ln}")

# q = int(input("quantidade "))
# lista = []
# for i in range(q):
#     num = float(input(f"{i}: "))
#     lista.append(num)
# print(f"{lista[::2]}, {lista[::-1]}")


# q = int(input("quantidade "))
# b = float(input("busca "))
# lista = []
# for i in range(1, q+1):
#     num = float(input(f" {i}: "))
#     lista.append(num)
# if b in lista:
#     c = lista.count(b)
#     d = lista.index(b)
#     print(f"{b} esta na lista e aparece {c} vezes, primeira {d+1}")
# else:
#     print(f"{b} não aparece ")

# q = int(input("quantidade "))
# lista = []
# for i in range(1, q+1):
#     num = float(input(f"{i}: "))
#     lista.append(num)
# media = sum(lista) / q
# m = max(lista)
# mi = min(lista)
# i1 = lista.index(m)
# i2 = lista.index(mi)
# print(f"{lista}, {sum(lista)}, {media}, {m}, {mi}, {i1+1}, {i2+1}")

# q = int(input("quantidade "))
# lista = []
# for i in range(1, q+1):
#     num = float(input(f"{i} "))
#     lista.append(num)

# crescente = sorted(lista)
# lista.sort(reverse=True)
# print(f"{lista}, {crescente}")

# q = int(input("quantidade "))
# lista = []
# for i in range(1, q+1):
#     num = float(input(f"{i}: "))
#     lista.append(num)
# nl = [0 if num < 0 else num for num in lista]
# print(f"{lista}, {nl}")

# q = int(input("quantidade de frutas "))
# B = input("busca ")
# lista = []
# for i in range(1, q+1):
#     fruta = input(f"{i} ")
#     lista.append(fruta)
# nl = [fruta.lower() for fruta in lista]
# if B.lower() in nl:
#     print(f"{B} esta na lista")
# print(f"{lista}, {nl}")

# produto = {
#     "nome": input("digite um nome "),
#     "preço": float(input("digite um preço ")),
#     "quantidade": int(input("digite a quantidade "))
# }
# produto["preço"] = produto["preço"] * 0.9
# if produto["quantidade"] > 0:
#     produto["status"] = "em estoque"
# else:
#     produto["status"] = "esgotado"
# pe = produto["preço"] * produto["quantidade"]
# print(f"{produto}, {pe}")
# consulta = input("deseja consultar qual chave ")
# resultado = produto.get(consulta, "não encontramos")
# print(f"{resultado}")

# q = int(input("digite quantos produtos tem no estoque"))
# estoque = []
# for i in range(1, q+1):
#     nome = input(f"nome do produto {i} ")
#     preço = float(input("preço "))
#     quantidade = int(input("quantidade "))
#     estoque.append({"nome": nome, "preço": preço, "quantidade": quantidade})
# for produto in estoque:
#     print(f"{produto['nome']}, {produto['preço']}, {produto['quantidade']}")


# q = int(input("digite quantos produtos tem no estoque "))
# estoque = []
# for i in range(1, q+1):
#     nome = input("nome do produto ")
#     quantidade = int(input("quantidade "))
#     estoque.append({"nome": nome, "quantidade": quantidade})
# be = [nome for nome in estoque if nome["quantidade"] < 5]
# print(f"{be}")

# q = int(input("quantidade de produtos "))
# estoque = []
# pg = 0
# for i in range(1, q+1):
#     nome = input("nome do produto ")
#     preço = float(input("preço "))
#     quantidade = int(input("digite a quantidade "))
#     estoque.append({"nome": nome, "preço": preço, "quantidade": quantidade})
#     pg += preço * quantidade
# for prod in estoque:
#     print(f"{prod['nome']}, {prod['preço']}, {prod['quantidade']}")
# print(f"total {pg}")

# q = int(input("quantidade de produtos "))
# produtos = {}
# for i in range(1, q+1):
#     nome = input("nome ")
#     preço = float(input("preço "))
#     quantidade = int(input("quantidade "))
#     produtos[nome] = {"preço": preço, "quantidade": quantidade}
# for nome in produtos:
#     p = produtos[nome]["preço"]
#     qe = produtos[nome]["quantidade"]
#     print(f"{nome}, {p:.2f}, {qe}")
#     total = produtos[nome]["preço"] * produtos[nome]["quantidade"]
#     print(f"total {total}")

# q = int(input("quantidade de alunos "))
# n = int(input("quantidade de notas "))
# o = 0
# nomes = {}
# for i in range(1, q+1):
#     nome = input("nome ")
#     notas = []
#     for j in range(1, n+1):
#         nota = float(input("nota "))
#         notas.append(nota)

#     nomes[nome] = notas
# for nome in nomes:
#     listan = nomes[nome]
#     media = sum(listan) / len(listan)
#     print(f"aluno: {nome}, notas: {listan}, media: {media:.2f}")

# q = int(input("quantidade de atletas "))
# v = int(input("quantidade de velocidades registradas por atleta "))
# atletas = {}
# for i in range(1, q+1):
#     nome = input(f"nome do atleta {i}")
#     idade = int(input("idade "))
#     altura = float(input("altura "))
#     velocidades = []
#     for j in range(1, v+1):
#         velocidade = float(input(f"velocidade {j}"))
#         velocidades.append(velocidade)
#     atletas[nome] = {"idade": idade,
#                      "altura": altura,
#                      "velocidades": velocidades}
# for nome in atletas:
#     listav = atletas[nome]["velocidades"]
#     media = sum(listav) / len(listav)
#     print(f"atleta: {nome}, idade:{atletas[nome]['idade']}")
#     print(f"altura: {atletas[nome]['altura']}, velocidades: {listav}")
#     print(f"media: {media:.2f}")

# q = int(input("quantidade de turmas "))
# turmas = {}
# for i in range(q):
#     modalide = input("digite a modalidade ")
#     instrutor = input("digite o nome do instrutor ")
#     d = int(input("quantidade de dias de treino "))

#     diast = []
#     for j in range(d):
#         dia = input("dia da semana ")
#         diast.append(dia)
#     turmas[modalide] = {"instrutor": instrutor, "dias": d,
#     "dias de treino": diast}

# for modalide in turmas:
#     print(f"modalidade: {modalide}, "
#           f"instrutor: {turmas[modalide]['instrutor']}, "
#           f"dias de treino: {turmas[modalide]['dias de treino']}, "
#           f"dias:{(turmas[modalide]['dias'])}"
#         )

# q = int(input("quantidade de filmes "))
# cat = {}
# for i in range(q):
#     tit = input("nome do filme ")
#     lan = int(input("data de lançamento "))
#     qa = int(input("quantidade de atores principais no elenco "))
#     elen = []
#     for j in range(qa):
#         at = input("nome do ator ")
#         elen.append(at)
#     cat[tit] = {"titulo": tit, "lançamento": lan,
#                 "quantidade de atores": qa,  "atores": elen}
# for tit in cat:
#     print(f"titulo: {tit}, lançamento: {cat[tit]['lançamento']}, "
#           f"quantidade de atores: {cat[tit]['quantidade de atores']}, "
#           f"atores: {cat[tit]['atores']}")

# q = int(input("digite quantos jogos "))
# bibli = {}
# for i in range(q):
#     ng = input("nome do jogo ")
#     p = input("plataforma ")
#     c = int(input("quantidade de conquistas "))
#     con = []
#     for j in range(c):
#         n = input("nome da conquista ")
#         con.append(n)
#     bibli[ng] = {"nome": ng, "plataforma": p, "conquistas": c, "show": con}
# for ng in bibli:
#     print(f"nome: {ng}, plataforma: {bibli[ng]['plataforma']}, "
#           f"conquistas: {bibli[ng]['conquistas']}, "
#           f"são elas: {bibli[ng]['show']}")

# q = int(input("quantos pratos "))
# card = {}
# for i in range(q):
#     nome = input("nome do prato ")
#     preço = float(input("preço do prato "))
#     quantidade = int(input("quantidade de ingredientes "))
#     ingrediente = []
#     for j in range(quantidade):
#         ing = input("ingrediente ")
#         ingrediente.append(ing)
#     card[nome] = {"preço": preço, "quantidade": quantidade, "ingredientes": ingrediente}
# for nome in card:
#     print(f"nome: {nome}, preço: {card[nome]['preço']}, quantidade: {card[nome]['quantidade']}, ingredientes: {card[nome]['ingredientes']}")

# q = int(input("quantidade de frutas "))
# frutas = []
# for i in range(q):
#     nome = input("nome ")
#     frutas.append(nome)
# cont = {}
# for fruta in frutas:
#     cont[fruta] = cont.get(fruta, 0) + 1
# print(f"{fruta} tem {cont[fruta]} frutas")

# q = int(input("quantidade de projetos "))
# proj = {}
# for i in range(q):
#     nome = input("nome ")
#     gerente = input("gerente ")
#     tc = int(input("quantidade de tarefas concluidas "))
#     tarefas = []
#     for j in range(tc):
#         tarefa = input("tarefa ")
#         tarefas.append(tarefa)
#     proj[nome] = {"gerente": gerente, "tarefas": tc, "tarefas concluidas": tarefas}
# for nome in proj:
#     print(f"nome: {nome}, gerente: {proj[nome]['gerente']}, tarefas: {proj[nome]['tarefas']}, tarefas concluidas: {proj[nome]['tarefas concluidas']}")

# q = int(input("tamanho da lista com nomes repetidos "))
# lista = []
# for i in range(q):
#     nome = input("nome ")
#     lista.append(nome)
# unica = list(set(lista))
# print(f"{lista}, {unica}, {len(unica)}")

# q = int(input("quantidade de cadastros"))
# cadastros = []
# for i in range(q):
#     c = int(input("digite o cadastro"))
#     cadastros.append(c)
# unicos = list(set(cadastros))
# print(f"{cadastros}, {unicos}, {len(unicos)}, {len(cadastros) - len(unicos)}")

# q = int(input("tamanho da lista de núemros repetidos"))
# rep = []
# for i in range(q):
#     num = float(input("digite um numero "))
#     rep.append(num)
# unicos = list(set(rep))
# print(f"{rep}, {unicos}")
# coordenadas = (-100, 100)
# print(f"{coordenadas}")

# u = int(input("quantidade de usuarios "))
# usuario = {}
# for i in range(u):
#     nome = input("nome ")
#     idade = int(input("digite sua idade "))
#     usuario[nome] = idade
# for nome in usuario:
#     print(f"{nome} tem {usuario[nome]} anos")

# q = int(input("tamanho lista "))
# lista = []
# for i in range(q):
#     fruta = input("nome fruta ")
#     lista.append(fruta)
# i = int(input("indice"))
# d = input("digite a fruta pra inserir no indice ")

# lista.insert(i, d)
# r = input("digite a fruta que quer remover da lista ")
# lista.remove(r)
# print(f"{lista}")

# p = int(input("tamanho do dicionario "))
# pro = {}
# for i in range(p):
#     nome = input("nome do produto ")
#     preço = float(input("preço "))
#     quantidade = int(input("quantidade "))
#     pro[nome] = {"preço": preço, "quantidade": quantidade}
# for nome in pro:
#     print(f"{nome}, {pro[nome]['preço']}, {pro[nome]['quantidade']}")

# f1 = input("digite uma frase ")
# f2 = input("digite outra frase ")
# f1 = set(f1)
# f2 = set(f2)
# uni = f1 | f2
# inter = f1 & f2
# dif = f1 - f2
# print(f"{uni} {inter} {dif}")

# i = int(input("dfigite um inteiro "))
# d = float(input("digite um decimal "))
# i = str(i)
# d = str(d)
# conc = "-".join([i, d])
# res = f"""concatenação {conc}
#         {len(conc)}"""
# print(F"{res}")

# p = input("digite uma frase ")
# a = int(input("digite qual letra quer ver "))
# c = int(input("começo "))
# f = int(input("fim "))
# print(f"{p[a-1]} {p[c-1:f]} {p[::-1]}")

# f = input("digite uma frase ")
# f = f.strip()
# print(f"{f.upper()} {f.title()} {f}")
# s = input("digite a palavra que quer trocar ")
# t = input("por qual ")
# f = f.replace(s, t)
# print(f"{f}")

# f = input("digite uma frase ")
# f = f.split()
# f = "*".join(f)
# print(f"{f}")
# c = """ los angeles
# nova york 
# tokio"""
# c = c.splitlines()
# print(f"{c}")

# f = input("digite uma frase ")
# b = input("digite a busca ")
# if b in f:
#     print(f"{b} encontrado na posição {f.find(b)}, apareceu {f.count(b)} vezes")
# h = input("digite uma entrada ")
# if h.isdigit():
#     print(f"{h} é um número")

# l = float(input("digite a largura "))
# c = float(input("digite o comprimento "))
# a = l * c
# print(f"{a:.2f}")
# print(f"{a:>10.2f}")


f1 = input("frase ")
f2 = input("outra ")
f3 = f1 + f2
print(f"{f3} {len(f3)} {min(f1, f2)} {max(f1, f2)}, {f1 * 3}")