from datetime import datetime

# 1) Na disciplina de Modelagem de Padrões de Projetos você e seu grupo estão desenvolvimento um
# Sistema WEB que faz uso de Orientação à Objetos. Implemente em Python todas as Classes da camada
# de negócio existentes em seu projeto.

class Produto:
    def __init__(self, nome, preco, tipo, dataFabricacao, dataValidade):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.dataFabricacao = dataFabricacao
        self.dataValidade = dataValidade
        self.dataCriacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # ====

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    # ====

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco

    # ====

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    # ====

    def getDataFabricacao(self):
        return self.dataFabricacao

    def setDataFabricacao(self, dataFabricacao):
        self.dataFabricacao = dataFabricacao

    # ====

    def getDataValidade(self):
        return self.dataValidade

    def setDataValidade(self, dataValidade):
        self.dataValidade = dataValidade

    # ====

    def getDataCriacao(self):
        return self.dataCriacao
    
# ======================================================================================================================

class User:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.dataCriacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # ====

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    # ====

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    # ====

    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        self.senha = senha

    # ====

    def getDataCriacao(self):
        return self.dataCriacao

# LOCAL ONDE DEVE SER A MAIN

    produto = Produto("Produto A", "10.00", "Alimento", "2024-01-01", "2024-12-31")
    user = User("João", "joao@example.com", "senha123")
    
    print(user.getDataCriacao())
    print(produto.getDataCriacao())
