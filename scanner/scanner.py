import pandas as pd
import gerar_tabela as gt
import erros

# gera tabela de tokens
def gerar_tbl_simb():
    cols = ['posicao', 'linha', 'coluna', 'lexema', 'token']
    tbl_simb = pd.DataFrame(columns=cols)
    return tbl_simb

# gera tabela para os erros
def gerar_tbl_erro():
    cols = ['posicao', 'linha', 'coluna', 'mensagem']
    tbl_erro = pd.DataFrame(columns=cols)
    return tbl_erro

# atualiza o cursor do arquivo
def att_cursor(cursor, char):
    # adiciona uma posicao
    cursor["posicao"] += 1

    if(char != '\n'): # adiciona uma coluna
        cursor["coluna"] +=1
    else: # caso caractere lido seja \n a linha é adicionda de a coluna volta a 1
        cursor["coluna"] = 1
        cursor["linha"] += 1
        


def scanner(nome_arq):
    tbl_transicao, estados_acc = gt.gerar_tabela() # recebe tabela de transicao e estados de aceitaçã
    tbl_simbolos = gerar_tbl_simb()
    cursor = {"posicao": 0, "linha": 1, "coluna": 1}
    tbl_erros = gerar_tbl_erro()
    
    arquivo = open(nome_arq, 'r')
    
    while(1):
        old_cursor = cursor.copy() # a cada rodada do loop o cursor é atualizado

        # recebe proximo token
        token, lexema, char = get_token(arquivo, cursor, tbl_transicao, estados_acc)

        # se final do arquivo for encontrado e nao houveram comentarios nao fechados
        if(token == 'EOF' and not erros.check_erro_coment(lexema)):
            break
        # caso encontrado comentario nao fechdado
        elif(token == 'EOF'):
            # recebe mensagem de erro e adiciona a tabela de erros
            mensagem_erro = erros.get_erro(lexema, char) 
            add_erro(tbl_erros, old_cursor, mensagem_erro)

            # trata o erro e atualiza o cursor
            erros.trat_erro_coment(arquivo, old_cursor)
            cursor = old_cursor.copy()
        # caso encontrado um estado de rejeicao
        elif(token == None):
            # recebe mensagem de erro e adiciona a tabela de erros
            mensagem_erro = erros.get_erro(lexema, char)
            add_erro(tbl_erros, old_cursor, mensagem_erro)
        elif(token != 'TK_COMENTARIO' and token != None and token != 'q0'):
            # adiciona token a tabela de tokens
            add_token(tbl_simbolos, old_cursor, lexema, token)
    arquivo.close()
    return tbl_simbolos, tbl_erros, cursor

# adiciona token a tabela de token
def add_token(tabela, posicao, lexema, token):
    distintos = ["TK_ID", "TK_NUMERO", "TK_CADEIA", "TK_MOEDA"]

    # se o token nao tem lexema distinto o lexema é adicionado como None
    if(token in distintos):
        tabela.loc[len(tabela)] = [posicao["posicao"], posicao["linha"], posicao["coluna"], lexema, token]
    else:
        tabela.loc[len(tabela)] = [posicao["posicao"], posicao["linha"], posicao["coluna"], None , token]

# adciciona erro a tabela de erros
def add_erro(tabela, posicao, mensagem):
    tabela.loc[len(tabela)] = [posicao["posicao"], posicao["linha"], posicao["coluna"], mensagem]

# retorna estado, lexema, char
# estado == None se for encontrado um erro
# lexema == estado anterior caso seja encontrado um erro
def get_token(arquivo, posicao, tbl_transicao, estados_acc):
    lexema = ''
    estado_att = 'q0'

    # em casos que você precisa retroceder o arquivo por causa da regra da maior cadeia
    lista_retroceder = ["TK_NUMERO", "TK_RESERVADA", "TK_OP_MAIOR", "TK_OP_MENOR"]

    # dicionario para palavras reservadas
    dic_rsv = {"programa": "TK_PROG", "fim_programa": "TK_FPROG", "se": "TK_SE", 
               "entao": "TK_ENTAO", "imprima": "TK_IMPRIMA", "leia": "TK_LEIA", "enquanto": "TK_ENQUANTO"}
    palavra_rsv = list(dic_rsv.keys())
    input = list(tbl_transicao.columns.values)
    input.remove('outro')
    
    while(1):
        # le um char do arquivo
        char = arquivo.read(1)
        if not char:
            # estado anterior é retornado para que o erro de comentario aberto seja tratado
            return 'EOF', estado_att, None
        if char not in input:
            # se o char nao estiver na tabela de transição ele recebe label 'outro'
            char = 'outro'
        
        # rescebe proximo estado
        aux = tbl_transicao.at[estado_att, char]

        # atualiza o cursor caso nao esteja na lista de retroceder
        if(aux not in lista_retroceder):
            att_cursor(posicao, char)

        # caso estado seja de rejeicao
        if(aux == None):
            return None, estado_att, char
        
        estado_att = aux
        
        # append letra no lexema caso nao seja um estado inicial
        if(estado_att != 'q0'):
            lexema = lexema + char
        else:
            return estado_att,'q0', None
        
        if (estado_att in lista_retroceder):
            # retira ultima letra do lexema
            lexema = lexema[:len(lexema)-1]
            arquivo.seek(posicao["posicao"]) #retroceder o arquivo

            # caso o token seja TK_RESERVADA verifica se lexema esta na lista de palavras reservadas
            if estado_att == 'TK_RESERVADA':
                if lexema in palavra_rsv:
                    return dic_rsv[lexema], lexema, None   
                else: # nao esta na lista de palavras reservadas
                    return None, 'q3', char
            else:
                return estado_att, lexema, None
        elif estado_att in estados_acc:
            return estado_att, lexema, None


    
