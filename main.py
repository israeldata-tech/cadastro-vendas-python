cabecalho = ["id", "produto", "valor", "status", ]
vendas = []
q = int(input("quantidade de produtos "))
for i in range(q):
    print(f"produto {i+1}:")
    try:
        idc = int(input("id do produto: "))
        nome = input("nome do produto: ").strip().title()
        valor = float(input("valor do produto: "))
        status = input("status (pago/cancelado): ").strip().lower()
        if status == "pago":
            vl = [idc, nome, valor, status]
            dc = dict(zip(cabecalho, vl))
            vendas.append(dc)
    except Exception as e:
        print(f"erro: {e}")

print("=========== PRODUTOS CADASTRADOS ============")
for item in vendas:
    print(f"id: {item['id']} - nome: {item['produto']} - valor: {item['valor']} - status: {item['status']}")
valores = [c["valor"] for c in vendas]
if valores:
    print(f"valor total = {sum(valores):.2f}")
    print(f"média de vendas: {sum(valores)/len(valores):.2f}")
    print(f"maior: {max(valores)}")
    print(f"menor: {min(valores)}")
