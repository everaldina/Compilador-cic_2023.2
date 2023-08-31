import pandas as pd
import gerar_tabela as gt



# lista com palavras reservadas da linguagem
reserv = ["programa", "fim_programa", "se", "entao", "imprima", "leia", "enquanto"]

def prox_estado(estado_atual, char):
    return tabela_transicao.at[estado_atual, char]

def gerar_tbl_simb():
    cols = ['linha', 'coluna', 'lexema', 'token']
    tbl_simb = pd.DataFrame(columns=cols)
    return tbl_simb

def scanner(nome_arq):
    tbl_transicao, estados_acc = gt.gerar_tabela()
    tbl_simbolos = gerar_tbl_simb()
    count_linha = 1
    posicao = 0
    
    while(1):
        estado_atual = 'q0'
        lexema = ''
        if(token != 'TK_COMENTARIO'):
            add_token(tbl_simbolos, linha, coluna, lexema, token)
    return tbl_simbolos

def add_token(tabela, linha, coluna, lexema, token):
    distintos = ["TK_ID", "TK_NUMERO", "TK_CADEIA", "TK_MOEDA"]
    if(token in distintos):
        tabela.loc[len(tabela)] = [linha, coluna, lexema, token]
    else:
        tabela.loc[len(tabela)] = [linha, coluna, None , token]
    return tabela
