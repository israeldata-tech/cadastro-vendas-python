# n = int(input("digite um número "))
# s = str(n)
# co = f"""  festa
#         {n} {s}"""
# print(f"{co}")

# q = (input("digite um texto "))
# co = int(input("digite o começo "))
# fi = int(input("digite o fim"))
# print(f"""{q[0]}
#         {q[-1]}
#         {q[:3]} {q[2:]}
#         {q[::-1]}
#         {q[co - 1:fi]}""")

# s = input("digite uma frase com espaços nas extremidades ")
# t = input("digite uma palavra que quer trocar ")
# b = input("digite a palavra que vai substituir ")
# ns = s.strip()
# print(f"{s} {ns} {ns.upper()} {ns.lower()} {ns.capitalize()} {ns.title()} {ns.replace(t,b)}")

# s = input("palavras divididas por virgula ")
# lista = s.split(",")
# fj = (" - ").join(lista)

# o = """ f1 = input("digite uma frase)
#     f2 = input("outra) """
# linhas = o.splitlines()

# print(f"{fj} {linhas}")


# f = input("digite uma frase ")
# b = input("digite uma pra buscar ")
# c = input("uma letra pra contar ")
# s = input("uma letra pra ver se inicia a frase ")
# n = input("letra pra ver se termina a frase")

# if b in f:
#     print(f"encontrei {b} na posição {f.find(b)}")
# if c in f:
#     print(f"{c} aparece {f.count(c)} vezes")
# if f.startswith(s):
#     print(f"a frase começa com {s}")
# if f.endswith(n):
#     print(f"a frase termina com {n}")

# p = input("nome do produto ")
# f = float(input("preço"))
# print(f"{f:.2f}")
# p2 = input("digite outro produto ")
# print(f"{p + p2}, {len(p)}, {p * 3}")


# em = input("digite seu email ")
# em = em.strip()
# em = em.lower()
# if "@" in em and em.endswith(".com"):
#     print("email valido ")
#     ne = em.split("@")
#     print(f"{ne[0]} {ne[1]} {len(em)}")
# else:
#     print("email invalido ")


# c = input("digite um codigo")
# c = c.strip()
# c = c.upper()
# if c.endswith(".TXT"):
#     c = c.replace(".TXT", "")
#     c = c.split("-")
#     print(f"{c[0]}  [{c[2]}]")
#     if c[1].isdigit():
#         print(f"{c[1]} ")
#     else:
#         print("codigo não possui apenas numeros ")
# else:
#     print("codigo invalido")

# p = input("digite uma frase ")
# b = input("digite a busca ")
# if b in p:
#     print(f"encontrei {b} em {p} na posição {p.find(b)}")

# p = input("digite uma frase ")
# b = input("outra ")
# co = set(p)
# cu = set(b)
# b = co | cu
# pu = "".join(b)
# print(f"{pu}")

# p = input("digire uma frase ")
# b = set(p)
# for carac in b:
#     qtd = p.count(carac)
#     print(f"{carac} aparece {qtd} vezes")

# p = input("frase um")
# b = input("outra ")
# p = set(p)
# b = set(b)
# dif = p - b
# print(f"{dif}")