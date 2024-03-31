from programas.crud import gerar_campo
from programas.helper import InputTypes

campos_cliente = [
    gerar_campo("id", "ID", tipo=InputTypes.NUMERO_INTEIRO, identificador=True),
    gerar_campo("nome", "Nome"),
    gerar_campo("sobrenome", "Sobrenome"),
    gerar_campo("email", "E-mail"),
    gerar_campo("tipo", "Tipo"),
    gerar_campo("idioma", "Idioma"),
    gerar_campo("pais", "País"),
    gerar_campo("telefone", "Telefone"),
]

campos_empresa = [
    gerar_campo("id", "ID", tipo=InputTypes.NUMERO_INTEIRO, identificador=True),
    gerar_campo("nome", "Nome"),
    gerar_campo("tipo_industria", "Indústria", artigo="a"),
    gerar_campo("tamanho", "Tamanho"),
    gerar_campo("pais_sede", "País Sede"),
]

campos_funcionario = [
    gerar_campo("id", "ID", tipo=InputTypes.NUMERO_INTEIRO, identificador=True),
    gerar_campo("nome", "Nome"),
    gerar_campo("sobrenome", "Sobrenome"),
    gerar_campo("email", "E-mail"),
    gerar_campo("cargo", "Cargo"),
    gerar_campo("telefone", "Telefone"),
    gerar_campo("salario", "Salário", tipo=InputTypes.NUMERO_REAL),
]

campos_perguntas_frequentes = [
    gerar_campo("id", "ID", tipo=InputTypes.NUMERO_INTEIRO, identificador=True),
    gerar_campo("tipo_produto", "Tipo do Produto"),
    gerar_campo("pergunta", "Pergunta", artigo="a"),
    gerar_campo("resposta", "Resposta", artigo="a"),
]

campos_produto = [
    gerar_campo("id", "ID", tipo=InputTypes.NUMERO_INTEIRO, identificador=True),
    gerar_campo("empresa", "Empresa", artigo="a"),
    gerar_campo("preco", "Preço", tipo=InputTypes.NUMERO_REAL),
    gerar_campo("status", "Status"),
    gerar_campo("plano_contratado", "Plano Contratado"),
    gerar_campo("tipo_produto", "Tipo do Produto"),
    gerar_campo("teste_gratis_ate", "Teste Grátis Até"),
]

campos_recurso = [
    gerar_campo("id", "ID", tipo=InputTypes.NUMERO_INTEIRO, identificador=True),
    gerar_campo("nome", "Nome"),
    gerar_campo("notas_preco", "Notas do Preço", artigo="as"),
    gerar_campo("descricao", "Descrição", artigo="a"),
    gerar_campo("categoria", "Categoria", artigo="a"),
]

campos_tipo_plano = [
    gerar_campo("id", "ID", tipo=InputTypes.NUMERO_INTEIRO, identificador=True),
    gerar_campo("nome", "Nome"),
    gerar_campo("descricao", "Descrição", artigo="a"),
    gerar_campo("preco", "Preço", tipo=InputTypes.NUMERO_REAL),
    gerar_campo("tipo_preco", "Tipo do Preço"),
    gerar_campo("nivel_plano", "Nível do Plano"),
    gerar_campo("recursos", "Recursos", artigo="os"),
    gerar_campo("teste_gratis_disponivel", "Teste Grátis Disponível? (1-SIM;0-NÃO)", tipo=InputTypes.VERDADEIRO_FALSO),
]

campos_tipo_produto = [
    gerar_campo("id", "ID", tipo=InputTypes.NUMERO_INTEIRO, identificador=True),
    gerar_campo("nome", "Nome"),
    gerar_campo("descricao", "Descrição", artigo="a"),
    gerar_campo("planos_disponíveis", "Planos Disponíveis", artigo="os"),
    gerar_campo("is_add_on", "É Add On? (1-SIM;0-NÃO)", tipo=InputTypes.VERDADEIRO_FALSO),
    gerar_campo("nome_grupo", "Nome do Grupo"),
]
