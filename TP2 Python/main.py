def main():
  while True:
    print("/nEscolha uma opção: ")
    print("1 - Executar 'Nivel Minhoquinha'")
    print("2 - Executar 'Nivel Minhoquinha 2'")
    print("3 - Executar 'Nivel Minhoquinha 3'")
    print("4 - Executar 'Nivel Minhoquinha 4'")
    print("5 - Executar 'Nivel Minhoquinha 5'")
    print("6 - Executar 'Nivel Minhoquinha 6'")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
      nivel_minhoquinha()

    elif opcao == "2":
      nivel_minhoquinha2()

    elif opcao == "3":
      nivel_minhoquinha3()

    elif opcao == "4":
      mensagem = input("Digite a mensagem para imprimir: ")
      imprime_mensagem(mensagem)
      break

    elif opcao == "5":
      nome = input("Seu nome: ")
      saudacao(nome)

    elif opcao == "6":
      nome = input("Seu nome (ou deixe em branco para saudação genérica): ")
      nivel_minhoquinha6(nome)

    elif opcao == "0":
      print("Saindo do programa...")

    else:
      print("Opção inválida. Tente novamente.")
      break




def nivel_minhoquinha():
  palavra = input("Digite a string: ")

  lista = []

  for i in palavra:
    lista.append(i)

  print(lista)




def nivel_minhoquinha2():
  lista = []

  while True:
    numero = input("Digite um número: Ou 0 para parar.")
    if numero == "0":
      break
    lista.append(numero)

    print("A lista final é: ", lista)



def nivel_minhoquinha3():
  lista = []

  print("Digite o número: Ou digite 'Sair' para parar o programa.")

  while True:
    entrada = input("Digite 'Sair para parar o programa.'")

    if entrada.lower() == "sair":
      break

    try:
      numero = float(entrada)
      lista.append(numero)

    except ValueError:
      print("Entrada inválida. Por favor, digite um número ou 'sair'.")
    
    soma = 0

    for numero in lista:
      soma += numero

    if len(lista) > 0:
      media = soma / len(lista)
      print("A média dos valores da lista é: ", media)
    
    else:
      print("Nenhum número foi adicionado à lista!")



def imprime_mensagem(mensagem):
  print("Olá", mensagem, "Tudo bem?")



def saudacao(nome):
  print("Olá ", nome + " você ainda vai ser um excelente programador.")
  


def nivel_minhoquinha6(nome=""):
  if nome:
    print("Olá ", nome + " você ainda vai ser um excelente programador.")
  else:
    print("Olá, seja bem vindo ao programa.")


main()