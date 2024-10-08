from etl import *

lista_de_produtos = ler_csv(path_arquivo)

produtos_filtrados = filtrar_produtos_nao_entregues(lista_de_produtos=lista_de_produtos)

total_dos_valores = somar_valores_dos_produtos(lista_com_produtos_filtrados=produtos_filtrados)

print(total_dos_valores)