import pandas as pd
import gerar_tabela as gt


def gerar_tbl_simb():
    cols = ['posicao', 'linha', 'coluna', 'lexema', 'token']
    tbl_simb = pd.DataFrame(columns=cols)
    return tbl_simb

def att_cursor(cursor, char, retroceder=False):
    if(not retroceder):
        cursor["posicao"] += 1
        if(char != '\n'):
            cursor["coluna"] +=1
        else:
            cursor["coluna"] = 1
            cursor["linha"] += 1
    return cursor

def scanner(nome_arq):
    tbl_transicao, estados_acc = gt.gerar_tabela()
    tbl_simbolos = gerar_tbl_simb()
    cursor = {"posicao": 0, "linha": 1, "coluna": 1}
    
    arquivo = open(nome_arq, 'r')
    
    while(1):
        token, lexema, nova_posicao = get_token(arquivo, cursor, tbl_transicao, estados_acc)
        if(token == 'EOF'):
            break
        if(token != 'TK_COMENTARIO' and token != None):
            add_token(tbl_simbolos, cursor, lexema, token)
        cursor = nova_posicao
    arquivo.close()
    return tbl_simbolos

def add_token(tabela, posicao, lexema, token):
    distintos = ["TK_ID", "TK_NUMERO", "TK_CADEIA", "TK_MOEDA"]
    if(token in distintos):
        tabela.loc[len(tabela)] = [posicao["posicao"], posicao["linha"], posicao["coluna"], lexema, token]
    else:
        tabela.loc[len(tabela)] = [posicao["posicao"], posicao["linha"], posicao["coluna"], None , token]
    return tabela

def get_token(arquivo, posicao, tbl_transicao, estados_acc):
    lexema = ''
    estado_att = 'q0'
    # em casos que você precisa retroceder o arquivo por causa da regra da maior cadeia
    lista_retroceder = ["TK_NUMERO", "TK_RESERVADA", "TK_OP_MAIOR", "TK_OP_MENOR"]
    dic_rsv = {"programa": "TK_PROG", "fim_programa": "TK_FPROG", "se": "TK_SE", 
               "entao": "TK_ENTAO", "imprima": "TK_IMPRIMA", "leia": "TK_LEIA", "enquanto": "TK_ENQUANTO"}
    palavra_rsv = list(dic_rsv.keys())
    input = list(tbl_transicao.columns.values)
    input.remove('outro')
    
    while(1):
        char = arquivo.read(1)
        if not char:
            return 'EOF', None, None
        if char not in input:
            char = 'outro'
        estado_att = tbl_transicao.at[estado_att, char]
        if(estado_att != 'q0'):
            lexema = lexema + char
        posicao = att_cursor(posicao, char)
        if(estado_att == None):
            return estado_att, None, posicao
        if (estado_att in estados_acc) and (estado_att not in lista_retroceder):
            return estado_att, lexema, posicao
        elif (estado_att in estados_acc):
            lexema = lexema[:len(lexema)-1]
            posicao["posicao"]-=1
            if(char == '\n'):
                posicao["coluna"]=1
                posicao["linha"]-=1
            else:
                posicao["coluna"]-=1
            arquivo.seek(posicao["posicao"]) #retroceder o arquivo
            if estado_att == 'TK_RESERVADA':
                if lexema in palavra_rsv:
                    return dic_rsv[lexema], lexema, posicao       
                else:
                    return None, None, posicao
            else:
                return estado_att, lexema, posicao
            
fim = scanner('ex1.cic')
fim.to_csv("v2.csv", sep=";", index=True, header=True)
print(fim)


    
