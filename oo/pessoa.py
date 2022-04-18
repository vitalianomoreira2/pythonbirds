class Pessoa:
    def __init__(self, nome=None, idade=34):
        self.idade=idade
        self.nome=nome

    def cumprimentar(self):
        return f'Ola {id(self)}'
if __name__== '__main__':

    p = Pessoa('Vitaliano')
    print(Pessoa.cumprimentar(p))
    print(f'Olá', id(p))
    print(p.cumprimentar())
    p.nome='Moreira'
    print(p.nome)
    print(p.idade)
