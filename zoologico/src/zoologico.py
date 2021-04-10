from satisfacao_restricoes import Restricao, SatisfacaoRestricoes
from itertools import chain, combinations

class Restricaozoologico(Restricao):
    def __init__(self, a1, a2, a3, a4):
        super().__init__([a1, a2, a3, a4])
        self.variaveis = [a1, a2, a3, a4]

    def esta_satisfeita(self, atribuicao):
        # se nenhum dos as está com cor atribuída, está satisfeito
        if not all(variavel in atribuicao for variavel in self.variaveis):
              return True
        valores = [atribuicao[variavel] for variavel in self.variaveis]
        return len(set(valores)) == 4

class rei(Restricao):
    def __init__(self, a1):
        super().__init__([a1])
        self.a1 = a1

    def esta_satisfeita(self, atribuicao):
        # se nenhum dos as está com cor atribuída, está satisfeito
        if self.a1 not in atribuicao:
              return True
        return atribuicao[self.a1] == 1

class amigos(Restricao):
    def __init__(self, a1, a2):
        super().__init__([a1, a2])
        self.variaveis = [a1, a2]

    def esta_satisfeita(self, atribuicao):
        # se nenhum dos as está com cor atribuída, está satisfeito
        if not all(variavel in atribuicao for variavel in self.variaveis):
              return True
        # cores de as vizinhos não podem ser igual 
        return atribuicao[self.variaveis[0]] != atribuicao[self.variaveis[1]]

class vizinhos(Restricao):
    def __init__(self, a1, a2):
        super().__init__([a1, a2])
        self.variaveis = [a1, a2]

    def esta_satisfeita(self, atribuicao):
        # se nenhum dos as está com cor atribuída, está satisfeito
        if not all(variavel in atribuicao for variavel in self.variaveis):
              return True
        # cores de as vizinhos não podem ser igual 
        return (atribuicao[self.variaveis[1]] != atribuicao[self.variaveis[0]]+1) and (atribuicao[self.variaveis[1]] != atribuicao[self.variaveis[0]]-1)


if __name__ == "__main__":
    variaveis = ["Leão", "Antílope", "Hiena", "Tigre", "Pavão", "Suricate", "Javali"]      
    dominios = {}
    for variavel in variaveis:
        dominios[variavel] = [1, 2, 3, 4]
    problema = SatisfacaoRestricoes(variaveis, dominios)
    problema.adicionar_restricao(rei("Leão"))
    problema.adicionar_restricao(amigos("Leão", "Tigre"))
    problema.adicionar_restricao(amigos("Leão", "Antílope"))
    problema.adicionar_restricao(amigos("Leão", "Pavão"))
    problema.adicionar_restricao(amigos("Tigre", "Antílope"))
    problema.adicionar_restricao(amigos("Leão", "Hiena"))
    problema.adicionar_restricao(amigos("Antílope", "Hiena"))
    problema.adicionar_restricao(amigos("Pavão", "Hiena"))
    problema.adicionar_restricao(amigos("Suricate", "Hiena"))
    problema.adicionar_restricao(amigos("Javali", "Hiena"))
    problema.adicionar_restricao(vizinhos("Leão", "Antílope"))
    problema.adicionar_restricao(vizinhos("Tigre", "Antílope"))

    resposta = problema.busca_backtracking()
    if resposta is None:
        print("Nenhuma resposta encontrada")
    else:
        print(resposta)