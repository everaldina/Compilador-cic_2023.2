import pandas as pd
import gerar_tabela as gt


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
        token, lexema, nova_posicao = get_token(arquivo, posicao, tbl_transicao, estados_acc)
        if(token == 'EOF'):
            break
        if(token != 'TK_COMENTARIO' and token != None):
            add_token(tbl_simbolos, posicao, lexema, token)
        posicao = nova_posicao
    arquivo.close()
    return tbl_simbolos

def add_token(tabela, posicao, lexema, token):
    distintos = ["TK_ID", "TK_NUMERO", "TK_CADEIA", "TK_MOEDA"]
    if(token in distintos):
        tabela.loc[len(tabela)] = [posicao, None, None, lexema, token]
    else:
        tabela.loc[len(tabela)] = [posicao, None, None, None , token]
    return tabela

def get_token(arquivo, posicao, tbl_transicao, estados_acc):
    lexema = ''
    estado_att = 'q0'
    # em casos que você precisa retroceder o arquivo por causa da regra da maior cadeia
    lista_retroceder = ["TK_NUMERO", "TK_RESERVADO", "TK_OP_MAIOR", "TK_OP_MENOR"]
    dic_rsv = {"programa": "TK_PROG", "fim_programa": "TK_FPROG", "se": "TK_SE", 
               "entao": "TK_ENTAO", "imprima": "TK_IMPRIMA", "leia": "TK_LEIA", "enquanto": "TK_ENQUANTO"}
    palavra_rsv = list(dic_rsv.keys())
    
    while(1):
        char = arquivo.read(1)
        if not char:
            return 'EOF', None, None
        estado_att = tbl_transicao.at[estado_att, char]
        lexema.append(char)
        posicao+=1
        if (estado_att in estados_acc) and (estado_att not in lista_retroceder):
            return estado_att, lexema, posicao
        elif (estado_att in estados_acc) and (estado_att in lista_retroceder):
            lexema.pop()
            posicao-=1
            arquivo.seek(-1, 1) #retroceder o arquivo
            if estado_att == 'TK_RESERVADO':
                if lexema in palavra_rsv:
                    return dic_rsv[lexema], lexema, posicao       
                else:
                    return None, lexema, posicao
            else:
                return estado_att, lexema, posicao


    
