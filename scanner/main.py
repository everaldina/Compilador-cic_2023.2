import scanner
import pandas as pd
import os

def main(nome_arquivo):
    tbl_simbolos, tbl_erros, cursor = scanner.scanner(nome_arquivo)
    count_linha = cursor["linha"]
    
    nome_token = nome_arquivo + "-" + "token.txt"
    nome_count_token = nome_arquivo + "-" + "count_token.txt"
    nome_codigo_fonte = nome_arquivo + "-" + "codigo_fonte.txt"
    
    saida_token(tbl_simbolos, nome_token)
    saida_count_token(tbl_simbolos, nome_count_token)
    saida_codigo_fonte(nome_arquivo, tbl_erros, count_linha, nome_codigo_fonte)

def saida_count_token(tbl_simbolos, nome_saida):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio_superior = os.path.dirname(diretorio_atual)
    caminho_arquivo = os.path.join(diretorio_superior, 'testes', nome_saida)
    
    
    tokens_count = tbl_simbolos['token'].value_counts()
    with open(caminho_arquivo, 'w') as arq:
        arq.write("+----------------------------------+\n")
        arq.write("|         Contagem de Tokens       |\n")
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
    

def saida_token(tbl_simbolos, nome_saida):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio_superior = os.path.dirname(diretorio_atual)
    caminho_arquivo = os.path.join(diretorio_superior, 'testes', nome_saida)
    
    with open(caminho_arquivo, 'w') as arq:
        arq.write("+-----------------------------------------------------------------------+\n")
        arq.write("|                            Tabela de Tokens                           |\n")
        arq.write("+-----------------------------------------------------------------------+\n")
        arq.write("| Linha".ljust(10))
        arq.write("| Coluna".ljust(10))
        arq.write("| Token".ljust(22))
        arq.write("| Lexema".ljust(30))
        arq.write("|\n")
        arq.write("+-----------------------------------------------------------------------+\n")
        for i in range(len(tbl_simbolos)):
            arq.write("| " + str(tbl_simbolos["linha"][i]).ljust(8))
            arq.write("| " + str(tbl_simbolos["coluna"][i]).ljust(8))
            arq.write("| " + tbl_simbolos["token"][i].ljust(20))
            if(tbl_simbolos["lexema"][i] != None):
                arq.write("| " + tbl_simbolos["lexema"][i].ljust(28))
            else:
                arq.write("| " + " ".ljust(28))
            arq.write("|\n")
        arq.write("+-----------------------------------------------------------------------+\n")

def saida_codigo_fonte(nome_arquivo, tbl_erros, count_linhas, nome_saida):
    dg_linhas = len(str(count_linhas))
    pos_err = 0
    linha_att = 1
    
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio_superior = os.path.dirname(diretorio_atual)
    caminho_arquivo = os.path.join(diretorio_superior, 'testes', nome_saida)
    
    with open(nome_arquivo, 'r') as fonte:
        with open(caminho_arquivo, 'w') as saida:
            for linha in fonte:
                saida.write("[")
                saida.write(str(linha_att).rjust(dg_linhas))
                saida.write("]  ")
                linha_att += 1
                saida.write(linha)
                if pos_err < len(tbl_erros):
                    while(tbl_erros["linha"][pos_err] == linha_att-1):
                        saida.write(" " * (dg_linhas + 3 + tbl_erros["coluna"][pos_err]))
                        saida.write("^--")
                        saida.write(" Erro (ln ")
                        saida.write(str(tbl_erros["linha"][pos_err]))
                        saida.write(", col ")
                        saida.write(str(tbl_erros["coluna"][pos_err]))
                        saida.write("): ")
                        saida.write(tbl_erros["mensagem"][pos_err])
                        saida.write("\n")
                        pos_err += 1
                        if pos_err >= len(tbl_erros):
                            break

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio_superior = os.path.dirname(diretorio_atual)
main(os.path.join(diretorio_superior, 'testes', "ex1.cic"))
main(os.path.join(diretorio_superior, 'testes', "ex2.cic"))
main(os.path.join(diretorio_superior, 'testes', "ex3.cic"))