import mysql.connector
import getpass

senha = getpass.getpass("Qual é sua senha ?")
con = mysql.connector.connect(
    host = 'seu_host',
    user = 'seu_usuario',
    password = senha,
    database = 'seu_banco_de_dados',
)
cursor = con.cursor()
try:
    # Cria a tabela
    cursor.execute("CREATE TABLE IF NOT EXISTS livros(livro_id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255),autor VARCHAR(255),ano INT,editora_id INT)")
    # Adiciona valores
    adiciona = "INSERT INTO livros(nome,autor,ano,editora_id) VALUES(%s,%s,%s,%s)"
    valores = [('Pai rico pai pobre','Robert T. Kiyosaki','2001',1),('Me poupe','Nathalia Arcuri','2021',2),('O investidor inteligente','Benjamin Graham','1992',3)]
    cursor.executemany(adiciona,valores)
    con.commit()
    # Mostra os valores
    print("Livros publicados antes de 2000:")
    cursor.execute("SELECT * FROM livros WHERE ano < 2000")
    resultado = cursor.fetchall()
    for c in resultado:
        print(c)
    print('-' * 30)
    # Criando outra tabela
    cursor.execute("CREATE TABLE IF NOT EXISTS editora(editora_id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255))")
    # Inserindo elementos na tabela editora:
    values = "INSERT INTO editora(nome) VALUES(%s)"
    add = [('Alta Books',), ('Sextante',), ('Harper Collins',)]
    cursor.executemany(values, add)
    con.commit()
    # Inserindo uma tabela na outra
    consulta = """
        SELECT livros.nome, livros.autor, editora.nome
        FROM livros
        JOIN editora ON livros.editora_id = editora.editora_id
    """
    cursor.execute(consulta)
    resultados= cursor.fetchall()
    print("Todos os livros:")
    for c in resultados:
        print(c)
except mysql.connector.Error as Err:
    print(Err)
    cursor.execute("DROP TABLE livros")
    cursor.execute("DROP TABLE editora")
finally:
    # Fechando a conexão
    con.close()
    cursor.close()