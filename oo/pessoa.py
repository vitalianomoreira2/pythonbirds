


class Pessoa:
    def cumprimentar(self):
        return f'Ola {id(self)}'
if __name__== '__main__':

    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(f'Olá', id(p))
    print(p.cumprimentar())
