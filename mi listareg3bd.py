
import sqlite3 as conector #apelido
def listar_tabelas_relacionadas():
    try:
        conexao = conector.connect('/aularadpy/mi listareg3bd')
        cursor = conexao.cursor()
        sql = 'SELECT * FROM Pessoa'
        cursor.execute(sql)
        pessoas = []
        reg_pessoas = cursor.fetchall()
        for reg_pessoa in reg_pessoas:
         cpf,nome,nascimento,oculos = reg_pessoa
        print('Proprietário:',nome)
        veiculos = recuperar_veiculos(conexao,cpf)
        pessoas.append(veiculos)
    except conector.DatabaseError as err:
        print('Erro de banco de dados',err)
    finally:
        if(conexao):
            cursor.close()
            conexao.close()

def recuperar_veiculos(conexao, cpf):
    try:
        cursor = conexao.cursor()
        sql = 'SELECT * FROM Veiculo JOIN Marca ON Marca.id=Veiculo.marca WHERE Veiculo.proprietario=?;'
        cursor.execute(sql,(cpf,))
        veiculos = []
        registros = cursor.fetchall()
        for registro in registros:
         veiculos.append(registro)
        print(registro)
    except conector.DatabaseError as err:
        print('Erro de banco de dados',err)
    finally:
        cursor.close()
        return (veiculos)
        #executar função
        listar_tabelas_relacionadas()
        #encerrando
        print("Fim do programa")
