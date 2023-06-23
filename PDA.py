class PDA:
    def __init__(self):
        self.estados = set()  # Conjunto de estados
        self.alfabeto = set()  # Alfabeto de entrada
        self.alfabeto_pilha = set()  # Alfabeto da pilha
        self.transicoes = {}  # Função de transição
        self.estado_inicial = None  # Estado inicial
        self.estados_aceitacao = set()  # Conjunto de estados de aceitação

    def adicionar_estado(self, estado):
        self.estados.add(estado)

    def definir_estado_inicial(self, estado):
        self.estado_inicial = estado

    def adicionar_estado_aceitacao(self, estado):
        self.estados_aceitacao.add(estado)

    def adicionar_transicao(self, estado, simbolo, topo_pilha, novo_estado, simbolos_empilhar):
        chave = (estado, simbolo, topo_pilha)
        self.transicoes[chave] = (novo_estado, simbolos_empilhar)

    def processar_entrada(self, cadeia_entrada):
        pilha = ['Z']  # Inicializa a pilha com um símbolo especial 'Z'
        estado_atual = self.estado_inicial

        for simbolo in cadeia_entrada:
            if (estado_atual, simbolo, pilha[-1]) in self.transicoes:
                novo_estado, simbolos_empilhar = self.transicoes[(estado_atual, simbolo, pilha[-1])]
                pilha.pop()  # Remove o símbolo do topo da pilha
                pilha.extend(simbolos_empilhar)  # Empilha os novos símbolos
                estado_atual = novo_estado
            else:
                return False

        return estado_atual in self.estados_aceitacao and len(pilha) == 1


# Exemplo de uso do PDA
pda = PDA()

# Definição dos estados
pda.adicionar_estado('q0')
pda.adicionar_estado('q1')

# Definição do alfabeto
pda.alfabeto = {'a', 'b'}

# Definição do alfabeto da pilha
pda.alfabeto_pilha = {'Z', 'a'}

# Definição do estado inicial
pda.definir_estado_inicial('q0')

# Definição dos estados de aceitação
pda.adicionar_estado_aceitacao('q1')

# Definição das transições
pda.adicionar_transicao('q0', 'a', 'Z', 'q0', ['a', 'Z'])
pda.adicionar_transicao('q0', 'a', 'a', 'q0', ['a', 'a'])
pda.adicionar_transicao('q0', 'b', 'a', 'q1', [])
pda.adicionar_transicao('q1', 'b', 'a', 'q1', [])

# Teste de strings
print(pda.processar_entrada('aabb'))  # True
print(pda.processar_entrada('aabbb'))  # False
