q = int(input("digite a quantidade de alunos para cadastro: "))
cabecalho = ["matricula", "nome", "media", "frequencia"]
aprovados = []
for i in range(q):
    print(f"========== ALUNO {i+1} ==========")
    try:
        mat = int(input("digite a matrícula do aluno: "))
        nm = input("digite o nome do aluno: ").strip().title()
        freq = int(input("digite a frequência do aluno: "))
        k = int(input("digite quantas notas desse aluno quer cadastrar:"))
        soma = 0
        for j in range(k):
            nota = float(input(f"digite a nota {j+1}: "))
            soma += nota
        media = soma / k
        if media >= 7 and freq >= 75:
            vl = [mat, nm, media, freq]
            dc = dict(zip(cabecalho, vl))
            aprovados.append(dc)
            print("========== ALUNO CADASTRADO COM SUCESSO ==========")
        else:
            print("========== ALUNO REPROVADO(NÃO ADICIONADO) ==========")
    except Exception as e:
        print(f"erro: {e}")
        print("========== FALHA NO CADASTRO ==========")
print("========== RESUMO ==========")
for item in aprovados:
    print(f"matrícula: {item['matricula']} | nome: {item['nome']} | média: {item['media']:.2f} | frequencia: {item['frequencia']}%")
geral = [a['media'] for a in aprovados]
if geral:
    print(f"de {q} alunos cadastrados, {len(aprovados)} foram aprovados")
    print(f"média das médias dos alunos aprovados: {sum(geral)/len(geral):.2f}")
    print(f"a maior média foi: {max(geral):.2f}")
    print(f"a menor média foi: {min(geral):.2f}")
else:
    print("\nnenhum aluno foi aprovado")
