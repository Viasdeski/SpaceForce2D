def limparTela():
    import os
    os.system('cls')

def criaBanco():
    try:
        leBanco()
    except:
        arquivo = open('banco.txt', 'w')
        arquivo.close()
    
def leBanco():
    arquivo = open('banco.txt', 'r')
    dados = arquivo.read()
    arquivo.close()
    return dados

def escreveBanco(dados):
    arquivo = open('banco.txt', 'w')
    arquivo.write(dados)
    arquivo.close()

def adicionaBanco(dados):
    arquivo = open('banco.txt', 'a')
    arquivo.write(dados)
    arquivo.close

def insereDados(dados,nome,email):
    dados = dados + "Player: " + nome + "\n" + "E-mail: " + email + "\n"
    return dados

def verificaEmail(email):
    while True:
        try:
            emails = ['@gmail','@hotmail','@outlook','@yahoo']
            for i in email:
                for j in emails:
                    if i == j:
                        break
                    break
        except:                
            print('Formato de e-mail inválido. Tente novamente')