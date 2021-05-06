
class Pessoa:
    def __init__(self, tipo, nome, formacao, monitoria):
        self.tipo = tipo
        self.nome = nome
        self. formacao = formacao
        self.monitoria = monitoria

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getFormacao(self):
        return self.formacao

    def setFormacao(self, formacao):
        self.formacao = formacao

    def getMonitoria(self):
        return self.monitoria

    def setTMonitoria(self, monitoria):
        self.monitoria = monitoria

