

def entradaUsuario(): 
    global acao 
    print('''1: Cadastrar novo aluno. 
    Listar alunos cadastrados. 
    Procurar aluno pelo nome. 
    SAIR.''') 
    acao = int(input('O que deseja fazer? ')) 

def cadastraAluno(): 
    print('Cadastro de aluno. Preencha as informações:') 
    nome = input('Nome: ') 
    email = input('E-mail: ') 
    curso = input('Curso: ') 
    aluno = f'{nome}, {email}, {curso}\n' 
    with open('alunos.txt', 'a', encoding='UTF-8') as arquivo: 
        arquivo.write(aluno) 

def listaAluno(): 
    print('\nLista de alunos cadastrados:') 
    with open('alunos.txt', 'r', encoding='utf-8') as arquivo: 
        listaAlunos = arquivo.read().split('\n') 
    print('Nome, Email, Curso') 
    for aluno in listaAlunos: 
        print(aluno) 

def procuraAluno(): 
    print('Buscar aluno por nome:') 
    busca = input('Nome: ') 
    with open('alunos.txt', 'r', encoding='utf-8') as arquivo: 
        listaAlunos = arquivo.read().split('\n') 
    resultado = None 
    for aluno in listaAlunos: 
        nomeAluno = aluno.split(',')[0].rstrip() 
        if busca == nomeAluno: 
            resultado = aluno 
            break 
    if resultado == None: 
     print('\nNão foi encontrado nenhum aluno com esse nome.\n') 
    else: 
     print(resultado+'\n')
while True: 
    entradaUsuario()

    if acao == 1: 
        cadastraAluno() 
    elif acao == 2: 
        listaAluno() 
    elif acao == 3: 
        procuraAluno() 
    elif acao == 4: 
        break 
    else: 
     print('\n::::: Escolha uma das quatro opções! :::::\n') 

     