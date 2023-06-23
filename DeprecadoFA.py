class DFATransdutor:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2'}
        self.alfabeto_entrada = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '+', '(', ')', ' '}
        self.alfabeto_saida = {'x'}
        self.transicoes = {
            'q0': {'a': ('q1', 'x'), 'b': ('q1', 'x'), 'c': ('q1', 'x'), 'd': ('q1', 'x'), 'e': ('q1', 'x'),
                   'f': ('q1', 'x'), 'g': ('q1', 'x'), 'h': ('q1', 'x'), 'i': ('q1', 'x'), 'j': ('q1', 'x'),
                   'k': ('q1', 'x'), 'l': ('q1', 'x'), 'm': ('q1', 'x'), 'n': ('q1', 'x'), 'o': ('q1', 'x'),
                   'p': ('q1', 'x'), 'q': ('q1', 'x'), 'r': ('q1', 'x'), 's': ('q1', 'x'), 't': ('q1', 'x'),
                   'u': ('q1', 'x'), 'v': ('q1', 'x'), 'w': ('q1', 'x'), 'x': ('q1', 'x'), 'y': ('q1', 'x'),
                   'z': ('q1', 'x'), '+': ('q2', '+'), '(': ('q2', '('), ')': ('q2', ')'), ' ': ('q2', '')
                   },
            'q1': {'a': ('q1', 'x'), 'b': ('q1', 'x'), 'c': ('q1', 'x'), 'd': ('q1', 'x'), 'e': ('q1', 'x'),
                   'f': ('q1', 'x'), 'g': ('q1', 'x'), 'h': ('q1', 'x'), 'i': ('q1', 'x'), 'j': ('q1', 'x'),
                   'k': ('q1', 'x'), 'l': ('q1', 'x'), 'm': ('q1', 'x'), 'n': ('q1', 'x'), 'o': ('q1', 'x'),
                   'p': ('q1', 'x'), 'q': ('q1', 'x'), 'r': ('q1', 'x'), 's': ('q1', 'x'), 't': ('q1', 'x'),
                   'u': ('q1', 'x'), 'v': ('q1', 'x'), 'w': ('q1', 'x'), 'x': ('q1', 'x'), 'y': ('q1', 'x'),
                   'z': ('q1', 'x'), '+': ('q2', '+'), '(': ('q2', '('), ')': ('q2', ')'), ' ': ('q2', '')
                   },
            'q2': {'a': ('q1', 'x'), 'b': ('q1', 'x'), 'c': ('q1', 'x'), 'd': ('q1', 'x'), 'e': ('q1', 'x'),
                   'f': ('q1', 'x'), 'g': ('q1', 'x'), 'h': ('q1', 'x'), 'i': ('q1', 'x'), 'j': ('q1', 'x'),
                   'k': ('q1', 'x'), 'l': ('q1', 'x'), 'm': ('q1', 'x'), 'n': ('q1', 'x'), 'o': ('q1', 'x'),
                   'p': ('q1', 'x'), 'q': ('q1', 'x'), 'r': ('q1', 'x'), 's': ('q1', 'x'), 't': ('q1', 'x'),
                   'u': ('q1', 'x'), 'v': ('q1', 'x'), 'w': ('q1', 'x'), 'x': ('q1', 'x'), 'y': ('q1', 'x'),
                   'z': ('q1', 'x'), '+': ('q2', '+'), '(': ('q2', '('), ')': ('q2', ')'), ' ': ('q2', '')
                   }
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
                raise ValueError("<REJEITAR>" + simbolo)

        return cadeia_saida

# Exemplo de uso
transdutor = DFATransdutor()

cadeia_entrada_1 = 'abc+ (+) ab ()'
cadeia_saida_1 = transdutor.processar_entrada(cadeia_entrada_1)
print(cadeia_entrada_1, '->', cadeia_saida_1)

cadeia_entrada_2 = 'abc + (ab +  ) ab ()'
cadeia_saida_2 = transdutor.processar_entrada(cadeia_entrada_2)
print(cadeia_entrada_2, '->', cadeia_saida_2)

cadeia_entrada_3 = 'love + (hate + something)'
cadeia_saida_3 = transdutor.processar_entrada(cadeia_entrada_3)
print(cadeia_entrada_3, '->', cadeia_saida_3)

cadeia_entrada_4 = 'abc123'
cadeia_saida_4 = transdutor.processar_entrada(cadeia_entrada_4)
print(cadeia_entrada_4, '->', cadeia_saida_4)
