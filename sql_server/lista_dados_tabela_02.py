import pyodbc

# Conectando ao banco de dados
conexao = pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=DESKTOP-HVTNLUB\SQLEXPRESS;" 
                         "Database=agenda;" "Trusted_Connection=yes;")

mycursor = conexao.cursor()
comando_sql = 'SELECT * FROM cidade'
mycursor.execute(comando_sql)

linha = mycursor.fetchone()
while linha:
    print(f'cidade: {linha[0]} - Email: {linha[1]}')
    linha = mycursor.fetchone()




