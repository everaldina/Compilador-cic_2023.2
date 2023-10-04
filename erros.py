
ERR_CADEIA = ["q1"]
ERR_NUM_FORMAT = ["q9"]
ERR_FLOAT_FORMAT = ["q13", "q14"]
ERR_CIEN_FORMAT = ["q10", "q11", "q12"]
ERR_ID_FORMAT = ["q24"]
ERR_NAO_RESERV = ["q2", "q3", "TK_RESERVADA"]
ERR_MOEDA_FORMAT = ["q6", "q7", "q8"]
ERR_NAO_OPER = ["q15", "q16", "q4"]
ERR_COMENT_FORMAT = ["q18", "q19"]

disc_mensagem = {"ERR_CADEIA_FORMAT": "Cadeia mal formatada.",
                 "ERR_NUM_FORMAT": "Número mal formatado.", 
                 "ERR_FLOAT_FORMAT": "Número flaot mal formatado.",
                 "ERR_CIEN_FORMAT": "Número cientifico mal formatado.",
                 "ERR_ID_FORMAT": "ID mal formatado.",
                 "ERR_NAO_RESERV": "Palavra não reservada.",
                 "ERR_MOEDA_FORMAT": "Moeda mal formatada.",
                 "ERR_NAO_OPER": "Não é um operador reconhecido.",
                 "ERR_COMENT_FORMAT": "Comentário mal formatado.",
                 "ERR_LEXICO": "Erro léxico."}



def get_erro(estado_att, char):
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
    elif estado_att in ERR_NAO_OPER or not char.isalnum():
        return disc_mensagem["ERR_NAO_OPER"]
    elif estado_att in ERR_COMENT_FORMAT:
        return disc_mensagem["ERR_COMENT_FORMAT"]
    else:
        return disc_mensagem["ERR_LEXICO"]