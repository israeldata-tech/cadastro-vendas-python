cabecalho = ["id", "produto", "quantidade", "preço_unitario", "status_reposicao", "status_troca", "v/d", "arrecadação"]

estoque = []

q = int(input("digite a quantidade de produtos para cadastro: "))

for i in range(q):
    print(f"========== PRODUTO {i+1} ==========")
    try:

        idc = int(input("digite o id do produto: "))
        nome = input("digite o nome do produto: ").strip().title()
        qtd = int(input("digite a quantidade em estoque: "))
        if qtd < 5:
            status = "precisa de reposição"
        else:
            status = "não precisa de reposição"
        p = float(input("digite o preço por unidade: "))
        v = int(input("digite a quantidade que foi vendido/devolvido: "))
        stat = input("digite o status do produto (vendido/devolvido): ").strip().lower()
        soma = 0
        if stat == "vendido":
            soma = v * p

        elif stat == "devolvido":
            soma = -(v * p)
        vl = [idc, nome, qtd, p, status, stat, v, soma]
        dc = dict(zip(cabecalho, vl))
        estoque.append(dc)
        print("========== PRODUTO CADASTRADO COM SUCESSO ==========")

    except Exception as e:
        print(f"erro: {e}")
        print("========== FALHA NO CADASTRO DO PRODUTO ==========")
print("========== RESUMO INDIVIDUAL DE ESTOQUE ==========")
for item in estoque:
    print(f"""
    |id: {item['id']}|
    |nome: {item['produto']}|
    |quantidade em estoque: {item['quantidade']}|
    |preço por unidade: {item['preço_unitario']}|
    |status de reposição: {item['status_reposicao']}|
    |status de troca: {item['status_troca']}|
    |quantidade vendida/devolvida: {item['v/d']}
    |valor arrecadado: {item['arrecadação']:.2f}|""")
if estoque:
    arrecadacoes = [item['arrecadação'] for item in estoque]
    vendidos = [item['v/d'] for item in estoque if item['status_troca'] == "vendido"]
    devolvidos = [item['v/d'] for item in estoque if item['status_troca'] == "devolvido"]
    mais_mov = estoque[0]
    menos_mov = estoque[0]
    for item in estoque:
        if item['v/d'] > mais_mov['v/d']:
            mais_mov = item
        if item["v/d"] < menos_mov['v/d']:
            menos_mov = item
    print("========== RESUMO GERAL ==========")
    print(f"lucro geral(líquido): {sum(arrecadacoes):.2f}")
    print(f"média arrecadada por produto: {sum(arrecadacoes)/len(arrecadacoes):.2f}")
    print(f"total de unidades vendidas: {sum(vendidos)}")
    print(f"total de unidades devolvidas: {sum(devolvidos)}")
    print(f"produto mais comprado: {mais_mov['produto']} - {mais_mov['v/d']} - {mais_mov['status_troca']}")
    print(f"produto menos comprado: {menos_mov['produto']} - {menos_mov['v/d']} - {menos_mov['status_troca']}")
else:
    print("nenhum produto foi cadastrado.")