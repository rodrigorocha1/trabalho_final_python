import pokemon


class Menu:
    def mostrar_menu(self):
        while True:
            pk = pokemon.Pokemon()
            print("1-Testar Pokedex\n2-Mais detalhes\n")
            op = int(input())
            if op == 1:
                if pk.testar_pokedex():
                    print('Pokedex online')
                else:
                    print('Pokedex Offline')
            else:
                print('Abrindo navegador externo')
                pk.abrir_site()
