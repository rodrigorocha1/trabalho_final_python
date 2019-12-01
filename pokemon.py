import requests
import webbrowser
import json
from jsonpath_ng import jsonpath, parse
import banco_pokemon as pk


class Pokemon:

    def abrir_site(self):
        webbrowser.open(
            'https://pt.wikipedia.org/wiki/Lista_de_Pok%C3%A9mon', 1, True)

    def testar_pokedex(self):
        url = "https://pokeapi.co/api/v2/"
        payload = ""
        response = requests.request("GET", url, data=payload)
        data = response.status_code
        if data == 200:
            return True
        return False

    def captura_dados_pokemon(self, id_pk, id_local):
        url_dados = 'https://pokeapi.co/api/v2/pokemon/' + str(id_pk) + "/"
        payload = ""
        response = requests.request("GET", url_dados, data=payload)
        data = response.json()

        id_tipo_exp = parse("$['types'][0]['type']['url']")
        match_tipo_id_url = id_tipo_exp.find(data)
        id_url_tipo = match_tipo_id_url[0].value

        id_tipo = id_url_tipo.replace('//', '/').replace(':',
                                                         '').replace(" "" ", '').split('/')[-2]
        print(id_tipo)

        name_pk_exp = parse('$[name]')
        id_pk_exp = parse("$['id']")
        match_id = id_pk_exp.find(data)
        match_nome = name_pk_exp.find(data)

        tipo_nome_exp = parse("$['types'][0]['type']['name']")

        match_tipo_nome = tipo_nome_exp.find(data)
        if id_tipo == None:
            id_tipo = -1
        pk.BancoPokemon().inserir_tipo_pokemon(
            id_tipo,  match_tipo_nome[0].value)
        pk.BancoPokemon().inserir_pokemon(
            match_id[0].value, match_nome[0].value, id_tipo, id_local)

    def localizacao_pokemon(self, id_pk):

        stg = "/encounters"
        url_local = 'https://pokeapi.co/api/v2/pokemon/' + str(id_pk) + stg
        payload = ""
        response = requests.request("GET", url_local, data=payload)
        data = response.json()

        id_locap_exp = parse("$[0]['location_area'].['url']")
        match_id_url_local = id_locap_exp.find(data)

        if not match_id_url_local:
            id_local = -1
            tipo_nome = 'Local não encontrado'
        else:
            id_url_local = match_id_url_local[0].value
            id_local = id_url_local.replace('//', '/').replace(':',
                                                               '').replace(" "" ", '').split('/')[-2]

            name_local_exp = parse("$[0]['location_area'].['name']")
            match_tipo_nome = name_local_exp.find(data)
            tipo_nome = match_tipo_nome[0].value

        bck = pk.BancoPokemon()
        bck.inserir_local_pokemon((id_local), tipo_nome)
        print(id_local)
        return id_local
