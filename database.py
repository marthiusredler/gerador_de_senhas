import sqlite3

class Data_base:
    def __init__(self, name = "system.db") -> None:
        self.name = name
    
    def connect(self):
        self.connection = sqlite3.connect(self.name)
    
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    
    def create_table_keys(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """
        
            CREATE TABLE IF NOT EXISTS Dados(
                
                TITULO TEXT,
                EMAIL TEXT,
                SENHA TEXT,
                
                PRIMARY KEY(TITULO)
            );
            
            """           
        )
    
    def resgistra_senha(self, alldados):
        campos = ('TITULO','EMAIL','SENHA')
        qtd = ('?,?,?')
        cursor = self.connection.cursor()
        
        try:
            cursor.execute(
                f"""
                INSERT INTO Dados {campos}
                VALUES({qtd})
                """, alldados
            )
            self.connection.commit()
            return "ok"
        except:
            return "Erro"
        
    def select_dados(self):
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                SELECT * FROM Dados ORDER BY TITULO
                """
            )
            dados = cursor.fetchall()
            return dados
        
        except:
            pass
    
    def delete_dado(self, id):
    
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                f"""
                DELETE FROM Dados WHERE TITULO = '{id}'
                """
            )
            self.connection.commit()
            return "Registro de Senha deletado com Sucesso"
        except:
            return "Erro Ao Deletar Registro de Senha!"     
       
    def update_dado(self, alldados):
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            UPDATE Dados set
            
            TITULO = '{alldados[0]}',
            EMAIL = '{alldados[1]}',
            SENHA = '{alldados[2]}'
            
            WHERE TITULO = '{alldados[0]}'
            
            """
        )
        self.connection.commit()
        