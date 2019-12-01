import Conexao as bc


class Usuario:
    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha

    @property
    def nome(self):
        return self.nome

    @property
    def senha(self):
        return self.senha

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @nome.setter
    def senha(self, senha):
        self.__senha = senha

    def inserir_usuario(self):

        conexao = bc.Conexao()
        con = conexao.criar_conexao()
        cur = con.cursor()
        try:

            sql_ins = (
                f"INSERT INTO tb_usuario(nome_usuario, senha_usuario) values ('{self.__nome}', '{self.__senha}')")
            cur.execute(cur.mogrify(sql_ins))
            print('Usuário cadastrado')
            con.commit()
        except Exception as e:
            print(e)
        con.close()

    def atualizar_usuario(self):
        conexao = bc.Conexao()
        con = conexao.criar_conexao()
        cur = con.cursor()
        sql_up = (
            f"UPDATE tb_usuario SET senha_usuario = ('{self.__senha}') WHERE nome_usuario=({self.__nome})")
        cur.execute(cur.mogrify(sql_up))
        print("Total de usuários atualizadas %s" % cur.rowcount)
        con.commit()
        con.close()

    def buscar_usuarios(self):
        """Não se esque de implementar a validação aqui também
        """
        nome_usuario = str(input('Digite o nome do usuário: ')).upper()
        conexao = bc.Conexao()
        con = conexao.criar_conexao()
        cur = con.cursor()
        sql_select = f"SELECT nome_usuario FROM tb_usuario WHERE nome_usuario = '{nome_usuario}'"
        cur.execute(cur.mogrify(sql_select))
        linhas = cur.fetchall()
        for linha in linhas:
            nome = linha[0]
        senha = str(input('Digite a senha: '))
        if len(senha) == 6:
            sql_update = (
                f"UPDATE tb_usuario SET senha_usuario = ('{senha}') WHERE nome_usuario=('{nome_usuario}')")
            cur.execute(cur.mogrify(sql_update))
        else:
            print('A senha deve ter seis caracteres')
        con.close()

    def validar_login(self):
        conexao = bc.Conexao()
        con = conexao.criar_conexao()
        cur = con.cursor()
        sql_select_user = f"SELECT nome_usuario, senha_usuario FROM tb_usuario WHERE nome_usuario = '{self.__nome}' and senha_usuario = '{self.__senha}'"
        cur.execute(cur.mogrify(sql_select_user))
        linhas = cur.fetchall()
        if not linhas:
            nome_banco = 'F'
            senha_banco = 'F'
        else:
            for linha in linhas:
                nome_banco = linha[0]
                senha_banco = linha[1]
        if nome_banco == self.__nome and senha_banco == self.__senha:
            return True
        return False
