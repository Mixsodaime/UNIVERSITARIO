

import sqlite3

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect('/aularadpy/registalpr.bd')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar tabela de alunos
cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    idade INTEGER,
                    turma TEXT
                )''')

# Criar tabela de professores
cursor.execute('''CREATE TABLE IF NOT EXISTS professores (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    disciplina TEXT
                )''')

# Commit para salvar as alterações
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()


def adicionar_aluno(nome, idade, turma):
    conn = sqlite3.connect('/aularadpy/registalpr.bd')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO alunos (nome, idade, turma') 
    conn.commit()
    conn.close()

def adicionar_professor(nome, disciplina):
    conn = sqlite3.connect('registro.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO professores (nome, disciplina')
    conn.commit()
    conn.close()

def listar_alunos():
    conn = sqlite3.connect('/aularadpy/registalpr.bd')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alunos')
    alunos = cursor.fetchall()
    conn.close()
    return alunos

def listar_professores():
    conn = sqlite3.connect('/aularadpy/registalpr.bd')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM professores')
    professores = cursor.fetchall()
    conn.close()
    return professores


    # Adicionar alguns alunos e professores
    adicionar_aluno('João', 15, '9A')
    adicionar_aluno('Maria', 14, '8B')
    adicionar_professor('Sr. Silva', 'Matemática')
    adicionar_professor('Sra. Souza', 'História')

# Listar todos os alunos e professores
    print("Alunos:")
    print(listar_alunos)
    print("Professores:")
    print(listar_professores)

