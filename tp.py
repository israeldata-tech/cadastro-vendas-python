# texto = input("digite um texto")

# try:
#     with open("anot.txt", "a", encoding="utf-8") as arquivo:
#         arquivo.write(f"{texto}\n")
#         print("texto salvo ")
# except Exception as e:
#     print(f"não foi possivel salvar. motivo:{e}")

# try:
#     with open("anot.txt", "r", encoding="utf-8") as arquivo:
#         for linha in arquivo:
#             print(linha.strip())
# except Exception as e:
#     print(f"não foi possivel ler, motivo: {e}")

# import json
# from pathlib import Path

# pasta = Path("dados")
# caminho = pasta / "perfil.json"

# pasta.mkdir(parents=True, exist_ok=True)

# nome = input("nome: ")
# idade = int(input("idade: "))
# cidade = input("cidade")

# dic = {
#     "nome": nome,
#     "idade": idade,
#     "cidade": cidade
# }
# try:

#     with open(caminho, "w", encoding="utf-8") as f:
#         json.dump(dic, f, indent=4)
#         print("perfil salvo")
# except Exception as e:
#     print(f"erro: {e}")

# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         dados = json.load(f)
#         print(dados)
# except Exception as e:
#     print(f"erro: {e}")


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import json
from pathlib import Path

# q = int(input("quantidade de produtos: "))
# produtos = []
# preço = []
# for i in range(q):
#     nome = input("nome do produto ")
#     p = float(input("preço do produto "))
#     produtos.append(nome)
#     preço.append(p)

# pasta = Path("relatorio")
# caminho = pasta / "relatorio.json"
# Path("relatorio").mkdir(parents=True, exist_ok=True)

# lista = []
# for prod, val in zip(produtos, preço):
#     lista.append({"produto": prod, "valor": val})
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         json.dump(lista, f, indent=4)
# except Exception as e:
#     print(f"erro: {e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         dados = json.load(f)
#         for item in dados:
#             print(f"produto:{item['produto']} valor:{item['valor']:.2f}")
# except Exception as e:
#     print(f"erro: {e}")

# q = int(input("digite quantas tarefas quer cadastrar: "))
# tarefa = []
# prioridade = []
# for i in range(q):
#     taf = input("digite a tarefa ")
#     pri = input("digite a prioridade (baixa, média, alta): ")
#     tarefa.append(taf)
#     prioridade.append(pri)
# sistema = Path("sistema")
# caminho = sistema / "sistema.json"
# Path("sistema").mkdir(parents=True, exist_ok=True)
# sist = []
# for taf, pri in zip(tarefa, prioridade):
#     sist.append({"tarefa": taf, "prioridade": pri})
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         json.dump(sist, f, indent=4)
# except Exception as e:
#     print(f"erro: {e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         dados = json.load(f)
#         for item in dados:
#             print(f"tarefa: {item['tarefa']} | prioridade:{item['prioridade']}")
# except Exception as e:
#     print(f"erro:{e}")

# q = int(input("quantidade de alunos pra cadastrar notas "))
# alunos = []
# n1 = []
# n2 = []
# for i in range(q):
#     nome = input("nome do aluno ")
#     no1 = float(input("digite a primeira nota desse aluno "))
#     no2 = float(input("digite a segunda nota desse aluno "))
#     alunos.append(nome)
#     n1.append(no1)
#     n2.append(no2)
# escola = Path("escola")
# caminho = escola / "escola.json"
# Path("escola").mkdir(parents=True, exist_ok=True)
# sist = []
# for alu, t, r in zip(alunos, n1, n2):
#     sist.append({"nome": alu, "media": (t + r) / 2})
# try:
#     with open(caminho, "w", encoding="utf-8") as n:
#         json.dump(sist, n, indent=4)
# except Exception as e:
#     print(f"erro: {e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as n:
#         dados = json.load(n)
#         for item in dados:
#             print(f"nome: {item['nome']} | média: {item['media']:.2f}")
# except Exception as e:
#     print(f"erro:{e}")

# dados_sujos = [
#     "  MARCOS SILVA , 28 ,  são paulo  \n",
#     "lucas mendes, 35, RIO DE JANEIRO\n",
#     "  ana PAULA ,22,  curitiba  \n"
# ]
# dadosl = Path("dados")
# Path("dados").mkdir(parents=True, exist_ok=True)
# try:
#     with open(dadosl / "dados.txt", "w", encoding="utf-8") as f:
#         for item in dados_sujos:
#             linhal = item.strip()
#             partes = linhal.split(",")
#             nome = partes[0].strip().title()
#             idade = partes[1].strip()
#             cidade = partes[2].strip().title()
#             lp = f"{nome}, {idade}, {cidade}"
#             f.write(f"{lp}\n")
# except Exception as e:
#     print(f"erro: {e}")
# try:
#     with open(dadosl / "dados.txt", "r", encoding="utf-8") as f:
#         for linha in f:
#             print(linha.strip())
# except Exception as e:
#     print(f"erro: {e}")

# dados_brutos = [
#     "  CARLOS EDUARDO , 42 ,  belo horizonte  \n",
#     "linha_corrompida_sem_virgulas\n",
#     "  BEATRIZ SOUZA , 19 ,  porto alegre  \n"
# ]
# relatoriol = Path("relatorio")
# caminho = relatoriol / "relatorio.txt"
# Path("relatorio").mkdir(parents=True, exist_ok=True)

# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         for linha in dados_brutos:
#             linhal = linha.strip()
#             partes = linhal.split(",")
#             if len(partes) == 3:
#                 nome = partes[0].strip().title()
#                 idade = partes[1].strip()
#                 cidade = partes[2].strip().title()
#                 lp = f"{nome}, {idade}, {cidade}"
#                 f.write(f"{lp}\n")
#             else:
#                 print(f"erro: linha corrompida '{linhal}'")
# except Exception as e:
#     print(f"erro: {e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         for linha in f:
#             print(linha.strip())
# except Exception as e:
#     print(f"erro:{e}")

# dados_brutos = [
#     " MARCOS SILVA , 28 , são paulo \n",
#     " ANA PAULA , 15 , curitiba \n",
#     " LUCAS MENDES , 35 , rio de janeiro \n"
# ]
# idadesv = []
# anal = Path("anal")
# caminho = anal / "anal.json"
# Path("anal").mkdir(parents=True, exist_ok=True)
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         for linha in dados_brutos:
#             linhal = linha.strip()
#             partes = linhal.split(",")
#             if len(partes) == 3:
#                 nome = partes[0].strip().title()
#                 idade = int(partes[1].strip())
#                 cidade = partes[2].strip().title()
#                 if idade >= 18:
#                     idadesv.append(idade)
#                     lp = f"{nome}, {idade}, {cidade}"
#                     f.write(f"{lp}\n")
#             else:
#                 print(f"erro: linha corrompida {linhal}")
    
# except Exception as e:
#     print(f"erro: {e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         for linha in f:
#             print(linha.strip())
#     if idadesv:
#         print(f"idade média: {sum(idadesv)/len(idadesv)}")
# except Exception as e:
#     print(f"erro: {e}")


# pedidos_brutos = [
#     " 101 , CARLOS EDUARDO , 150.50 , pago \n",
#     "linha_corrompida_sem_virgula\n",
#     " 102 , ANA PAULA , 80.00 , cancelado \n",
#     " 103 , LUCAS MENDES , 300.00 , PAGO \n"
# ]
# vp = []
# anal = Path("vendas")
# caminho = anal / "vendas.csv"
# Path("vendas").mkdir(parents=True, exist_ok=True)
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         for linha in pedidos_brutos:
#             linhal = linha.strip()
#             partes = linhal.split(",")
#             if len(partes) == 4:
#                 cliente = partes[0].strip()
#                 nome = partes[1].strip().title()
#                 valor = float(partes[2].strip())
#                 status = partes[3].strip().lower()
#                 if status == "pago":
#                     vp.append(valor)
#                     lp = f"{cliente} - {nome} - {valor:.2f} - {status}\n"
#                     f.write(f"{lp}")
#             else:
#                 print(f"linha ignorada: {linha}")
# except Exception as e:
#     print(f"erro:{e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         for linha in f:
#             print(linha.strip())

#         print(f"valor geral: {sum(vp):.2f}")
# except Exception as e:
#     print(f"erro:{e}")

# produtos_brutos = [
#     " P01 , teclado mecânico , 150.00 , 5 \n",
#     "linha_invalidap02\n",                        # Corrompida
#     " P02 , MOUSE OPTICO , 50.00 , 0 \n",          # Estoque 0 (deve ser ignorado)
#     " P03 , monitor 24pol , 850.00 , 12 \n"        # Válido
# ]
# totale = []
# estoque = Path("estoque")
# caminho = estoque / "estoque.csv"
# Path("estoque").mkdir(parents=True, exist_ok=True)
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         for linha in produtos_brutos:
#             linhal = linha.strip()
#             partes = linhal.split(",")
#             if len(partes) == 4:
#                 c = partes[0].strip()
#                 nome = partes[1].strip().title()
#                 valor = float(partes[2].strip())
#                 est = int(partes[3].strip())
#                 if est > 0:
#                     totale.append(valor * est)
#                     lp = f"{c} - {nome} - {valor:.2f} - {est}\n"
#                     f.write(f"{lp}")
#                 else:
#                     print(f"estoque 0 para {nome}")
# except Exception as e:
#     print(f"erro:{e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         for linha in f:
#             print(linha.strip())
#         print(f"total: {sum(totale):.2f}")
# except Exception as e:
#     print(f"erro:{e}")


# logs_brutos = [
#     " 2026-09-11 08:00 , CARLOS_DEV , 192.168.1.10 , SUCESSO \n",
#     "linha_de_log_corrompida_sem_formato\n",
#     " 2026-09-11 08:05 , ANA_ADMIN , 192.168.1.15 , FALHA \n",
#     " 2026-09-11 08:10 , LUCAS_USER , 192.168.1.20 , sucesso \n"
# ]
# dados = []
# anal = Path("logs")
# caminho = anal / "logs.csv"
# anal.mkdir(parents=True, exist_ok=True)
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         for linha in logs_brutos:
#             linhal = linha.strip()
#             partes = linhal.split(",")
#             if len(partes) == 4:
#                 dh = partes[0].strip()
#                 nome = partes[1].strip()
#                 ip = partes[2].strip()
#                 status = partes[3].strip().lower()
#                 if status == "sucesso":
#                     dados.append({"data": dh, "nome": nome, "ip": ip, "status": status})
#                     lp = f"{dh} - {nome} - {ip} - {status}\n"
#                     f.write(f"{lp}")
#             else:
#                 print(f"erro: linha corrompida {linhal}")
# except Exception as e:
#     print(f"erro: {e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         for linha in f:
#             print(linha.strip())
#         print(f"total: {len(dados)}")
# except Exception as e:
#     print(f"erro:{e}")

# base_crua = [
#     " 101 , CARLOS SILVA , 28 , são paulo , ativo \n",
#     "linha_corrompida_invalida\n",
#     " 102 , ANA PAULA , 17 , curitiba , inativo \n",
#     " 103 , LUCAS MENDES , 35 , RIO DE JANEIRO , ATIVO \n"
# ]
# dados = []
# anal = Path("anal")
# caminho = anal / "anal.csv"
# anal.mkdir(parents=True, exist_ok=True)
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         for linha in base_crua:
#             linhal = linha.strip()
#             partes = linhal.split(",")
#             if len(partes) == 5:
#                 ende = partes[0].strip()
#                 nome = partes[1].strip()
#                 idade = int(partes[2].strip())
#                 estado = partes[3].strip().title()
#                 status = partes[4].strip().lower()
#                 if status == "ativo":
#                     dados.append(idade)
#                     lp = f"{ende} - {nome} - {idade} -{estado} - {status}\n"
#                     f.write(f"{lp}")
#             else:
#                 print(f"erro: linha corrompida: {linhal}")
# except Exception as e:
#     print(f"erro: {e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         for linha in f:
#             print(linha.strip())
#     if dados:
#         print(f"média de idades: {sum(dados)/len(dados)}")
# except Exception as e:
#     print(f"erro: {e}")


# funcionarios_brutos = [
#     " F01 , MARCOS SILVA , 3500.00 , TI \n",
#     "linha_com_erro\n",
#     " F02 , ANA PAULA , 2100.00 , VENDAS \n",
#     " F03 , LUCAS MENDES , 5000.00 , ti \n"
# ]
# salarios = []
# empresa = Path("dados")
# caminho = empresa / "funcionarios.csv"
# empresa.mkdir(parents=True, exist_ok=True)
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         for linha in funcionarios_brutos:
#             linhal = linha.strip()
#             partes = linhal.split(",")
#             if len(partes) == 4:
#                 depar = partes[0].strip()
#                 nnome = partes[1].strip()
#                 sal = float(partes[2].strip())
#                 setor = partes[3].strip().lower()
#                 if setor == "ti":
#                     salarios.append(sal)
#                     lp = f"{depar} - {nnome} - {sal} - {setor}\n"
#                     f.write(f"{lp}")
#             else:
#                 print(f"erro: {linhal}")
# except Exception as e:
#     print(f"erro: {e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         for linha in f:
#             print(linha.strip())
#     if salarios:
#         print(f"média de salarios: {sum(salarios)/len(salarios)}")
# except Exception as e:
#     print(f"erro: {e}")


# gastos_brutos = [
#     " 2026-09-01 , Supermercado , 250.80 , Alimentacao \n",
#     "linha_invalida_sem_formato\n",
#     " 2026-09-02 , Aluguel , 1200.00 , Moradia \n",
#     " 2026-09-03 , Restaurante , 95.40 , ALIMENTACAO \n"
# ]
# al = []
# casa = Path("dados")
# caminho = casa / "gastos.csv"
# casa.mkdir(parents=True, exist_ok=True)
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         for linha in gastos_brutos:
#             linhal = linha.strip()
#             partes = linhal.split(",")
#             if len(partes) == 4:
#                 data = partes[0].strip()
#                 locc = partes[1].strip().title()
#                 val = float(partes[2].strip())
#                 tipo = partes[3].strip().lower()
#                 if tipo == "alimentacao":
#                     al.append(val)
#                     lp = f"{data} - {locc} - {val} - {tipo}\n"
#                     f.write(f"{lp}")
#             else:
#                 print(f"erro: {linhal}")
# except Exception as e:
#     print(f"erro: {e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         for linha in f:
#             print(linha.strip())
#     if al:
#         print(f"média de gastos com alimentação: {sum(al)/len(al)}")
# except Exception as e:
#     print(f"erro: {e}")


# vendas_brutas = [
#     " V101 , Notebook , 3500.00 , concluida \n",
#     "linha_corrompida\n",
#     " V102 , Mouse , 80.00 , concluida \n",
#     " V103 , Teclado , 200.00 , cancelada \n",
#     " V104 , Monitor , 1200.00 , CONCLUIDA \n"
# ]
# gastosc = []
# dados = Path("vendas")
# caminho = dados / "vendas.csv"
# dados.mkdir(parents=True, exist_ok=True)
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         for linha in vendas_brutas:
#             linhal = linha.strip()
#             partes = linhal.split(",")
#             if len(partes) == 4:
#                 cod = partes[0].strip()
#                 prod = partes[1].strip().title()
#                 val = float(partes[2].strip())
#                 status = partes[3].strip().lower()
#                 if status == "concluida":
#                     gastosc.append(val)
#                     lp = f"{cod} - {prod} - {val} - {status}\n"
#                     f.write(f"{lp}")
#             else:
#                 print(f"erro: {linhal}")
# except Exception as e:
#     print(f"erro: {e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         for linha in f:
#             print(linha.strip())
#     if gastosc:
#         print(f"""
# média de vendas: {sum(gastosc)/len(gastosc):.2f},
# total = {sum(gastosc)},
# maior = {max(gastosc)},
# menor = {min(gastosc)},
#               """)
# except Exception as e:
#     print(f"erro: {e}")


# folha_bruta = [
#     " 101 , MARCOS SILVA , 4500.00 , engenharia \n",
#     "linha_com_erro_de_dados\n",
#     " 102 , ANA PAULA , 1800.00 , estagio \n",      
#     " 103 , LUCAS MENDES , 8200.00 , ENGENHARIA \n",
#     " 104 , BEATRIZ LIMA , 3100.00 , engenharia \n"
# ]
# val = []
# neg = Path("tp")
# caminho = neg / "tp.csv"
# neg.mkdir(parents=True, exist_ok=True)
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         for linha in folha_bruta:
#             linhal = linha.strip()
#             partes = linhal.split(",")
#             if len(partes) == 4:
#                 senha = partes[0].strip()
#                 nome = partes[1].strip()
#                 qtd = float(partes[2].strip())
#                 setor = partes[3].strip().lower()
#                 if setor == "engenharia":
#                     val.append(qtd)
#                     lp = f"{senha} - {nome} - {qtd} - {setor}"
#                     f.write(f"{lp}\n")
#             else:
#                 print(f"erro: {linhal}")
# except Exception as e:
#     print(f"erro: {e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         for linha in f:
#             print(linha.strip())
#     if val:
#         print(f"""
# contagem de engenheiros: {len(val)},
# salario total = {sum(val)},
# média de salarios = {sum(val)/len(val):.2f},
# maior = {max(val)},
# menor = {min(val)}
#             """)
# except Exception as e:
#     print(f"erro: {e}")

# def ll(arq):
#     chaves = [c.strip() for c in arq[0].split(",")]
#     cl = []
#     for linha in arq[1:]:
#         linhal = linha.strip()
#         partes = linhal.split(",")
#         if len(partes) == len(chaves):
#             try:
#                 idc = int(partes[0].strip())
#                 nome = partes[1].strip().title()
#                 idade = int(partes[2].strip())
#                 gastos = float(partes[3].strip())
#                 val = [idc, nome, idade, gastos]
#                 dc = dict(zip(chaves, val))
#                 cl.append(dc)
#             except Exception as e:
#                 print(f"erro: {e}")
#         else:
#             print(f"erro: linha corrompida: {linhal}")
#     return cl


# def gr(clientes):
#     gastos = [c["gastos"] for c in clientes]
#     if gastos:
#         print(f"""
# total de clientes: {len(clientes)},
# total de gastos: {sum(gastos)},
# média de gastos: {sum(gastos)/len(gastos):.2f},
# maior:{max(gastos)},
# menor:{min(gastos)}

#         """)
#     else:
#         print("erro: sem clientes")


# conteudo_bruto = """id,nome,idade,gastos
# 1,  MARCOS SILVA  ,28, 1500.50
# 2,linha_corrompida_invalida
# 3,  ANA PAULA  ,texto_invalido, 800.00
# 4,  LUCAS MENDES  ,35, 3200.00"""

# pasta = Path("dados")
# caminho = pasta / "dados.txt"
# pasta.mkdir(parents=True, exist_ok=True)

# with open(caminho, "w", encoding="utf-8") as f:
#     f.write(conteudo_bruto)
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         linhas = f.readlines()
#     cv = ll(linhas)
#     gr(cv)
# except Exception as e:
#     print(f"erro: {e}")





# cabecalho = ["id", "nome", "salario"]
# dados1 = [101, "Carlos Silva", 3500.0]
# dados2 = [102, "Ana Paula", 4200.0]
# cat = []

# re1 = dict(zip(cabecalho, dados1))
# re2 = dict(zip(cabecalho, dados2))
# cat.append(re1)
# cat.append(re2)
# print(f"{cat}")

#/////////////////////////////////////// fase 1 //////////////////////////////////////////////////////////////////////////////////////
# def ll(linhas):
#     cabecalho = linhas[0].strip().split(",")
#     dados = linhas[1:]
#     cat = []
#     for linha in dados:
#         linha = linha.strip()
#         partes = linha.split(",")
#         try:
#             idc = int(partes[0].strip())
#             nome = partes[1].strip().title()
#             valor = float(partes[2].strip())
#             status = partes[3].strip().lower()
#             if status == "pago":
#                 vl = [idc, nome, valor, status]
#                 dc = dict(zip(cabecalho, vl))
#                 cat.append(dc)
#         except Exception as e:
#             print(f"erro: {e}")
#     return cat


# def rel(cat):
#     valores = [c["valor"] for c in cat]
#     if valores:
#         print(f"total de vendas = {sum(valores):.2f}")
#         print(f"média de vendas = {sum(valores) / len(valores):.2f}")


# conteudo_bruto = """id,nome,valor,status
# 1, MARCOS SILVA , 150.50 , pago
# 2, ANA PAULA , 80.00 , cancelado
# 3, LUCAS MENDES , 300.00 , pago"""


# anal = Path("dados")
# caminho = anal / "dados.txt"
# anal.mkdir(parents=True, exist_ok=True)
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         f.write(conteudo_bruto)
# except Exception as e:
#     print(f"erro: {e}")
    
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         linhas = f.readlines()
#         dl = ll(linhas)
#         rel(dl)
#         for item in dl:
#             print(item)
# except Exception as e:
#     print(f"erro: {e}")




# def ge(linhas):
#     cabecalho = [c.strip() for c in linhas[0].strip().split(",")]
#     dados = linhas[1:]
#     cat = []

#     for linha in dados:
#         linha = linha.strip()
#         partes = linha.split(",")
#         try:
#             c = partes[0].strip()
#             i = partes[1].strip().title()
#             p = float(partes[2].strip())
#             qtd = int(partes[3].strip())

#             if qtd > 0:
#                 vl = [c, i, p, qtd]
#                 dc = dict(zip(cabecalho, vl))
#                 cat.append(dc)
#         except Exception as e:
#             print(f"Erro na linha: {e}")

#     return cat



# def gr(cat):
#     # Extrai o patrimônio total (preço * quantidade) de cada produto
#     totais = [item["preco"] * item["quantidade"] for item in cat]

#     if totais:
#         print("\n--- DETALHAMENTO POR PRODUTO ---")
#         for item in cat:
#             subtotal = item["preco"] * item["quantidade"]
#             print(f"Item: {item['item']} | Qtd: {item['quantidade']} | Total: R$ {subtotal:.2f}")

#         print("\n=== RESUMO PATRIMONIAL ===")
#         print(f"Patrimônio Total: R$ {sum(totais):.2f}")
#         print(f"Média por Item:   R$ {sum(totais) / len(totais):.2f}")
#     else:
#         print("Nenhum produto válido encontrado.")



# est = """codigo,item,preco,quantidade
# P1, TECLADO , 150.00 , 10
# P2, MOUSE , 50.00 , 0
# P3, MONITOR , 800.00 , 5"""

# estoque = Path("estoque")
# caminho = estoque / "estoque.txt"
# estoque.mkdir(parents=True, exist_ok=True)

# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         f.write(est)
# except Exception as e:
#     print(f"erro: {e}")

# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         linhas = f.readlines()

#     dados_limpos = ge(linhas)
#     gr(dados_limpos)

# except Exception as e:
#     print(f"erro: {e}")


# dados = """id,aluno,nota,frequencia
# 101, CARLOS SILVA , 8.5 , 85
# 102,linha_com_erro_de_leitura
# 103, ANA PAULA , 4.0 , 90
# 104, LUCAS MENDES , 9.0 , 60
# 105, BEATRIZ LIMA , 7.5 , 75"""

# escola = Path("dados")
# caminho = escola / "dados.txt"
# escola.mkdir(parents=True, exist_ok=True)

# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         f.write(dados)
# except Exception as e:
#     print(f"Erro na escrita: {e}")

# ap = []
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         linhas = f.readlines()
#         cabecalho = [c.strip() for c in linhas[0].strip().split(",")]  
#         ob = linhas[1:]

#         for linha in ob:
#             linha = linha.strip()
#             partes = linha.split(",")
#             try:
#                 c = partes[0].strip()
#                 n = partes[1].strip().title()
#                 p = float(partes[2].strip())
#                 freq = int(partes[3].strip())

#                 if p >= 7 and freq >= 75:
#                     vl = [c, n, p, freq]
#                     dc = dict(zip(cabecalho, vl))
#                     ap.append(dc)
#             except Exception as e:
#                 print(f"Erro na linha ignorada: {e}")


#         for item in ap:
#             print(f"aluno: {item['aluno']} | nota: {item['nota']} | frequencia: {item['frequencia']}%")

#         na = [a["nota"] for a in ap]
#         if na:
#             print(f"\nmédia de notas: {sum(na)/len(na):.2f}")
#             print(f"maior nota:     {max(na)}")
#             print(f"menor nota:     {min(na)}")

# except Exception as e:
#     print(f"erro: {e}")

# dados = """placa,modelo,quilometragem,revisado
# ABC1234, gol 1.0 , 45000.5 , sim
# XYZ9999,linha_corrompida_sem_dados
# DEF5678, uno mille , 120000.0 , nao
# GHI9012, corolla , 15000.0 , SIM"""
# frota = Path("dados")
# caminho = frota / "dados.txt"
# frota.mkdir(parents=True, exist_ok=True)
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         f.write(dados)
# except Exception as e:
#     print(f"erro: {e}")
# rev = []
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         linhas = f.readlines()
#         cabecalho =[c.strip() for c in linhas[0].strip().split(",")]
#         ob = linhas[1:]
#         for linha in ob:
#             linha = linha.strip()
#             partes = linha.split(",")
#             try:
#                 placa = partes[0].strip()
#                 modelo = partes[1].strip().title()
#                 quilo = float(partes[2].strip())
#                 revisado = partes[3].strip().lower()
#                 if revisado == "sim":
#                     vl = [placa, modelo, quilo, revisado]
#                     dc = dict(zip(cabecalho, vl))
#                     rev.append(dc)
#             except Exception as e:
#                 print(f"erro: {e}")
#         for item in rev:
#             print(f"{item['placa']} - {item['modelo']} - {item['quilometragem']} - {item['revisado']}")
#         q = [r['quilometragem'] for r in rev]
#         if q:
#             print(f"quilometragem média: {sum(q)/len(q):.2f}")
#             print(f"maior {max(q)}")
#             print(f"menor {min(q)}")
# except Exception as e:
#     print(f"erro:{e}")

# vendas = """id,item,categoria,valor,status
# 101, fone bluetooth , eletronicos , 150.00 , pago
# 102,linha_invalida
# 103, cadeira gamer , moveis , 1200.00 , pago
# 104, mouse sem fio , eletronicos , 80.00 , CANCELADO
# 105, teclado mecanico , eletronicos , 350.00 , PAGO"""
# v = Path("vendas")
# caminho = v / "vendas.txt"
# v.mkdir(parents=True, exist_ok=True)
# res = []
# try:
#     with open(caminho, "w", encoding="utf-8") as f:
#         f.write(vendas)
# except Exception as e:
#     print(f"erro:{e}")
# try:
#     with open(caminho, "r", encoding="utf-8") as f:
#         linhas = f.readlines()
#         cabecalho = [c.strip() for c in linhas[0].strip().split(",")]
#         ob = linhas[1:]
#         for linha in ob:
#             linha = linha .strip()
#             partes = linha.split(",")
#             try:
#                 c = partes[0].strip()
#                 i = partes[1].strip().title()
#                 t = partes[2].strip().lower()
#                 p = float(partes[3].strip())
#                 status = partes[4].strip().lower()
#                 if status == "pago" and t == "eletronicos":
#                     vl = [c, i, t, p, status]
#                     dc = dict(zip(cabecalho, vl))
#                     res.append(dc)
#             except Exception as e:
#                 print(f"erro: {e}")
#         for item in res:
#             print(f"{item['id']} - {item['item']} - {item['categoria']} - {item['valor']} - {item['status']}")
#         val = [r["valor"] for r in res]
#         if val:
#             print(f"total {sum(val)}")
#             print(f"média {sum(val)/len(val)}")
#             print(f"maior {max(val)}")
#             print(f"menor {min(val)}")
# except Exception as e:
#     print(f"erro: {e}")

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
