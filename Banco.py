import psycopg2 as pg
import psycopg2.extras
import Conexao as cx


class Banco:

    def criar_tabela(self):

        conexao = cx.Conexao()
        con = conexao.criar_conexao()
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS tb_editora")
        cur.execute(
            "CREATE TABLE tb_editora (Id SERIAL PRIMARY KEY, nome_livro VARCHAR(100))")
        con.commit()
        con.close()
        print('Tabela Criada')

    def inserir_livro(self, nome_livro):
        conexao = cx.Conexao()
        con = conexao.criar_conexao()
        cur = con.cursor()
        try:

            sql = (
                f"INSERT INTO tb_editora(nome_livro) values ('{nome_livro}')")
            cur.execute(cur.mogrify(sql))
            print("Inserção feita com sucesso")
            con.commit()
        except Exception as e:
            print(e)
        con.close()

    def exibir(self):
        conexao = cx.Conexao()
        con = conexao.criar_conexao()
        cur = con.cursor()
        sql = "SELECT * FROM tb_editora order by id"
        cur.execute(sql)
        linhas = cur.fetchall()
        if len(linhas) == 0:
            print('Tabela vazia')
        else:
            print('=======================')
            for linha in linhas:
                print("Id = %d " % linha[0])
                print("Nome = %s " % linha[1])
                print('=======================')
        con.close()

    def atualizar(self, id_livro, nome_livro):
        conexao = cx.Conexao()
        con = conexao.criar_conexao()
        cur = con.cursor()
        sql = (
            f"UPDATE tb_editora SET nome_livro = ('{nome_livro}') WHERE id=({id_livro})")
        cur.execute(cur.mogrify(sql))
        print("Total linhas atualizadas %s" % cur.rowcount)
        con.commit()
        con.close()

    def deletar(self, id_livro):
        conexao = cx.Conexao()
        con = conexao.criar_conexao()
        cur = con.cursor()
        sql = f"DELETE FROM tb_editora WHERE id=({id_livro})"
        cur.execute(cur.mogrify(sql))
        print("Total linhas atualizadas %s" % cur.rowcount)
        con.commit()
        con.close()
