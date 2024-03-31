from programas.crud import gerar_crud
from programas.helper import safe_input, InputTypes, deseja_continuar

campos_cliente = getattr(__import__("programas.lista-campos"), "lista-campos").campos_cliente


def main():
    cliente_crud = gerar_crud("o", "Cliente", campos_cliente)

    print(f"Bem-vindo ao CRUD para {cliente_crud.nome_classe_dados}!")
    _continue = 1
    while _continue == 1:
        print("Opções:\n1-LISTAR\n2-LISTAR UM\n3-CRIAR\n4-ATUALIZAR UM\n5-REMOVER UM\n")
        opcao = safe_input("Digite a opção que deseja: ", InputTypes.NUMERO_INTEIRO)

        match opcao:
            case 1:
                cliente_crud.listar()
            case 2:
                cliente_crud.listar_pelo_identificador()
            case 3:
                cliente_crud.criar()
            case 4:
                cliente_crud.atualizar_pelo_identificador()
            case 5:
                cliente_crud.remover_pelo_identificador()
            case _:
                print("Opção inválida!")

        _continue = deseja_continuar()


if __name__ == '__main__':
    main()
