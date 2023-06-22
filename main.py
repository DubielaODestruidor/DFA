class DFATransdutor:
    def __init__(self):
        # Definindo os estados, alfabetos e transições
        self.estados = {'q0', 'q1', 'q2'}
        self.alfabeto_entrada = {'a', 'b', 'c', '+', '(', ')', ' '}
        self.alfabeto_saida = {'x'}
        self.transicoes = {
            'q0': {'a': ('q1', 'x'), 'b': ('q1', 'x'), 'c': ('q1', 'x'), '+': ('q2', '+'),
                   '(': ('q2', '('), ')': ('q2', ')'), ' ': ('q2', ' ')},
            'q1': {'a': ('q1', 'x'), 'b': ('q1', 'x'), 'c': ('q1', 'x'), '+': ('q2', '+'),
                   '(': ('q2', '('), ')': ('q2', ')'), ' ': ('q2', ' ')},
            'q2': {'a': ('q1', 'x'), 'b': ('q1', 'x'), 'c': ('q1', 'x'), '+': ('q2', '+'),
                   '(': ('q2', '('), ')': ('q2', ')'), ' ': ('q2', ' ')}
        }
        self.estado_atual = 'q0'

    def processar_entrada(self, cadeia_entrada):
        # Começa com o estado inicial, e a cadeia de saída vazia
        cadeia_saida = ''
        self.estado_atual = 'q0'

        for simbolo in cadeia_entrada:
            if simbolo in self.alfabeto_entrada:
                # Muda de estado e pega a saída
                self.estado_atual, saida = self.transicoes[self.estado_atual].get(simbolo, (None, None))
                if saida:
                    # Concatena a saída
                    cadeia_saida += saida
            else:
                print(simbolo)

        return cadeia_saida


# Exemplo de uso
transdutor = DFATransdutor()

cadeia_entrada_1 = 'abc+ (+) ab ()'
cadeia_saida_1 = transdutor.processar_entrada(cadeia_entrada_1)
print(cadeia_entrada_1, '->', cadeia_saida_1)

cadeia_entrada_2 = 'abc + (ab +  ) ab ()'
cadeia_saida_2 = transdutor.processar_entrada(cadeia_entrada_2)
print(cadeia_entrada_2, '->', cadeia_saida_2)
