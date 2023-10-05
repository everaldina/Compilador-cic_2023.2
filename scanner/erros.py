def get_erro(estado_att, char):
    ERR_CADEIA = ["q1"]
    ERR_NUM_FORMAT = ["q10"]
    ERR_FLOAT_FORMAT = ["q14", "q15"]
    ERR_CIEN_FORMAT = ["q11", "q12", "q13"]
    ERR_ID_FORMAT = ["q25"]
    ERR_NAO_RESERV = ["q2", "q3", "TK_RESERVADA"]
    ERR_MOEDA_FORMAT = ["q6", "q7", "q8", "q9"]
    ERR_NAO_OPER = ["q16", "q17"]
    ERR_COMENT_FORMAT = ["q18", "q19"]
    ERR_COMENT_ABERTO = ["q20", "q21", "q22"]

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
    estados_erro = ["q20", "q21", "q22"]
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