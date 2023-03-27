#Aula de Variáveis


#nome = input("Digite seu nome:")
#print("Você digitou %s" % nome)
#print("Olá, %s!" % nome)

#anos = int(input("Anos de serviço:"))
#valor_por_ano = float(input("Valor por ano:"))
#bônus = anos * valor_por_ano
#print("Bônus de R$ %5.2f" % bônus)


#nome = input("Digite seu nome: ")
#idade = int(input("Digite sua idade: "))
#saldo = float(input("Digite o saldo da sua conta bancária: "))
#print(nome)
#print(idade)
#print(saldo)

#----------------------------------------------------------------------------

#Condicionais

#a= int(input("Primeiro valor:"))
#b= int(input("Segundo valor:"))

#if a>b:
    #print("O primeiro número é o maior")

#if b>a:
    #print("O segundo valor é maior")


#Listagem 4.3

#idade= int(input("Digite a idade do seu carro: "))
#if idade <= 3:
    #print("Seu carro é novo")
#if idade > 3:
    #print("Seu carro é velho")


#Listagem 4.4 – Cálculo do Imposto de Renda

#salário= float(input("Digite o salário para o cálculo do imposto:"))
#base= salário
#imposto= 0

#if base > 3000:
    #imposto = imposto + ((base - 3000) * 0.35)
    #base = 3000

#if base > 1000:
    #imposto = imposto + ((base - 1000) * 0.20)

#print("Salário: R$%6.2f Imposto a pagar: R$6.2f %")

#----------------------------------------------------------------------------

#else

#idade = int(input("Digite a idade do seu carro:"))
#if idade<=3:
    #print("Seu carro é novo")
#else:
    #print("Seu carro é velho")

#Listagem - Conta de telefone com três faixas de preço

#----------------------------------------------------------------------------

#minutos= int(input("Quantos minutos você utilizou este mês:"))
#if minutos < 200:
    #preço = 0.20
#else:
    #if minutos < 400:
       #preço = 0.18
    #else:
        #preço = 0.15

#print("Você vai pagar este mês: R$%6.2f" % (minutos * preço))

#----------------------------------------------------------------------------

#Repetições

#x=1
#while x<=10:
    #print(x)
    #x= x + 1

#fim=int(input("Digite o último número"))
#x = 1
#while x <=fim:
    #x = 1
    #while x<= fim:
        #print(x)
        #x = x + 1


#----------------------------------------------------------------------------

#fim = int(input("Digite o último número a imprimir:"))

#x = 0
#while x <= fim:
    #if x % 2 == 0:
        #print(x)
    #x = x + 2

#----------------------------------------------------------------------------

fim=int(input("Digite o último número a imprimir:"))
x = 0
while x <=fim:
    if x % 2 == 0:
        print(x)
    x = x + 1

#----------------------------------------------------------------------------

#Listagem – Contagem de questões corretas

pontos = 0
questão = 1
while questão <=3:
    resposta = input("Resposta da questão %d: " % questão)
    if questão == 1 and resposta == "b":
        pontos = pontos + 1
    if questão == 2 and resposta == "a":
        pontos = pontos + 1
    if questão == 3 and resposta == "d":
        pontos = pontos + 1
    questão += 1

print("O aluno fez %d ponto(s)" % pontos)

#----------------------------------------------------------------------------

#Listagem 1 - Soma de 10 números

n = 1
soma = 0

while n <= 10:
    x= int(input("Digite o %d número:"%n))
    soma = soma + x
    n = n + 1

print("Soma: %d"%soma)

#----------------------------------------------------------------------------

#Listagem – Cálculo de média com acumulador
x = 1
soma = 0

while x<= 5:
    n = int(input("%d Digite o número:" % x))
    soma = soma + n
    x = x + 1

print("Média: %5.2f" % (soma/5))

#----------------------------------------------------------------------------

#Listagem – Interrompendo a repetição

s=0
while True:
    v=int(input("Digite um número a somar ou 0 para sair:"))
    if v == 0:
        break
    s = s + v

print(s)























