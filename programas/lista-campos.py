from programas.crud import gerar_campo
from programas.helper import InputTypes

campos_cliente = [
    gerar_campo("id", "ID", InputTypes.NUMERO_INTEIRO, identificador=True),
    gerar_campo("nome", "Nome", InputTypes.TEXTO),
    gerar_campo("sobrenome", "Sobrenome", InputTypes.TEXTO),
    gerar_campo("email", "E-mail", InputTypes.TEXTO),
    gerar_campo("tipo", "Tipo", InputTypes.TEXTO),
    gerar_campo("idioma", "Idioma", InputTypes.TEXTO),
    gerar_campo("pais", "País", InputTypes.TEXTO),
    gerar_campo("telefone", "Telefone", InputTypes.TEXTO),
]