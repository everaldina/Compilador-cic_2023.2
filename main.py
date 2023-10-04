import scanner
import pandas as pd

def main(nome_arquivo):
    tbl_simbolos, tbl_erros, cursor = scanner.scanner(nome_arquivo)
    count_linha = cursor["linha"]
    #saida_token(tbl_simbolos, count_linha, "saida_token.txt")
    saida_count_token(tbl_simbolos, "saida_count_token.txt")

def saida_count_token(tbl_simbolos, nome_saida):
    tokens_count = tbl_simbolos['token'].value_counts()
    with open(nome_saida, 'w') as arq:
        arq.write("+----------------------------------+\n")
        arq.write("|          Tabela de Tokens        |\n")
        arq.write("+----------------------------------+\n")
        arq.write("| Token".ljust(22))
        arq.write("| Quantidade ".ljust(10))
        arq.write("|\n")
        arq.write("+----------------------------------+\n")
        for i in range(len(tokens_count)):
            arq.write("| " + tokens_count.index[i].ljust(20))
            arq.write("| " + str(tokens_count[i]).ljust(11))
            arq.write("|\n")
        arq.write("+----------------------------------+\n")
    

def saida_token(tbl_simbolos, linhas, nome_saida):
    dg_linha = len(str(linhas))
    with open(nome_saida, 'w') as arq:
        arq.write("Tabela de Tokens\n")
        arq.write("Linha\tColuna\tToken\tLexema\n")
        
main("ex1.cic")