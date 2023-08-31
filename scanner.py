import pandas as pd
import gerar_tabela as gt



# lista com palavras reservadas da linguagem
reserv = ["programa", "fim_programa", "se", "entao", "imprima", "leia", "enquanto"]

def prox_estado(estado_atual, char):
    return tabela_transicao.at[estado_atual, char]

def gerar_tbl_simb():
    cols = ['posicao', 'linha', 'coluna', 'lexema', 'token']
    tbl_simb = pd.DataFrame(columns=cols)
    return tbl_simb

def scanner(nome_arq):
    tbl_transicao, estados_acc = gt.gerar_tabela()
    tbl_simbolos = gerar_tbl_simb()
    posicao = 0
    
    arquivo = open(nome_arq, 'r')
    
    while(1):
        lexema = ''
        token, lexema, posicao = get_token(arquivo, posicao, tbl_transicao, estados_acc)
        if(token == 'EOF'):
            break
        if(token != 'TK_COMENTARIO'):
            add_token(tbl_simbolos, posicao, lexema, token)
    arquivo.close()
    return tbl_simbolos

def add_token(tabela, posicao, lexema, token):
    distintos = ["TK_ID", "TK_NUMERO", "TK_CADEIA", "TK_MOEDA"]
    if(token in distintos):
        tabela.loc[len(tabela)] = [posicao, None, None, lexema, token]
    else:
        tabela.loc[len(tabela)] = [posicao, None, None, None , token]
    return tabela

    
