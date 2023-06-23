- Erick Sartori 13381156
- João Pedro Viana Dubiela 13262572
- Vinicius Krieger Granemann 13416847

**Formal normal de Chomsky:**

Com base na tabela de transições fornecida anteriormente, aqui estão alguns exemplos de formatação para a tabela no arquivo README.md:
**Tabela de Origem**
S → (E) \n 
S → x\n
E → S\n
E → E+S\n

Para S → (E) criamos as regras, \n
A → ( \n
B → ), logo S → AEB então,\n
C → EB então S → AB, e para\n
E → E + S, criamos as regras,\n 
F → +\n
D → FS, então E → ED por fim temos que a forma normal de Chomsky é a **Tabela Simples**\n

**Exemplo 1: Tabela Simples**

| Origem | Transição |
|:---: | :---:  |
| `S`    | `AC`       |
| `A`      | `(`         |
| `C`     | `EB`       |
| `B`      | `)`         |
| `S`      | `x`         |
| `E`      | `S`         |
| `E`      | `ED`       |
| `D`      | `FS`       |
| `F`      | `+`         |
