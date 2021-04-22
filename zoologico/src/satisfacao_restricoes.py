class Restricao():
    def __init__(self, variaveis):
        self.variaveis = variaveis

    def esta_satisfeita(self, atribuicao):
      return True

class SatisfacaoRestricoes():
  def __init__(self, variaveis, dominios):
    self.variaveis = variaveis # Variáveis para serem restringidas
    self.dominios = dominios # Domínio de cada variável
    self.save = ""
    self.restricoes = {}
    for variavel in self.variaveis:
        self.restricoes[variavel] = []
        if variavel not in self.dominios:
            raise LookupError("Cada variávei precisa de um domínio")

  def adicionar_restricao(self, restricao):
    for variavel in restricao.variaveis:
      if variavel not in self.variaveis:
        raise LookupError("Variável não definida previamente")
      else:
        self.restricoes[variavel].append(restricao)

  def esta_consistente(self, variavel, atribuicao):
    for restricoes in self.restricoes[variavel]:
      if not restricoes.esta_satisfeita(atribuicao):
        return False
    return True

  def forward(self, possiveis, atribuicao):
    valores = possiveis.values()
    valores_list = list(valores)

    variaveis_nao_atribuida  = [v for v in self.variaveis if v not in atribuicao]

    for variavel in variaveis_nao_atribuida:
        listval = {variavel:valores_list[0]}
        possiveis.update(listval)
        if self.esta_consistente(variavel,possiveis) == False:
          if (len(self.dominios[variavel]) != 1):
            self.dominios[variavel].remove(valores_list[0])
            possiveis.pop(variavel)
          else:
            break
            
                
                  
  def busca_backtracking(self, atribuicao = {}):
    menor = 5
    if len(atribuicao) == len(self.variaveis):
      return atribuicao

    # pega todas as variáveis que ainda não foram atribuídas
    variaveis_nao_atribuida  = [v for v in self.variaveis if v not in atribuicao]
    primeira_variavel = variaveis_nao_atribuida[0]

    #MRV pega a variavel com menos domínios 
    if len(atribuicao)!=0:
      self.forward(self.save,atribuicao)
      for val in variaveis_nao_atribuida:
        if(len(self.dominios[val])<menor):
          primeira_variavel = val
          menor = len(self.dominios[val])
    else:
      primeira_variavel = variaveis_nao_atribuida[0]

    for valor in self.dominios[primeira_variavel]:

      atribuicao_local = atribuicao.copy()
    
      atribuicao_local[primeira_variavel] = valor
      # estamos consistentes, seguir recursão
      if self.esta_consistente(primeira_variavel, atribuicao_local):
        atribuicao_save = {primeira_variavel:valor}
        self.save = atribuicao_save
        resultado  = self.busca_backtracking(atribuicao_local)
        # para o backtracking se não encontra todos os resultados
        if resultado is not None:
          return resultado
    return None