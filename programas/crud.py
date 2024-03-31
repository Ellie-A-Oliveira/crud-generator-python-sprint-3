from programas.helper import InputTypes, safe_input, deseja_continuar


def gerar_campo(
    nome_propriedade: str,
    titulo: str,
    tipo: InputTypes,
    artigo: str = "o",
    identificador: bool = False,
):
    return {
        "nome_propriedade": nome_propriedade,
        "titulo": titulo,
        "tipo": tipo,
        "artigo": artigo,
        "identificador": identificador,
    }


class Crud:
    artigo_nome_classe_dados: str
    nome_classe_dados: str
    campos: list
    campo_identificador: dict
    dados = []

    def __init__(self, artigo_nome_classe_dados: str, nome_classe_dados: str, campos: list):
        self.artigo_nome_classe_dados = artigo_nome_classe_dados
        self.nome_classe_dados = nome_classe_dados
        self.campos = campos

        campos_identificadores = list(filter(lambda campo: campo["identificador"], self.campos))

        if len(campos_identificadores) == 0:
            raise Exception("Um campo identificador deve existir nos campos!")
        elif len(campos_identificadores) > 1:
            raise Exception("Apenas um campo identificador pode ser declarado nos campos!")
        else:
            campo_identificador = campos_identificadores[0]
            self.campo_identificador = campo_identificador

    def __listar_dado(self, dado):
        print("-" * 35)
        for campo in self.campos:
            print(f"{campo['titulo']}: {dado[campo['nome_propriedade']]}")

    def __existem_dados(self):
        return len(self.dados) > 0

    def __encontrar_por_identificador(self, identificador):
        return next(
            filter(lambda dado: dado[self.campo_identificador['nome_propriedade']] == identificador, self.dados),
            None
        )

    def __coletar_identificador(self):
        return safe_input(
            f"Digite {self.campo_identificador['artigo']} {self.campo_identificador['titulo'].lower()} do {self.nome_classe_dados.lower()}: ",
            InputTypes.NUMERO_INTEIRO
        )

    def criar(self):
        objeto = {}
        for campo in self.campos:
            objeto[campo["nome_propriedade"]] = (
                safe_input(
                    f"Digite {campo['artigo']} {campo['titulo'].lower()} do {self.nome_classe_dados.lower()}: ",
                    campo["tipo"]
                )
            )

        print(f"{self.nome_classe_dados} adicionad{self.artigo_nome_classe_dados} com sucesso!")
        self.dados.append(objeto)

    def listar(self):
        if not self.__existem_dados():
            print(f"Nenhum dado cadastrado para {self.nome_classe_dados.lower()}!")

        for dado in self.dados:
            self.__listar_dado(dado)

    def listar_pelo_identificador(self):
        if not self.__existem_dados():
            print(f"Nenhum dado cadastrado para {self.nome_classe_dados.lower()}!")

        identificador = self.__coletar_identificador()
        dado_encontrado = self.__encontrar_por_identificador(identificador)

        if dado_encontrado:
            self.__listar_dado(dado_encontrado)
        else:
            print(f"{self.nome_classe_dados} não encontrado com {self.campo_identificador['artigo']} {self.campo_identificador['titulo'].lower()} {identificador}!")

    def atualizar_pelo_identificador(self):
        if not self.__existem_dados():
            print(f"Nenhum dado cadastrado para {self.nome_classe_dados.lower()}!")

        identificador = self.__coletar_identificador()
        dado_encontrado = self.__encontrar_por_identificador(identificador)

        if dado_encontrado:
            _continue = 1
            while _continue == 1:
                print("\n")
                for i in range(len(self.campos)):
                    campo = self.campos[i]
                    numero_opcao = i + 1

                    print(f"{numero_opcao}-{campo["titulo"]}")

                numero_campo_selecionado = safe_input("\nSelecione o campo que deseja modificar: ", InputTypes.NUMERO_INTEIRO)

                idx_campo_selecionado = next(
                    filter(
                        lambda idx_campo: idx_campo + 1 == numero_campo_selecionado,
                        range(len(self.campos))
                    ),
                    None
                )

                if idx_campo_selecionado:
                    campo_selecionado = self.campos[idx_campo_selecionado]
                    novo_valor = safe_input(
                        f"Digite {campo_selecionado['artigo']} {campo_selecionado['titulo'].lower()} novo: ",
                        campo_selecionado["tipo"]
                    )

                    dado_encontrado[campo_selecionado["nome_propriedade"]] = novo_valor
                    print(f"{campo_selecionado['titulo']} atualizado com sucesso!")
                else:
                    print("Opção inválida!")

                _continue = deseja_continuar(f"Deseja continuar modificando {self.artigo_nome_classe_dados} {self.nome_classe_dados.lower()}?")

            print(f"{self.nome_classe_dados} de {self.campo_identificador['titulo'].lower()} {identificador} atualizado com sucesso!")
        else:
            print(f"{self.nome_classe_dados} não encontrado com {self.campo_identificador['artigo']} {self.campo_identificador['titulo'].lower()} {identificador}!")

    def remover_pelo_identificador(self):
        if not self.__existem_dados():
            print(f"Nenhum dado cadastrado para {self.nome_classe_dados.lower()}!")

        identificador = self.__coletar_identificador()
        dado_encontrado = self.__encontrar_por_identificador(identificador)

        if dado_encontrado:
            self.dados.remove(dado_encontrado)
            print(f"{self.nome_classe_dados} com {self.campo_identificador['artigo']} {self.campo_identificador['titulo'].lower()} {identificador} removido com sucesso!")
        else:
            print(f"{self.nome_classe_dados} não encontrado com {self.campo_identificador['artigo']} {self.campo_identificador['titulo'].lower()} {identificador}!")


def gerar_crud(artigo_nome_classe_dados, nome_classe_dados: str, campos: list):
    return Crud(artigo_nome_classe_dados, nome_classe_dados, campos)
