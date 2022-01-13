import json
import os
def chamarMenu():
    escolha = int(input("\nDigite: \n | <1> Para registrar ativo \n | <2> Para exibir ativos armazenados \n | <3> Para finalizar busca\n > "))

    return escolha

def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq_json:
            dicionario = json.load(arq_json)
    else:
        dicionario = {}
    return dicionario

def gravar_arquivo(dicionario, arquivo):
    with open(arquivo, "w") as arq_json:
        json.dump(dicionario, arq_json)

def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("\nDigite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
        resp = input("\nDigite <S> para continuar ou <R> para retornar as opções: ").upper()
        gravar_arquivo(dicionario, arquivo)
    return "\nJSON gerado!!!\n"

def exibir(arquivo):
    dicionario = ler_arquivo(arquivo)
    for chave, dado in dicionario.items():
        print("\nData.........: ", dado[0])
        print("Descrição....: ", dado[1])
        print("Departamento.: ", dado[2], "\n")