import Conexao as cx


class BancoPokemon:
    def inserir_local_pokemon(self, id_local, nome_local):
        conexao = cx.Conexao()
        con = conexao.criar_conexao()
        cur = con.cursor()
        try:

            sql_ins = (
                f"INSERT INTO local_pokemon(id_local_pokemon, localizacao) values ('{id_local}', '{nome_local}')")
            cur.execute(cur.mogrify(sql_ins))
            print('local cadastrado')
            con.commit()
        except Exception as e:
            print(e)
        con.close()

    def inserir_tipo_pokemon(self, id_tipo, nome_tipo):
        conexao = cx.Conexao()
        con = conexao.criar_conexao()
        cur = con.cursor()
        try:

            sql_ins = (
                f"INSERT INTO tipo_pokemon(id_tipo_pokemon, nome_tipo_pokemon) values ('{id_tipo}', '{nome_tipo}')")
            cur.execute(cur.mogrify(sql_ins))
            print('Tipo cadastrado')
            con.commit()
        except Exception as e:
            print(e)
        con.close()

    def inserir_pokemon(self, id_pokemon, nome_pokemon, id_tipo_pokemon_1, id_localizacao_pokemon):
        conexao = cx.Conexao()
        con = conexao.criar_conexao()
        cur = con.cursor()
        try:

            sql_ins = (
                f"INSERT INTO tb_pokemon(id_pokemon, nome_pokemon, id_tipo_pokemon_1, id_localizacao_pokemon) values ('{id_pokemon}', '{nome_pokemon}', '{id_tipo_pokemon_1}', '{id_localizacao_pokemon}')")
            cur.execute(cur.mogrify(sql_ins))
            print('Pokemon cadastrado')
            con.commit()
        except Exception as e:
            print(e)
        con.close()

    def consulta_completa(self, id_pk):
        conexao = cx.Conexao()
        con = conexao.criar_conexao()
        cur = con.cursor()
        try:
            sql = f'select pk.nome_pokemon, tp.nome_tipo_pokemon, lp.localizacao from tb_pokemon pk inner join local_pokemon lp on lp.id_local_pokemon = pk.id_localizacao_pokemon inner join tipo_pokemon tp on tp.id_tipo_pokemon = pk.id_tipo_pokemon_1 where pk.id_pokemon ={id_pk}'
            cur.execute(cur.mogrify(sql))
            linhas = cur.fetchall()
            for linha in linhas:
                print("Pokemon:  " + linha[0] +
                      " Tipo:  " + linha[1] + "  Localização:  " + linha[2], end='')
            print()
        except Exception as e:
            print("Deu ruim!")
