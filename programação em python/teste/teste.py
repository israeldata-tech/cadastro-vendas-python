# print(10 + 20 * 30)
# nome=input("digite seu nome :")
# print(f"ola {nome}")

# a=int(input("digite um número :"))
# b=int(input("digite um número :"))
# print(2*a*3*b)

# a = int(input("digite um número "))
# b = int(input("digite um num"))
# c = int(input("digite um num"))
# print(a+b+c)

# salario = float(input("digite seu sálario :"))
# aumento = float(input("digite a porcentagem de aumento :"))
# print(salario+(salario*aumento/100))


# a = int(input("digite um número inteiro :"))
# print("o dobro é :", a*2)
# print("a raiz dele é :", a ** (1/2))

# a = float  ( input ( "nota 1 "))
# b = float  ( input ( "nota 2 "))
# c = float  ( input ( "nota 3 "))

# m = (a+b+c)/3
# print(f"a média é {m}")

# temconvite = True
# idade = int(input("digite sua idade :"))

# podeentrar = idade >= 18 and temconvite
# print(f"voÇe pode entrar?{podeentrar}")


# preço = float (input("digite o preço do produto :"))
# desconto = (preço * 0.9)
# pagamento = float (input("digite quanto pagou :"))
# troco = pagamento - desconto
# print(f"o seu troco é {troco:.2f}")


# estudante = True
# idade = int (input("digite sua idade :"))
# ganhameia = estudante or idade >= 60
# print(f"voce paga meia ? {ganhameia}")


# salario = float (input("digite seu salario :"))
# pagaimposto = salario > 1200
# print(f"voce paga imposto? {pagaimposto}")

# mat1 = float (input("nota 1 "))
# mat2 = float (input("nota 2 "))
# mat3 = float (input("nota 3 "))
# aprovado = mat1 > 7 and mat2 > 7 and mat3 > 7

# print(f"aprovado? {aprovado}")

# nome = (input("digite seu nome"))
# sobrenome = (input("digite seu sobrenome"))
# tamanho = len(nome+sobrenome)
# print(f"o nome tem {tamanho} letras", nome[0], sobrenome[0])


# palavra = input("digite uma palavra ")
# print(f"a palavra invertida é {palavra[::-1]} {palavra[:3]}")


# produto = input("digite um produto ")
# preço = float(input("digite o preço "))
# print(f"o produto {produto} custa {preço:.2f}")

# texto = input("DIGITE UMA FRASE ")
# tamanho = len(texto)
# pripa = texto.split()[0]
# maiusculo = texto.upper()
# print(f"o texto tem {tamanho} letras, a primeira palavra é {pripa}")
# print(f" o texto em maiusculo é {maiusculo}")


# logado = True
# valido = True
# aceito = logado and valido
# print(f"aceito?{aceito}")

# preço = int(input("digite o preço "))
# vip = True
# cupom = True
# desconto = vip or cupom
# print(f"o preço é {preço}. terá desconto? {desconto}")


# texto = input("digite um texto com muito espaço ")
# limpa = texto.strip().lower()
# print(f"o texto limpo é {limpa}")

# sistemaop = False
# sistem = not sistemaop
# print(f"o sistema opera? {sistem}")

# nome = input("seu nome ")
# idade = int(input("sua idade "))
# temdoc = True
# tamanho = len(nome)

# cadastrov = tamanho > 2 and idade >= 18 and temdoc
# print(f"pode cadastrar?{cadastrov}")

# a = int(input("num 1 "))
# b = int(input("num 2 "))

# print(f"a soma é {a+b}")

# metros = float(input("digite a quantidade de metros "))
# mili = metros * 1000
# print(f"o valor dá {mili} milimetros")

# dias = float(input("dias "))
# hd = dias * 24 * 60 * 60
# horas = float(input("horas "))
# sh = horas * 60 * 60
# minutos = float(input("minutos "))
# sm = minutos * 60
# segundos = float(input("segundos "))
# print(f"dias {hd} horas {sh} minutos {sm} segundos {segundos}")


# salario = float(input("valor do salario "))
# aumento = float(input("digite o aumento "))
# ns = salario + (salario * aumento / 100)
# qa = ns - salario
# print(f"o seu novo salario é {ns:.2f} o aumento foi de {qa:.2f} reais")

# preço = float(input("digite o preço "))
# desconto = float(input("digite a porcentagem de desconto "))
# np = preço - (preço * desconto / 100)
# vald = preço - np
# print(f"desconto {desconto}% economizou {vald} reais e o novo preço é {np}")

# distancia = float(input("distancia "))
# velocidade = float(input("digite a velocidade em km/h "))
# tempo = distancia / velocidade
# print(f"a viagem durara cerca de {tempo:.2f} horas")

# temperatura = float(input("digite a temperatura"))
# fahrenheit = ((temperatura * 9) / 5) + 32
# print(f"a temperatura em graus fahrenheit é {fahrenheit:.2f}")

# dias = float(input("dias usados "))
# kmp = float(input("kms usados "))
# valor = 60 * dias + kmp * 0.15
# print(f"o valor a pagar pelo carro alugado é {valor:.2f} reais ")

# cfd = float(input("digite quantos cigarros fumou por dia "))
# anos = float(input("digite por quantos anos fumou "))
# ap = (cfd * (anos * 365) * 10)/1440
# print(f"voce perdeu {ap:.2f} dias de vida")

# vel = float(input("digite sua velocidade "))

# if vel > 80:
#     multa = (vel - 80) * 5
#     print(f"voce foi multado e pagará uma multa de {multa:.2f} reais")

# a = float(input("num 1 "))
# b = float(input("num 2 "))
# c = float(input("num 3 "))
# maior = a
# menor = a
# if b > maior:
#     maior = b
# if c > maior:
#     maior = c
# if b < menor:
#     menor = b
# if c < menor:
#     menor = c
# print(f"o maior é {maior} o menor é {menor}")

# salario = float(input("seu salario "))
# if salario > 1250:
#     sn = salario * 1.10
#     print(f"seu novo salario é {sn:.2f}")
# if salario < 1250:
#     sn = salario * 1.15
#     print(f"seu novo salário é {sn:.2f}")

# disqp = float(input("digite quanto quer percorrer em km "))
# if disqp <= 200:
#     v = disqp * 0.5
#     print(f"voce pagará {v:.2f} reais")
# else:
#     v = disqp * 0.45
#     print(f"voce pagará {v:.2f} reais")

# a = float(input("digite um num "))
# b = float(input("digite outro "))
# c = input("digite uma operação")
# if c == "+":
#     print(f"resultado {a+b}")
# elif c == "-":
#     print(f"resultado {a-b}")
# elif c == "*":
#     print(f"resultado {a*b}")
# elif c == "/":
#     if b != 0:
#         print(f"resultado {a/b}")
#     else:
#         print("divisão por zero")
# else:
#     print("operação invalida")

# pc = float(input("digite o valor da casa que quer comprar "))
# salario = float(input("digite seu salario "))
# ap = float(input("digite por quantos anos quer pagar "))
# pm = pc/(ap * 12)
# aprovado = pm < salario * 0.30
# print(f"pode comprar a casa? {aprovado}")

# kus = float(input("quantos kwh usou "))
# instalação = input("digite o tipo de instalação ")
# if instalação == "r":
#     if kus <= 500:
#         v = kus * 0.40
#     else:
#         v = kus * 0.65
# elif instalação == "c":
#     if kus <= 1000:
#         v = kus * 0.55
#     else:
#         v = kus * 0.60
# elif instalação == "i":
#     if kus <= 5000:
#         v = kus * 0.55
#     else:
#         v = kus * 0.60
# else:
#     print("tipo errado ")

# print(f"voce pagara {v:.2f} reais")

# a = float(input("lado 1 "))
# b = float(input("lado 2 "))
# c = float(input("lado 3 "))

# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("é equilatero")
#     elif a == b or a == c or b == c:
#         print("isosceles")
#     else:
#         print("escaleno")
# else:
#     print("não é triangulo ")


# altura = float(input("digite sua altura "))
# peso = float(input("digite seu peso "))
# imc = peso/(altura ** 2)
# if imc < 18.5:
#     print("abaixo do peso")
# elif 18.5 < imc <= 24.9:
#     print("peso ideal ")
# elif 25 < imc <= 29.9:
#     print("sobrepeso ")
# else:
#     print("obesidade ")


# nota1 = float(input("digite a nota 1 "))
# nota2 = float(input("digite a nota 2 "))
# frequencia = float(input("digite a frequencia "))
# media = (nota1 + nota2)/2
# if frequencia >= 75 and media >= 7:
#     print("aprovado ")
# elif frequencia < 75:
#     print("reprovado por falta de frequencia ")
# elif frequencia >= 75 and 5.0 <= media < 7:
#     print("recuperação de nota ")
# elif media < 5:
#     print("reprovado por falta de nota ")


# salario = float(input("digite seu salario "))
# at = float(input("quantos anos trabalha na empresa "))
# if at > 5:
#     ns = salario * 1.15
# elif 2 <= at <= 5:
#     ns = salario * 1.10
# else:
#     ns = salario * 1.05

# if ns < 2000:
#     ns += 200
# print(f"seu novo salário é {ns:.2f}")

# x = 10
# while x > 0:
#     print(x)
#     x -= 1
#     if x == 0:
#         print("FOgOOOO")

# fim = int(input("digite o valor final "))
# x = 0
# while x < fim:
#     if x % 2 != 0:
#         print(x)
#     x += 1

# val = int(input("digite qual número quer ver os multiplos "))
# multi = int(input("digite quantos multiplos quer ver "))
# x = val
# cont = 0
# while cont < multi:
#     print(x)
#     x += val
#     cont += 1


# dep = float(input("digite o deposito inicial "))
# am = float(input("digite a porcentagem de aumento mensal "))
# x = 0
# va = dep
# vald = dep
# while x < 24:
#     va += (va * am / 100)
#     print(f"o valor atual é {va:.2f}")
#     dm = float(input("quer depositar quanto esse mês?"))
#     va += dm
#     vald += dm
#     x += 1
# c = va - vald
# print(f"o valor ganho foi de {c:.2f} reais")

# divida = float(input("digite sua divida "))
# juros = float(input("digite o juros mensal "))
# pm = float(input("digite quanto vai pagar por mês "))

# jui = divida * (juros / 100)
# if pm < jui:
#     print("valor pago menor que o juros, a divida nunca acabara ")
# else:
#     cm = 0
#     tp = 0

#     while divida > 0:

#         divida += divida * (juros/100)
#         if pm >= divida:
#             tp += divida
#             divida = 0
#         else:
#             divida -= pm
#             tp += pm
#         cm += 1
# print(f"voce vai levar {cm} meses pra terminar de pagar a divida")
# print(f"o total pago foi de {tp:.2f} reais")


# soma = 0
# qtdn = 0
# while True:
#     num = float(input("digite um número "))
#     if num == 0:
#         break
#     soma += num
#     qtdn += 1
# m = soma / qtdn
# print(f"a media é {m:.2f} a soma é {soma:.2f} teve {qtdn} numeros")

# pp = 0
# while True:
#     cod = int(input("digite o codigo do produto "))
#     qtd = int(input("digite a quantidade de produtos"))
#     if cod or qtd == 0:
#         break
#     else:
#         if cod == 1:
#             v = 0.5
#             pp += v * qtd
#         elif cod == 2:
#             v = 1
#             pp += v * qtd
#         elif cod == 3:
#             v = 4
#             pp += v * qtd
#         elif cod == 4:
#             v = 7
#             pp += v * qtd
#         elif cod == 5:
#             v = 9
#             pp += v * qtd
#     fim = int(input("digite 0 se fim e outra coisa pra continuar"))
#     if fim == 0:
#         print(f"voce pagará {pp:.2f} reais")
#         break

# tab = int(input("digite qual número quer ver a tabuada "))
# for i in range(11):
#     print(f"{tab} x {i} = {tab * i}")

# for i in range(10, -1, -1):
#     print(f"{i}")
#     if i == 0:
#         print("decolagem")

# fim = int(input("digite o limite "))
# soma = 0
# for i in range(1, fim+1):
#     if (i % 2 != 0):
#         soma += i
# print(f"a soma dos impares ate {fim} è {soma}")

# while True:
#     num = int(input("digite um númnero pra ver se é primo "))
#     if num <= 1:
#         print("programa encerrado")
#         break
#     p = True
#     for i in range(2, num):
#         if num % i == 0:
#             p = False
#             break
#     if p:
#         print(f"{num} é primo")
#     else:
#         print(f"{num} não é primo")

# while True:
#     qtda = int(input("digite a quantidade de alunos "))
#     if qtda <= 0:
#         print("invalido ")
#         break
#     soma = 0

#     for i in range(1, qtda+1):

#         nota = float(input(f"digite a nota do aluno {i} "))
#         while nota < 0 or nota > 10:
#             print("nota invalida ")
#             nota = float(input(f"digite a nota do aluno {i} "))
#         soma += nota

#     media = soma / qtda
#     print(f"a média da turma é {media:.2f}")

# while True:
#     val = int(input("digite o valor a sacar "))
#     if val <= 0:
#         print("valor invalido ")
#         break
#     for cedula in (50, 20, 10, 5, 1):
#         qtdn = val // cedula
#         val = val % cedula
#         if qtdn > 0:
#             print(f"voce sacou {qtdn} de {cedula}")

tam = int(input("digite o tamanho da lista "))
lista = []
for i in range(tam):
    num = int(input(f"digite o número {i+1}"))
    lista.append(num)
for num in lista:
    if (num % 2 == 0):
        print(f"{num} é par")
