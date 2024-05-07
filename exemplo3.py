import sqlite3 as conector #apelido
#funçao para criar a estrutura da tabela
def criar_tabela():
    print('Abrindo uma conexao de bd')
    conexao = conector.connect('d:/banco/academia.db')
    cursor = conexao.cursor()
    #execuçao de comandos SQL
    sql = "create table cadastro (codigo integer, nome text, idade integer)"#criar tabela
    cursor.execute(sql)
    sql = '''insert into cadastro (codigo, nome, idade) values 
    (1284, 'pedro de oliveira',32)''' #inserir registros 
    cursor.execute(sql)
    
    sql = "insert into cadastro (codigo, nome, idade) values   (1309, 'LUCIA Machado' ,37)"
    cursor.execute(sql)
    #efetivaçao do comando
    conexao.commit()
    #fechamento das conexoes
    cursor.close()
    conexao.close()
    #executar funçao
   
    print("Abra a pasta do programa e veja se o arquivo esta la")
    print("Fim do programa")



 



criar_tabela()


  

    


