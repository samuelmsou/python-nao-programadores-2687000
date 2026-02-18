# Nesse desafio você verificará dentro de uma lista se o item está contido nela, 
# caso verdadeiro deverá imprimir na tela essa informação, 
# além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.

# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
lista_cursos=['Excel','Marketing','Dados','SQL','Python']
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
print("Iremos adicionar seus cursos na lista de cursos.")
curso1=input("1. Diga o nome do curso: ")
lista_cursos.append(curso1)

curso2=input("2. Diga o nome do curso: ")
lista_cursos.append(curso2)

curso3=input("3. Diga o nome do curso: ")
lista_cursos.append(curso3)

print(lista_cursos)

# 3. Crie um dicionário vazio para armazenar a nota do curso
dict_notas={}


# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista

if curso1 in lista_cursos:
  dict_notas[curso1]=int(input(f"Dê uma nota de 1 a 10 para o curso {curso1}: "))

if curso2 in lista_cursos:
  dict_notas[curso2]=int(input(f"Dê uma nota de 1 a 10 para o curso {curso2}: "))

if curso3 in lista_cursos:
  dict_notas[curso3]=int(input(f"Dê uma nota de 1 a 10 para o curso {curso3}: "))


# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

print(dict_notas)