def printParametro(x):
    print(x)


Pessoas = ["Joao","Maria","Jose"]
LetrasIniciaisQuePodemEntrar = ("J","A","B")

Status = {"HP":50, "Stamina":100}








'''










Livro1 = {"Titulo":"Revolta das maquinas" , "Ano":1988}
Livro2 = {"Titulo":"Caminho da dor" , "Ano":2017}
Prateleira = [Livro1, Livro2]


nImpar = [1, 3, 5, 7, 9, 11]

def pegavalor(valor, posicaodesejada):
    print(valor[posicaodesejada])

pegavalor(nImpar, 5)

'''
'''
Crie uma função que receba uma lista de qualquer 
tamanho com as horas trabalhadas por dia um funcionário. 
Esta função deve ao final retornar a média aritmética das
horas trabalhadas. Este retorno deve ser utilizado para 
imprimir a situação do funcionário: "Carga-horário ok", 
se média maior ou igual a 30 e "Falar com o RH", caso o 
contrário.(2,0)'''

TrabalhadorJoao = {"Nome":"Joao", "Setor":"Financas", "HorasTrabalhadas":[60, 20, 1]}

OdeioTrabalhar = [30, 30, 30, 30, 30, 30,30, 30, 30,30, 30, 30,30, 30, 30,30, 30, 30,30, 30, 30,30, 30, 30,29, 30, 30,30, 30, 30,30, 30, 30,30, 30, 30]


def CalcularCargaHoraria(Horas):

    media = 0
    contador = 0

    while contador < len(Horas):
        media = media + Horas[contador]
        contador = contador + 1

    media = media / len(Horas)

    if media >= 30:
        print("Carga Horaria OK!")
    else:
        print("Falar com o RH.")

CalcularCargaHoraria(OdeioTrabalhar)





