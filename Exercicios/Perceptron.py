import numpy as np

class Perceptron:

    # Inicializa os pesos e bias da rede neural (CONSTRUTOR)
    def __init__(self):
        self.w1 = np.random.uniform(-1, 1)
        self.bias = np.random.uniform(-1, 1)

    # Função de ativação sigmoide
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def treinamento(self, entradas, saidas, taxaAprendizado, epocas):

        self.entradas = np.array(entradas)
        self.saidas = np.array(saidas)
        self.taxaAprendizado = taxaAprendizado
        self.epocas = epocas

        # Treinamento da rede
        for i in range(self.epocas):
            for j in range(len(self.entradas)):

                # Calcula a saída da rede
                entrada = self.entradas[j]
                saida_real = self.saidas[j]
                soma = self.w1 * entrada + self.bias
                saida_predita = self.sigmoid(soma)

                # Calcula o erro
                erro = saida_real - saida_predita

                # Atualiza os pesos e o bias
                self.w1 += self.taxaAprendizado * erro * entrada
                self.bias += self.taxaAprendizado * erro


    # Predição da classe de uma nova entrada
    def predicao(self, entrada):

        soma = self.w1 * entrada + self.bias
        saida_predita = self.sigmoid(soma)

        # Desnormaliza a saída para obter a nota final
        return saida_predita * 10


# Gerando dados aleatórios para os 50 alunos

np.random.seed(0)  # Reprodução dos resultados
horas_estudo_alunos = np.random.uniform(1, 15, 50)  # Horas de estudo dos alunos
notas_alunos = np.random.uniform(0, 10, 50)  # Notas dos alunos
notas_normalizadas = notas_alunos / 10.0  # Normalizando as notas para o intervalo [0, 1]

# Criando lista com os dados dos alunos
dados_alunos = list(zip(horas_estudo_alunos, notas_normalizadas))

# Criação do Perceptron
perceptron = Perceptron()

# Treinamento do Perceptron
perceptron.treinamento(horas_estudo_alunos, notas_normalizadas, taxaAprendizado=0.01, epocas=1000)

# Fazendo previsões para os próximos alunos
print("\nPrevisões para os próximos alunos:")

for i in range(50):
    horas_estudo_aluno_novo = np.random.uniform(1, 15)
    nota_prevista = perceptron.predicao(horas_estudo_aluno_novo)
    print(f"Aluno {i+1}: Horas de estudo = {horas_estudo_aluno_novo:.2f} horas, Nota prevista = {nota_prevista:.2f}")
