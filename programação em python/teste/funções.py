
# def media(q, soma):
#     m = soma / q
#     return m


# q = int(input("quantidade de notas "))
# soma = 0
# for i in range(q):
#     nota = float(input("digite a nota "))
#     soma += nota
# med = media(q, soma)
# print(f"a média é {med}")

# def tipo(n):
#     if n % 2 == 0:
#         p = "par"
#     else:
#         p = "impar"
#     if n > 0:
#         num = "positivo"
#     elif n < 0:
#         num = "negativo"
#     else:
#         num = "zero"
#     return f"{p} {num}"


# n = float(input("digite um número "))
# print(f"{tipo(n)}")

# def calc(p, i=0, d=0):
#     p = p * (1 + i / 100)
#     p = p * (1 - d / 100)
#     return p


# p = float(input("digite o preço "))
# i = float(input("imposto "))
# d = float(input("desconto "))
# p = calc(p, i, d)
# print(f"{p:.2f}")

# def ficha(nome, **kwargs):
#     print(f"{nome}")
#     for k, v in kwargs.items():
#         print(f"{k.title()}:{v}")


# nome = input("nome ")
# idade = int(input("idade "))
# ficha(nome, idade=idade)

# def soma(lista):
#     soma = 0
#     for num in lista:
#         soma += num
#     return soma


# q = int(input("quantidade de valores "))
# lista = []
# for i in range(q):
#     num = float(input("digite o numero "))
#     lista.append(num)
# soma = soma(lista)
# print(f"a soma da lista é {soma}")

# def dados(nome, idade, cidade):
#     print(f"{nome}, {idade}, {cidade}")


# q = int(input("quantidade de cadastros"))
# cadastro = {}
# for i in range(q):
#     dadospessoa = {
#         "nome": input("nome"),
#         "idade": int(input("idade")),
#         "cidade": input("cidade")
#     }

#     dados(**dadospessoa)

# def media(*notas):
#     return sum(notas) / len(notas)


# q = int(input("quantidade de notas "))
# mn = []
# for i in range(q):
#     nota = float(input("digite a nota "))
#     mn.append(nota)
# mf = media(*mn)
# print(f"a media é {mf:.2f}")

# def analise(*notas):
#     return sum(notas) / len(notas), max(notas), min(notas)


# q = int(input("quantidade de notas "))
# mn = []
# for i in range(q):
#     nota = float(input("nota "))
#     mn.append(nota)
# media, maior, menor = analise(*mn)
# print(f"media {media:.2f} maior {maior:.2f} menor {menor:.2f}")

# def cadastroprod(nome, preço, **detalhes):
#     print(f"{nome}, {preço}")
#     for chave, valor in detalhes.items():
#         print(f"{chave}: {valor}")


# nome = input("nome do produto ")
# preço = float(input("preço "))
# q = int(input("quantos detalhes extras quer adicionar?"))
# detalhes = {}
# for i in range(q):
#     detalhe = input("digire o detalhe ")
#     tipo = input("digite o tipo")
#     detalhes[detalhe] = tipo
# cadastroprod(nome, preço, **detalhes)

# def limparl(linha_texto, cabecalho):
#     frase = linha_texto.strip()
#     frasel = frase.split(",")
#     frasef = []
#     for i in range(len(frasel)):
#         frasef.append(frasel[i].strip())
#     pessoa = {}
#     for chave, valor in zip(cabecalho, frasef):
#         pessoa[chave] = valor
#     return pessoa


# linha_texto = "   JOAO SILVA , 28 , Juazeiro do Norte \n"
# cabecalho = ['nome', 'idade', 'cidade']
# res = limparl(linha_texto, cabecalho)
# print(f"{res}")

# def limparn(linha):
#     nome = linha.strip().title()
#     return nome

# nome = input("nome ")
# nome = limparn(nome)
# print(f"nome {nome}")


# def limparp(p):
#     p = (p.strip())
#     p = (p.replace(",", "."))
#     p = (p.replace("R$", ""))
#     return float(p)


# preço = (input("preço "))
# print(f"preço {limparp(preço)}")

def adesconto(preço, tdesconto):
    return preço * (1 - tdesconto / 100)


q = int(input("digite quantos produtos quer aplicar desconto: "))
c = int(input("digite quantas categorias vai ter: "))
cat = {}
prod = []
for i in range(c):
    nome = input("digite o nome da categoria ")
    desconto = float(input("digite o desconto para essa categoria: "))
    cat[nome] = desconto
for i in range(q):
    nome = input("digite o nome do produto: ")
    p = float(input("preço do produto: "))
    ca = input("digite a categoria do produto ")
    dc = cat.get(ca, 0)
    pf = adesconto(p, dc)
    prod.append({
        "nome": nome,
        "preço original": p,
        "categoria": ca
        "desconto": dc,
        "preço final": pf
    })

for item in cat:
    print(f"{item} {cat[item]}")
