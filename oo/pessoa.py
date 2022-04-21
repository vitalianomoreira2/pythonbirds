class Pessoa:
    def __init__(self, *filhos,nome=None, idade=34):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'
if __name__== '__main__':

    vital = Pessoa(nome='Vitaliano')
    raimundo = Pessoa(vital, nome='Raimundo')
    print(Pessoa.cumprimentar(raimundo))
    print(id(raimundo))
    print(raimundo.nome)
    print(raimundo.idade)
    for filho in raimundo.filhos:
        print(filho.nome)


