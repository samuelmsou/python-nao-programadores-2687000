# Crie uma função para selecionar o curso desejado em uma trilha profissional
def selecao_curso ():
  curso=int(input("Qual curso você quer? 1. Python 2. SQL. Digite o número do curso:"))
  if curso ==1:
     return "Python"
  if curso ==2:
     return "SQL"


# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual

def percorrer_niveis ():
  nivel_atual=int(input(f"Informe seu nível atual para o curso *{curso_escolhido}* (nível 1 a 5): "))
  while nivel_atual <5:
    print(f"Parabéns! Você está no nível {nivel_atual}. Continue progredindo.")
    nivel_atual+=1
  else:
      print(f"Você chegou no nível {nivel_atual} e concluiu o curso {curso_escolhido}. Mandou benzão.")



# Execute as funções

curso_escolhido=selecao_curso()
print(f"Seu curso escolhido é {curso_escolhido}")

percorrer_niveis()

