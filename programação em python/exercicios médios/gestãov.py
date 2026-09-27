def tt(texto):
    texto = texto.strip().title()
    return texto


def tv(vs):
    try:
        v = vs.strip()
        v = v.replace("R$", "")
        v = v.replace(",", ".")
        v = float(v)
        return v
    except:
        return 0.0


def desc(valor, desconto):
    t = valor * (1 - (desconto / 100))
    return t


q = int(input("digite quantas categorias tem a loja: "))
cat = {}
for i in range(q):
    print(f"===== CATEGORIA {i+1} =====")
    catn = input("digite o nome da categoria: ")
    catn = tt(catn)
    d = float(input("qual o desconto para a essa categoria? "))
    cat[catn] = d
    print(f"===== CATEGORIA {i+1} SALVA =====\n")


qp = int(input("digite a quantidade de produtos para cadastro:\n "))
vendas = []
for i in range(qp):
    print(f"===== PRODUTO {i+1} =====")
    n = input("digite o nome do produto:\n ")
    n = tt(n)
    p = input("digite o preço do produto:\n ")
    p = tv(p)
    c = input("digite a categoria do produto:\n ")
    c = tt(c)
    desconto = cat.get(c, 0.0)
    vp = desc(p, desconto)
    vendas.append({"nome": n, "preço": p, "categoria": c, "valor": vp})
    print(F"===== PRODUTO {i+1} CADASTRADO =====\n")
print("=====  RESULTADO GERAL =====\n")
for item in vendas:
    print(f"""
    | nome do produto: {item['nome']} |,
    | preço do produto: {item['preço']:.2f} |,
    | categoria do produto: {item['categoria']} |,
    | preço com desconto: {item['valor']:.2f}|\n""")
st = sum([item['valor'] for item in vendas])
print(f"valor total das compras: {st:.2f}")

try:
    with open("relatório.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("===== RELATÓRIO DE VENDAS =====\n")
        for item in vendas:
            arquivo.write(f"""
produto: {item['nome']}
preço do produto: {item['preço']:.2f}
categoria do prdouto: {item['categoria']}
preço com desconto: {item['valor']:.2f}       \n""")
        arquivo.write(f"\n| valor total: {st:.2f} |")
        print("arquivo salvo com sucesso!")
except Exception as e:
    print(f"erro: {e}")