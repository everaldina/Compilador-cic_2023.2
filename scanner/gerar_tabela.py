import pandas as pd



def gerar_estados():
    ### iniciando lista com estados
    #tokens
    estados = ["TK_ID", "TK_NUMERO", "TK_MOEDA", "TK_CADEIA", "TK_RESERVADA",
            "TK_COMENTARIO", "TK_OP_GE", "TK_OP_LE", "TK_OP_MAIOR", 
            "TK_OP_MENOR", "TK_OP_IGUAL", "TK_OP_DIF",
            "TK_OP_SOMA", "TK_OP_SUB", "TK_OP_MULT", "TK_OP_DIV",
            "TK_OP_OU", "TK_OP_E", "TK_OP_NEGACAO", "TK_OP_ATRIBUICAO",
            "TK_ABRE_PARENTESE", "TK_FECHA_PARENTESE", "TK_VIRGULA"]
    estados_acc = estados.copy()
    #estados
    for x in range (0,26):
        estados.append('q'+ str(x))
    return [estados, estados_acc]

def gerar_inputs():
    inputs = []
    for x in range(ord('A'), ord('Z')+1):
        inputs.append(chr(x))
    for x in range(ord('a'), ord('z')+1):
        inputs.append(chr(x))
    for x in range(0, 10):
        inputs.append(str(x))
    inputs.extend(["(", ")", ",", "+", "-", "*", "/", ">", "<", "=", "!", "_",
                " ", "\n", "\t", "$", '"', "'", ".", ":", '~', '|', "&", "#",
                "outro"])
    return inputs


def criar_tabela(inputs, estados):
    data = [[None] * len(inputs) for _ in range(len(estados))]
    tabela_transicao = pd.DataFrame(data, index=estados, columns=inputs)
    return tabela_transicao


def preencher_tabela(tabela_transicao):
    #q0
    tabela_transicao.at['q0', '\t'] = 'q0'
    tabela_transicao.at['q0', '\n'] = 'q0'
    tabela_transicao.at['q0', ' '] = 'q0'
    tabela_transicao.at["q0", '"']= 'q1'
    tabela_transicao.loc["q0", "a": "z"]= 'q2'
    tabela_transicao.loc["q0", 'A':'F']= 'q10'
    tabela_transicao.loc["q0", 'G':'Z']= 'q5'
    tabela_transicao.loc["q0", '0':'9']= 'q10'
    tabela_transicao.at["q0", '|']= 'TK_OP_OU'
    tabela_transicao.at["q0", '&']= 'TK_OP_E'
    tabela_transicao.at["q0", '~']= 'TK_OP_NEGACAO'
    tabela_transicao.at["q0", '(']= 'TK_ABRE_PARENTESE'
    tabela_transicao.at["q0", ')']= 'TK_FECHA_PARENTESE'
    tabela_transicao.at["q0", ',']= 'TK_VIRGULA'
    tabela_transicao.at["q0", '+']= 'TK_OP_SOMA'
    tabela_transicao.at["q0", '-']= 'TK_OP_SUB'
    tabela_transicao.at["q0", '*']= 'TK_OP_MULT'
    tabela_transicao.at["q0", '/']= 'TK_OP_DIV'
    tabela_transicao.at["q0", '=']= 'TK_OP_IGUAL'
    tabela_transicao.at["q0", ':']= 'q16'
    tabela_transicao.at["q0", '!']= 'q17'
    tabela_transicao.at["q0", '<']= 'q24'
    tabela_transicao.at["q0", '>']= 'q4'
    tabela_transicao.at["q0", '#']= 'q23'
    tabela_transicao.at["q0", "'"]= 'q18'
    #q1
    tabela_transicao.loc["q1", :]= 'q1'
    tabela_transicao.at["q1", '"']= 'TK_CADEIA'
    tabela_transicao.at["q1", '\n']= None
    #q2
    tabela_transicao.loc["q2", 'a':'z']= 'q3'
    #q3
    tabela_transicao.loc["q3", 'A':'Z']= 'TK_RESERVADA'
    tabela_transicao.loc["q3", 'a':'z']= 'q3'
    tabela_transicao.loc["q3", '0':'outro']= 'TK_RESERVADA'
    tabela_transicao.at["q3", '_']= 'q3'
    #q4
    tabela_transicao.loc["q4", :]= 'TK_OP_MAIOR'
    tabela_transicao.at["q4", '=']= 'TK_OP_GE'
    #q5
    tabela_transicao.at["q5", '$']= 'q6'
    #q6
    tabela_transicao.loc["q6", '0':'9']= 'q7'
    #q7
    tabela_transicao.loc["q7", '0':'9']= 'q7'
    tabela_transicao.at["q7", '.']= 'q8'
    #q8
    tabela_transicao.loc["q8", '0':'9']= 'q9'
    #q9
    tabela_transicao.loc["q9", '0':'9']= 'TK_MOEDA'
    #q10
    tabela_transicao.loc["q10", '0':'9']= 'q10'
    tabela_transicao.loc["q10", 'A':'F']= 'q10'
    tabela_transicao.loc["q10", 'G':'d']= 'TK_NUMERO'
    tabela_transicao.at["q10", 'e']= 'q11'
    tabela_transicao.loc["q10", 'f':'z']= 'TK_NUMERO'
    tabela_transicao.loc["q10", '(':]= 'TK_NUMERO'
    tabela_transicao.at["q10", '$']= 'q6'
    tabela_transicao.at["q10", '.']= 'q14'
    #q11
    tabela_transicao.loc["q11", '0':'9']= 'q13'
    tabela_transicao.loc["q11", 'A':'F']= 'q13'
    tabela_transicao.at["q11", '-']= 'q12'
    #q12
    tabela_transicao.loc["q12", '0':'9']= 'q13'
    tabela_transicao.loc["q12", 'A':'F']= 'q13'
    #q13
    tabela_transicao.loc["q13", '0':'9']= 'q13'
    tabela_transicao.loc["q13", 'A':'F']= 'q13'
    tabela_transicao.loc["q13", 'G':'z']= 'TK_NUMERO'
    tabela_transicao.loc["q13", '(':]= 'TK_NUMERO'
    #q14
    tabela_transicao.loc["q14", '0':'9']= 'q15'
    tabela_transicao.loc["q14", 'A':'F']= 'q15'
    #q15
    tabela_transicao.loc["q15", '0':'9']= 'q15'
    tabela_transicao.loc["q15", 'A':'F']= 'q15'
    tabela_transicao.loc["q15", 'G':'z']= 'TK_NUMERO'
    tabela_transicao.loc["q15", '(':]= 'TK_NUMERO'
    tabela_transicao.at["q15", 'e']= 'q11'
    #q16
    tabela_transicao.at["q16", '='] = "TK_OP_ATRIBUICAO"
    #q17
    tabela_transicao.at["q17", '='] = "TK_OP_DIF"
    #q18
    tabela_transicao.at["q18", "'"] = "q19"
    #q19
    tabela_transicao.at["q19", "'"] = "q20"
    #q20
    tabela_transicao.loc["q20", :] = "q20"
    tabela_transicao.at["q20", "'"] = "q21"
    #q21
    tabela_transicao.loc["q21", :] = "q20"
    tabela_transicao.at["q21", "'"] = "q22"
    #q22
    tabela_transicao.loc["q22", :] = "q20"
    tabela_transicao.at["q22", "'"] = "TK_COMENTARIO"
    #q23
    tabela_transicao.loc["q23", :] = "q23"
    tabela_transicao.at["q23", "\n"] = "TK_COMENTARIO"
    #q24
    tabela_transicao.loc["q24", :] = "TK_OP_MENOR"
    tabela_transicao.loc["q24", 'a':'z'] = "q25"
    tabela_transicao.at["q24", '='] = "TK_OP_LE"
    #q25
    tabela_transicao.loc["q25", "a":"9"] = "q25"
    tabela_transicao.at["q25", ">"] = "TK_ID"

def gerar_csv(tabela):
    tabela.to_csv("tabela_transicao.csv", sep=";", index=True, header=True)

def gerar_tabela():
    estados, estados_acc = gerar_estados()
    inputs = gerar_inputs()
    tabela_transicao = criar_tabela(inputs, estados)
    preencher_tabela(tabela_transicao)
    gerar_csv(tabela_transicao)
    return tabela_transicao, estados_acc




