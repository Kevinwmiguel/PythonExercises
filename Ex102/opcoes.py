from linhas import ilinha as l
def menu():
    print('\033[33m1 - \033[34mVerpessoas cadastradas\033[m')
    print('\033[33m2 - \033[34mCadastrar novas pessoa\033[m')
    print('\033[33m3 - \033[34mSair do sistema\033[m')
    l()
    while True:
        esc = int(input('\033[32mSua Opção: \033[m'))
        if esc > 3 and esc < 1:
            print('\033[31mERRO! Digiteu uma opção válida\033[m')
        break
    l()
    """
     -> LER UM ARQUIVO:
         OBS: open('Arquivo', 'opção')
    'rt' -> usado somente para ler algo
    'w+' -> somentado para escrever algo O + CRIA CASO NAO EXISTA
    'r+' -> ler e escrever
    'a' -> acrescentar
    """
    if esc == 1:
        try:
            pessoas = open('dados.txt', 'rt')
        except:
            print('Erro ao ler o arquivo')
        else:
            print('PESSOAS CADASTRADAS')
            for linha in pessoas:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n','')
                print(f'{dado[0]:<30}{dado[1]:3>} anos')
        finally:
            pessoas.close()

    if esc == 2:
        while True:
            nome = str(input('nome: ')).strip()
            if not nome.isnumeric():
                break
            else:
                print('\033[31mERRO: por favor digite um nome valido\033[m')
        while True:
            idade = str(input('idade: '))
            if idade.isnumeric():
                break
            else:
                print('\033[31mERRO: por favor digite uma idade valida\033[m')
        with open('dados.txt', 'at') as f:
            f.write(f'{nome};{idade} anos\n')
    if esc == 3:
        print('Saindo...')
        print('Até a próxima meu querido!')