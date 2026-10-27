# Python | Exercícios do Curso em Vídeo

Minhas resoluções dos exercícios de Python do [Curso em Vídeo](https://www.cursoemvideo.com/), do professor Gustavo Guanabara. São **104 scripts**, dos primeiros comandos até funções com parâmetros e validação de entrada.

Guardei também algumas soluções alternativas e comparações com as apresentadas nas aulas. O repositório registra esse aprendizado, incluindo pontos que ainda podem ser corrigidos.

## Encontre um assunto

| Exercícios | Conteúdo |
| --- | --- |
| 001–035 | Entrada e saída, números, strings, módulos e condições |
| 036–045 | Condições compostas e encadeadas |
| 046–056 | Repetições com `for`, contagens e análise de valores |
| 057–071 | Repetições com `while`, menus e interrupção de laços |
| 072–077 | Tuplas |
| 078–089 | Listas, listas compostas e matrizes |
| 090–095 | Dicionários e cadastros |
| 096–104 | Funções, parâmetros, documentação e leitura de inteiros |

O [índice completo](docs/INDICE.md) tem um link para cada arquivo.

## Executar um exercício

Use Python 3. Os programas são independentes e, em geral, pedem os dados pelo terminal.

```powershell
git clone https://github.com/WmsTech/CursoEmVideo-Python.git
cd CursoEmVideo-Python
python Exercicios/ex003.py
```

Nesse exemplo, informe dois números inteiros para ver a soma:

```text
Digite um numero: 7
Digite outro numero: 5
A soma entre 7 e 5 é 12
```

O exercício 021 é uma exceção: usa `pygame` para reproduzir `ex021.mp3`. Instale a biblioteca em seu ambiente e execute a partir da pasta `Exercicios`, onde está o áudio:

```powershell
python -m pip install pygame
cd Exercicios
python ex021.py
```

## Para começar a leitura

- [Palíndromos](Exercicios/ex053.py): tratamento de texto e comparação com a string invertida.
- [Matriz 3 × 3](Exercicios/ex086.py): leitura e apresentação de uma lista de listas.
- [Cadastro de pessoas](Exercicios/ex094.py): listas de dicionários e resumo dos dados.
- [Fatorial com parâmetro opcional](Exercicios/ex102.py): cálculo com ou sem exibição das etapas.

Os scripts preservam as versões de estudo. Há correções pendentes, como a conversão para Kelvin em `ex014.py` e um `-print(...)` em `EX095.py`, que interrompe esse exercício. Os exemplos não devem ser usados como calculadoras profissionais ou referência de regras atuais.

Resoluções de Washington Marinho dos Santos. A proposta dos exercícios e as soluções identificadas como do professor vêm do Curso em Vídeo. O código está sob a [licença MIT](LICENSE).
