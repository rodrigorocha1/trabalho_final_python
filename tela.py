import cadastro_usuario as cc
import menu as m

while True:
    print('*' * 20, "Bem vindo a pokedex", '*' * 20)
    print("1-Acessar\n2-Cadastrar Usuário\n3-Esqueci a senha\n4-Sobre\n5-Sair")
    op = int(input())
    if op == 1:
        nome = input('Digite o nome do usuário: ').upper()
        senha_usuario = input('Digite a senha do usuário: ')
        user = cc.Usuario(nome, senha_usuario)
        if (user.validar_login() == True):
            tela_menu = m.Menu()
            tela_menu.mostrar_menu()
        else:
            print('Login Invalido')
    elif op == 2:
        nome = input('Digite o nome do usuário: ').upper()
        senha_usuario = input('Digite a senha do usuário: ')

        if len(senha_usuario) == 6:
            user = cc.Usuario(nome, senha_usuario)
            user.inserir_usuario()
        else:
            print('A senha deverá ter seis carateres')
    elif op == 3:
        user = cc.Usuario(None, None)
        user.buscar_usuarios()
    elif op == 4:
        print('Uma pokedex em python\nAluno: Rodrigo Silva Rocha\nRA: 2840481621036')
    elif op == 5:
        print('Saindo....')
        exit()
