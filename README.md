- Erick Sartori 13381156
- João Pedro Viana Dubiela 13262572
- Vinicius Krieger Granemann 13416847

**Formal normal de Chomsky:**

Com base na tabela de transições fornecida anteriormente, aqui estão alguns exemplos de formatação para a tabela no arquivo README.md:
**Tabela de Origem**
S → (E)
S → x
E → S
E → E+S

Para S → (E) criamos as regras, 
A → ( 
B → ), logo S → AEB então,
C → EB então S → AB, e para
E → E + S, criamos as regras, 
F → +
D → FS, então E → ED por fim temos que a forma normal de Chomsky é a **Tabela Simples**

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
