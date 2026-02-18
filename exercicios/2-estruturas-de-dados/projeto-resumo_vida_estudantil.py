# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

estudante={}

estudante['nome']=input("Qual o seu nome? ")
estudante['ano_que_conheceu_linkedin']=int(input("Em que ano você conheceu o LinkedIn? "))
estudante['ano_atual']=int(input("Informe o ano atual: "))
cursos=input("Informe os cursos realizados no LinkedIn Learning em ordem cronológica (separe-os com vírgula + espaço): ")

estudante['cursos']=cursos.split(', ')
print(estudante)


total_anos= estudante['ano_atual']-estudante['ano_que_conheceu_linkedin']
total_cursos=len(estudante['cursos'])


print(f"Olá, {estudante['nome']}, segue suas informações:")
print(f'Ano em que conheceu o LinkedIn: {estudante["ano_que_conheceu_linkedin"]}')
print(f'Total de anos transcurridos: {total_anos}')
print(f'Total de cursos realizados: {total_cursos}')
print(f'Seu primeiro curso foi {estudante["cursos"][0]} e o último foi {estudante["cursos"][-1]}')