import requests
import webbrowser


class Pokemon:
    def abrir_site(self):
        webbrowser.open('https://bulbapedia.bulbagarden.net/', 1, True)

    def testar_pokedex(self):
        url = "https://pokeapi.co/api/v2/"
        payload = ""
        response = requests.request("GET", url, data=payload)
        data = response.status_code
        if data == 200:
            return True
        return False

    def captura_dados_pokemon(self):
        pass

    def captura_tipos_pokemon(self):
        pass
