import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Funcao que le um arquivo csv e retorna uma lista de dicionario
    """
    lista_de_produtos = []
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista_de_produtos.append(linha)
    return lista_de_produtos

def filtrar_produtos_nao_entregues(lista_de_produtos: list[dict]) -> list[dict]:
    """
    Funcao que filtra produtos onde entrega = True
    """
    lista_com_produtos_filtrados = []
    for produto in lista_de_produtos:
        if produto.get("entregue") == "False":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    """
    Funcao que soma os valores dos produtos
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get("valor"))
    return valor_total
