while True:
    try:
        e = input()
        if( e == '2002' ):
            print("Acesso Permitido")
            break
        else:
            print("Senha Invalida")       
    except EOFError:
        break
