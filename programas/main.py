from programas.crud import gerar_crud
from programas.helper import safe_input, InputTypes, deseja_continuar

campos = getattr(__import__("programas.lista-campos"), "lista-campos")

campos_cliente = campos.campos_cliente
campos_empresa = campos.campos_empresa
campos_funcionario = campos.campos_funcionario
campos_perguntas_frequentes = campos.campos_perguntas_frequentes
campos_produto = campos.campos_produto
campos_recurso = campos.campos_recurso
campos_tipo_plano = campos.campos_tipo_plano
campos_tipo_produto = campos.campos_tipo_produto


campos_para_crud = [
    {"campos": campos_cliente, "artigo": "o", "nome": "Cliente"},
    {"campos": campos_empresa, "artigo": "a", "nome": "Empresa"},
    {"campos": campos_funcionario, "artigo": "o", "nome": "Funcionário"},
    {"campos": campos_perguntas_frequentes, "artigo": "as", "nome": "Perguntas Frequentes"},
    {"campos": campos_produto, "artigo": "o", "nome": "Produto"},
    {"campos": campos_recurso, "artigo": "o", "nome": "Recurso"},
    {"campos": campos_tipo_plano, "artigo": "o", "nome": "Tipo do Plano"},
    {"campos": campos_tipo_produto, "artigo": "o", "nome": "Tipo do Produto"},
]


def listar_crud(tipo_crud):
    print(f"Bem-vindo ao CRUD para {tipo_crud.nome_classe_dados}!")
    _continue = 1
    while _continue == 1:
        print("Opções:\n1-LISTAR\n2-LISTAR UM\n3-CRIAR\n4-ATUALIZAR UM\n5-REMOVER UM\n0-SAIR\n")
        opcao = safe_input("Digite a opção que deseja: ", InputTypes.NUMERO_INTEIRO)

        match opcao:
            case 1:
                tipo_crud.listar()
            case 2:
                tipo_crud.listar_pelo_identificador()
            case 3:
                tipo_crud.criar()
            case 4:
                tipo_crud.atualizar_pelo_identificador()
            case 5:
                tipo_crud.remover_pelo_identificador()
            case 0:
                break
            case _:
                print("Opção inválida!")

        _continue = deseja_continuar()


def main():
    cruds = [crud for crud in list(map(lambda campo: gerar_crud(campo["artigo"], campo["nome"], campo["campos"]), campos_para_crud))]

    print("Bem-vindo ao programa de CRUDs!")

    _continue = 1
    while _continue == 1:
        for i in range(len(cruds)):
            crud = cruds[i]
            numero_opcao = i + 1
            print(f"{numero_opcao}-{crud.nome_classe_dados}")

        opcao = safe_input("\nDigite o CRUD desejado: ", InputTypes.NUMERO_INTEIRO)
        idx_crud_selecionado = next(
            filter(
                lambda idx_campo: idx_campo == opcao - 1,
                range(len(cruds))
            ),
            None
        )

        if idx_crud_selecionado is not None:
            crud = cruds[idx_crud_selecionado]
            listar_crud(crud)
        else:
            print("Opção inválida!")

        _continue = deseja_continuar("Deseja continuar no programa de CRUD?")


if __name__ == '__main__':
    main()
