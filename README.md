# Compilador-cic_2023.2
Um projeto para diciplina de Compiladores que trabalha com a linguagem ficticia cic_2023.2

## Como usar
Um arquivo de entrada da linguagem cic_2023.2 (extensao .cic) deve ser posto na pasta /testes e na main do arquivo main.py deve ser alterado a linha 99 para `arquivo_nome = "nome_do_arquivo`.
## Linguagem

### Tipos de dados
A linguagem cic_2023.2 possui os seguintes tipos de dados:
 * Número: Em formato hexadecimal (digitos [0-9][A-F]), podendo ser um um inteiro (num) ou um float (num.num). Os números podem ainda ter seu formato em notação cientifica (numenum, nume-num, num.numenum, num.nume-num). Os números não tem sinal exceto no sinal do expoente da notação cientifica.
      * Ex: -15, A1, A3e9, D.25Fe-9D.
      * Não são números: ., a1, 234.5ee3, .324, 234., D.25Fe-9.D.
 * Moeda: As moedas são formadas por uma letra maiuscula [A-Z] seguida de um $ e um número (em sistema decimal) flutuante, tendo obrigatoriamente 2 casas decimais.
      * Ex: R$21314.00, U$2.90, A$2.99.
      * Não são moedas: R$21314.0000, U$2.9, A$2. $13, R$12.
 * Cadeia: Cadeias de caracteres, formadas por uma sequência de caracteres entre aspas duplas ("), podendo conter qualquer caractere, exceto aspas duplas e quebras de linha. A cadeia pode ser vazia.
      * Ex: "-15", "cic 2023\n", "".
 * Identificadores: Identificadores de variaveis são formados por uma sequência de letras minúsculas e dígitos, dentro dos limitadores: <>. Um identificador deve ter ao menos 1 letra e não deve começar com dígito.
      * Ex: *<*var1*>*, *<*a*>*, *<*a8a8a8*>*
      * Não sao numeros: a, <1var>, <1>

### Operadores
A linguagem cic_2023.2 possui os seguintes operadores:
* Operadores aritiméticos e lógicos: -, ~, +, *, /, &, |, 
* Operadores relacionais: !=, =, >=, <=, >, <
* Operadores de atribuição: := 
### Comentarios
Comentários podem ser feitos de duas formas:
* Comentário de linha: Inicia com o caractere # e vai até o final da linha.
    * Ex: # Isso é um comentário de linha.
* Comentário de bloco: Inicia com três aspas simples (''') e termina com três aspas simples. Comentários de bloco podem ter mais de uma linha.
    * Ex: ''' Isso é um comentário de bloco. '''
### Delimitadores
Os delimitadores da linguagem são:
* Virgula ","
* Abre parentese "("
* Fecha parentese ")" 
### Palavras reservadas
Lista de palavras reservadas da linguagem são:
* programa
* fim_programa
* se
* entao
* imprima
* leia
* enquanto

## Automato
O automato completo para a linguagem cic_2023.2.
![automato completo](https://github.com/everaldina/Compilador-cic_2023.2/blob/main/automato/AFD_completo.png?raw=true)
* **Σ =** todos os caracteres possíveis de um arquivo de texto.
* _num_ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
* _letra_ = {a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z}

* _outro¹_ = Σ - {A, B, C, D, E, F, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

* _outro²_ = outro¹ - {e}

* _outro³_ = outro² - {., $}

* _outro⁴_ = Σ - {>, =}

* _outro⁵_ = Σ - {letra, _}

* _outro⁶_ = Σ - {'}

* _outro⁷_ = Σ - {\n}

* _outro⁸_ = Σ - {letra, =}

* _outro⁹_ = outro⁷ - {"}


## Tokens
A seguir a tabela com os tokens da linguagem e suas respectivas expressões regulares.
Tokens   | Expressão Regular
:--------- | :------ 
TK_ID | <[a-z]([a-z] &#124; [0-9])*>
TK_NUMERO | ([A-F] &#124; [0-9])+(.([A-F] &#124; [0-9])+)?(e-?([A-F] &#124; [0-9])+)? 
TK_MOEDA | [A-Z]$[0-9]+.[0-9][0-9]
TK_CADEIA | "(outro⁹)*"
TK_RESERVADA | ( programa &#124; fim_programa &#124; se &#124; entao &#124; imprima &#124; leia &#124; enquanto)
TK_COMENTARIO | (#(outro⁷)*\n) &#124; ('''(('Σ)*(outro⁶)*)*''')
TK_OP_GE | >=
TK_OP_LE | <=
TK_OP_MAIOR | >
TK_OP_MENOR | <
TK_OP_IGUAL | =
TK_OP_DIF | !=
TK_OP_SOMA | +
TK_OP_SUB | -
TK_OP_MULT | *
TK_OP_DIV | /
TK_OP_OU | &#124;
TK_OP_E | &
TK_OP_NEGACAO | ~
TK_OP_ATRIBUICAO | :=
TK_ABRE_PARENTESE | (
TK_FECHA_PARENTESE | )
TK_VIRGULA | ,

### Automato TK_ID
![automato id](https://github.com/everaldina/Compilador-cic_2023.2/blob/main/automato/TK_ID.png?raw=true)
### TK_NUMERO
![automato id](https://github.com/everaldina/Compilador-cic_2023.2/blob/main/automato/TK_NUMERO.png?raw=true)
### TK_MOEDA
![automato id](https://github.com/everaldina/Compilador-cic_2023.2/blob/main/automato/TK_MOEDA.png?raw=true)
### TK_CADEIA
![automato id](https://github.com/everaldina/Compilador-cic_2023.2/blob/main/automato/TK_CADEIA.png?raw=true)
### TK_RESERVADA
![automato id](https://github.com/everaldina/Compilador-cic_2023.2/blob/main/automato/TK_RESERVADO.png?raw=true)
### TK_COMENTARIO
![automato id](https://github.com/everaldina/Compilador-cic_2023.2/blob/main/automato/TK_COMENTARIO.png?raw=true)
### TK_OP's
![automato id](https://github.com/everaldina/Compilador-cic_2023.2/blob/main/automato/TK_OPERACAO.png?raw=true)
### TD_DELIMITADORES
![automato id](https://github.com/everaldina/Compilador-cic_2023.2/blob/main/automato/TK_DELIMITADOR.png?raw=true)