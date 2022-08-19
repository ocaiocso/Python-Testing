class Pessoa(object):
    __nome = " "
    __ano_nasc = 0
    __idade = 0

    def __init__(self, n, ano):
        self.__nome = n
        self.__ano_nasc = ano
        self.__idade = 2022 - ano

    def exibirinfo(self):
        print("Nome: ", self.__nome)
        print("Ano Nascimento: ", self.__ano_nasc)
        print("Idade: ", self.__idade)

class PessoaJuridica(Pessoa):
    __cnpj = " "

    def __init__(self, n, ano, cnpj):
        Pessoa.__init__(self, n, ano)
        self.__cnpj = cnpj

    def exibirinfo(self):
        super().exibirinfo()
        print("CNPJ", self.__cnpj)

class PessoaFisica(Pessoa):
    __rg = " "

    def __init__(self, n, ano, rg):
        Pessoa.__init__(self, n, ano)
        self.__rg = rg

    def exibirinfo(self):
        super().exibirinfo()
        print("RG: ", self.__rg)

p1 = Pessoa("Thiago", 1979)
p2 = PessoaFisica("Caio", 2003, "1234-X")
pj1 = PessoaJuridica("Unisantos", 1951, "123456789")

p1.exibirinfo()
p2.exibirinfo()
pj1.exibirinfo()