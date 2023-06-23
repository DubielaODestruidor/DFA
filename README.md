- Erick Sartori 13381156
- João Pedro Viana Dubiela 13262572
- Vinicius Krieger Granemann 13416847

**Formal normal de Chomsky:**

Com base na tabela de transições fornecida anteriormente, aqui estão alguns exemplos de formatação para a tabela no arquivo README.md:

**Exemplo 1: Tabela Simples**

| Origem | Transição |
|:---: | :---:  |
| `S`    | `A,C`       |
| `A`      | `(`         |
| `C`     | `E,B`       |
| `B`      | `)`         |
| `S`      | `x`         |
| `E`      | `S`         |
| `E`      | `E,D`       |
| `D`      | `F,S`       |
| `F`      | `+`         |
