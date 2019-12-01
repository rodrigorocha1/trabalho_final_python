import psycopg2 as pdb


class Conexao:

    def criar_conexao(self):

        try:
            con = pdb.connect(
                database="trabalho_final_python",
                user="postgres",
                password="1a2s3d",  # senha
                host="127.0.0.1",
                port="5432"
            )

        except Exception as erro:
            print(erro)
            con.close()
            exit(1)
        return con
