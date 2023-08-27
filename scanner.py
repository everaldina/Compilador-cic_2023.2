import pandas as pd
import gerar_tabela as gt

tabela_transicao, estados_acc = gt.gerar_tabela()
print(estados_acc)


# lista com palavras reservadas da linguagem
reserv = ["programa", "fim_programa", "se", "entao", "imprima", "leia", "enquanto"]

def prox_estado(estado_atual, char):
    return tabela_transicao.at[estado_atual, char]