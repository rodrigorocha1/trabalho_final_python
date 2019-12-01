import pokemon
import banco_pokemon as bp


class Menu:
    def mostrar_menu(self):
        while True:
            pk = pokemon.Pokemon()
            bpk = bp.BancoPokemon()

            print(
                "1-Testar Pokedex\n2-Mais detalhes\n3-Capturar dados\n4-Dados Completos\n5-Sair")
            op = int(input())
            if op == 1:
                if pk.testar_pokedex():
                    print('Pokedex online')
                else:
                    print('Pokedex Offline')
            elif op == 2:
                print('Abrindo navegador externo...')
                pk.abrir_site()
            elif op == 3:
                id_pk = int(input('Digite o Id do pokemon: '))
                id_local = pk.localizacao_pokemon(id_pk)
                pk.captura_dados_pokemon(id_pk, id_local)
            elif op == 4:
                id_pk = int(input('Digite o Id do pokemon: '))
                bp.BancoPokemon().consulta_completa(id_pk)
            elif op == 5:
                exit()
            else:
                print('Op invalida')
