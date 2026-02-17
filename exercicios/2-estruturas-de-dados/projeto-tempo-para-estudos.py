# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome=input("Olá! Qual é seu nome? ")
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias=int(input("Quantos dias foram dedicados ao estudo essa semana? "))
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas=float(input("Qual é a média de horas estudadas por dia? "))
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso=input("Me diga o título do curso desejado: ")
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print("Pois bem, aqui está um resumo de suas informações: ")
print(f"Nome: {nome}")
print(f"Curso desejado: {curso}")
print(f"Dias estudados: {total_dias}")
print(f"Média de horas diária: {total_horas}")
print(f"Horas totais estudadas: {total_dias*total_horas} horas estudadas essa semana")