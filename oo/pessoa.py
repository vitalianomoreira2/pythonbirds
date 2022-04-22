class Pessoa:
    olhos = 2
    def __init__(self, *filhos,nome=None, idade=34):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'Ola {cls} - olhos{cls.olhos}'

if __name__== '__main__':

    vital = Pessoa(nome='Vitaliano')
    raimundo = Pessoa(vital, nome='Raimundo')
    print(Pessoa.cumprimentar(raimundo))
    print(id(raimundo))
    print(raimundo.nome)
    print(raimundo.idade)
    for filho in raimundo.filhos:
        print(filho.nome)
    vital.sobrenome = 'Moreira'
    del raimundo.filhos ## excluindo um atributo do objeto dinamicamente
    print(vital.__dict__)
    print(raimundo.__dict__)
    Pessoa.olhos = 1
    print(Pessoa.olhos)
    print(Pessoa.olhos)
    print(vital.olhos)
    print(raimundo.olhos)
    print(id(Pessoa.olhos), id(raimundo.olhos), id(vital.olhos))
    print(Pessoa.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), vital.nome_e_atributos_de_classe())