def get_erro(estado_att, char):
    ERR_CADEIA = ["q1"]
    ERR_NUM_FORMAT = ["q9"]
    ERR_FLOAT_FORMAT = ["q13", "q14"]
    ERR_CIEN_FORMAT = ["q10", "q11", "q12"]
    ERR_ID_FORMAT = ["q24"]
    ERR_NAO_RESERV = ["q2", "q3", "TK_RESERVADA"]
    ERR_MOEDA_FORMAT = ["q6", "q7", "q8"]
    ERR_NAO_OPER = ["q15", "q16", "q4"]
    ERR_COMENT_FORMAT = ["q18", "q19"]
    ERR_COMENT_ABERTO = ["q19", "q20", "q25", "q21"]

    disc_mensagem = {"ERR_CADEIA_FORMAT": "Cadeia mal formatada.",
                    "ERR_NUM_FORMAT": "Numero mal formatado.", 
                    "ERR_FLOAT_FORMAT": "Numero flaot mal formatado.",
                    "ERR_CIEN_FORMAT": "Numero cientifico mal formatado.",
                    "ERR_ID_FORMAT": "ID mal formatado.",
                    "ERR_NAO_RESERV": "Palavra nao reservada.",
                    "ERR_MOEDA_FORMAT": "Moeda mal formatada.",
                    "ERR_NAO_OPER": "Nao eh um operador reconhecido.",
                    "ERR_COMENT_FORMAT": "Comentario mal formatado.",
                    "ERR_COMENT_ABERTO": "Comentario nao fechado.",
                    "ERR_LEXICO": "Erro lexico."}

    if estado_att in ERR_CADEIA:
        return disc_mensagem["ERR_CADEIA_FORMAT"]
    elif estado_att in ERR_NUM_FORMAT:
        return disc_mensagem["ERR_NUM_FORMAT"]
    elif estado_att in ERR_FLOAT_FORMAT:
        return disc_mensagem["ERR_FLOAT_FORMAT"]
    elif estado_att in ERR_CIEN_FORMAT:
        return disc_mensagem["ERR_CIEN_FORMAT"]
    elif estado_att in ERR_ID_FORMAT:
        return disc_mensagem["ERR_ID_FORMAT"]
    elif estado_att in ERR_NAO_RESERV:
        return disc_mensagem["ERR_NAO_RESERV"]
    elif estado_att in ERR_MOEDA_FORMAT:
        return disc_mensagem["ERR_MOEDA_FORMAT"]
    elif char is not None and estado_att in ERR_NAO_OPER:
        if estado_att in ERR_NAO_OPER or not char.isalnum():
            return disc_mensagem["ERR_NAO_OPER"]
    elif estado_att in ERR_COMENT_FORMAT:
        return disc_mensagem["ERR_COMENT_FORMAT"]
    elif estado_att in ERR_COMENT_ABERTO:
        return disc_mensagem["ERR_COMENT_ABERTO"]
    else:
        return disc_mensagem["ERR_LEXICO"]

def check_erro_coment(estado_att):
    estados_erro = ["q19", "q20", "q25", "q21"]
    if estado_att in estados_erro:
        return True
    else:
        return False
    

def trat_erro_coment(arquivo, cursor):
    cursor["coluna"] = 1
    cursor["linha"] += 1
    
    arquivo.seek(cursor["posicao"])
    char = arquivo.read(1)
    cursor["posicao"] += 1
    while(char != '\n'):
        char = arquivo.read(1)
        cursor["posicao"] += 1
        
get_erro("q0", 'P')