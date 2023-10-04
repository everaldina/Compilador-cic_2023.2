import pandas as pd
import gerar_tabela as gt
import erros

def gerar_tbl_simb():
    cols = ['posicao', 'linha', 'coluna', 'lexema', 'token']
    tbl_simb = pd.DataFrame(columns=cols)
    return tbl_simb

def gerar_tbl_erro():
    cols = ['posicao', 'linha', 'coluna', 'mensagem']
    tbl_erro = pd.DataFrame(columns=cols)
    return tbl_erro

def att_cursor(cursor, char):
    cursor["posicao"] += 1
    if(char != '\n'):
        cursor["coluna"] +=1
    else:
        cursor["coluna"] = 1
        cursor["linha"] += 1

def scanner(nome_arq):
    tbl_transicao, estados_acc = gt.gerar_tabela()
    tbl_simbolos = gerar_tbl_simb()
    cursor = {"posicao": 0, "linha": 1, "coluna": 1}
    tbl_erros = gerar_tbl_erro()
    
    arquivo = open(nome_arq, 'r')
    
    while(1):
        old_cursor = cursor.copy()
        token, lexema, char = get_token(arquivo, cursor, tbl_transicao, estados_acc)
        if(token == 'EOF'):
            break
        elif(token == None):
            mensagem_erro = erros.get_erro(lexema, char)
            add_erro(tbl_erros, old_cursor, mensagem_erro)
        elif(token != 'TK_COMENTARIO' and token != None and token != 'q0'):
            add_token(tbl_simbolos, old_cursor, lexema, token)
    arquivo.close()
    return tbl_simbolos, tbl_erros, cursor

def add_token(tabela, posicao, lexema, token):
    distintos = ["TK_ID", "TK_NUMERO", "TK_CADEIA", "TK_MOEDA"]
    if(token in distintos):
        tabela.loc[len(tabela)] = [posicao["posicao"], posicao["linha"], posicao["coluna"], lexema, token]
    else:
        tabela.loc[len(tabela)] = [posicao["posicao"], posicao["linha"], posicao["coluna"], None , token]

# def add_erro(tabela, posicao, mensagem):
def add_erro(tabela, posicao, mensagem):
    tabela.loc[len(tabela)] = [posicao["posicao"], posicao["linha"], posicao["coluna"], mensagem]

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
            return 'EOF', estado_att, None
        if char not in input:
            char = 'outro'
                    
        aux = tbl_transicao.at[estado_att, char]

        if(aux not in lista_retroceder):
            att_cursor(posicao, char)

        if(aux == None):
            return None, estado_att, char
        
        estado_att = aux
        
        if(estado_att != 'q0'):
            lexema = lexema + char
        else:
            return estado_att,'q0', None
        
        if (estado_att in lista_retroceder):
            lexema = lexema[:len(lexema)-1]
            arquivo.seek(posicao["posicao"]) #retroceder o arquivo
            if estado_att == 'TK_RESERVADA':
                if lexema in palavra_rsv:
                    return dic_rsv[lexema], lexema, None   
                else:
                    return None, 'q3', char
            else:
                return estado_att, lexema, None
        elif estado_att in estados_acc:
            return estado_att, lexema, None
            
#tbl_tokens, tbl_erro = scanner("ex2.cic")
#tbl_tokens.to_csv("tokens3.csv", sep=";", index=True, header=True)
#tbl_erro.to_csv("erros3.csv", sep=";", index=True, header=True)
#print(tbl_tokens)
#print(tbl_erro)


    
