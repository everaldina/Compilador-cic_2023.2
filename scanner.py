import numpy as np
import pandas as pd


# lista com palavras reservadas da linguagem
reserv = ["programa", "fim_programa", "se", "entao", "imprima", "leia", "enquanto"]


### iniciando lista com estados
#tokens
estados = ["TK_ID", "TK_NUMERO", "TK_MOEDA", "TK_CADEIA", "TK_RESERVADA",
           "TK_COMENTARIO", "TK_OP_GE", "TK_OP_LE", "TK_OP_MAIOR", 
           "TK_OP_MENOR", "TK_OP_IGUAL", "TK_OP_DIF", "TK_OP_IGUAL",
           "TK_OP_SOMA", "TK_OP_SUB", "TK_OP_MULT", "TK_OP_DIV",
           "TK_OP_OU", "TK_OP_E", "TK_OP_NEGACAO", 
           "TK_ABRE_PARENTESE", "TK_FECHA_PARENTESE", "TK_VIRGULA"]
estados_acc = estados.copy()
#estados
for x in range (0,25):
    estados.append('q'+ str(x))
#rejeicao
estados.append("TK_REJEICAO")


inputs = []
for x in range(ord('A'), ord('Z')+1):
    inputs.append(chr(x))
for x in range(ord('a'), ord('z')+1):
    inputs.append(chr(x))
for x in range(0, 10):
    inputs.append(str(x))
inputs.extend(["(", ")", ",", "+", "-", "*", "/", ">", "<", "=", "!",
              " ", "\n", "\t", "$", '"', "'", ".", ":", '~', '|', "&", "#",
              "outro"])


padrao = "TK_REJEICAO"
data = [[padrao] * len(inputs) for _ in range(len(estados))]
tabela_transicao = pd.DataFrame(data, index=estados, columns=inputs)


#q0
tabela_transicao.at['q0', '\t'] = 'q0'
tabela_transicao.at['q0', '\n'] = 'q0'
tabela_transicao.at['q0', ' '] = 'q0'
tabela_transicao.loc["q0", '"']= 'q1'
tabela_transicao.loc["q0", "a": "z"]= 'q2'
tabela_transicao.loc["q0", 'A':'F']= 'q9'
tabela_transicao.loc["q0", 'G':'Z']= 'q5'
tabela_transicao.loc["q0", '0':'9']= 'q9'
tabela_transicao.loc["q0", '|']= 'TK_OP_OU'
tabela_transicao.loc["q0", '&']= 'TK_OP_E'
tabela_transicao.loc["q0", '~']= 'TK_OP_NEGACAO'
tabela_transicao.loc["q0", '(']= 'TK_ABRE_PARENTESE'
tabela_transicao.loc["q0", ')']= 'TK_FECHA_PARENTESE'
tabela_transicao.loc["q0", ',']= 'TK_VIRGULA'
tabela_transicao.loc["q0", '+']= 'TK_OP_SOMA'
tabela_transicao.loc["q0", '-']= 'TK_OP_SUB'
tabela_transicao.loc["q0", '*']= 'TK_OP_MULT'
tabela_transicao.loc["q0", '/']= 'TK_OP_DIV'
tabela_transicao.loc["q0", '=']= 'TK_OP_IGUAL'
tabela_transicao.loc["q0", ':']= 'q15'
tabela_transicao.loc["q0", '!']= 'q16'
tabela_transicao.loc["q0", '<']= 'q23'
tabela_transicao.loc["q0", '>']= 'q4'
tabela_transicao.loc["q0", '#']= 'q22'
tabela_transicao.loc["q0", "'"]= 'q17'


def prox_estado(estado_atual, char):
    return tabela_transicao.at[estado_atual, char]













