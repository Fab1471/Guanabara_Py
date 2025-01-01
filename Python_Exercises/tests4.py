class Pessoa:
    # Método construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método da classe
    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criando um objeto da classe Pessoa
pessoa = Pessoa("João", 25)

# Chamando o método saudacao()
pessoa.saudacao()
