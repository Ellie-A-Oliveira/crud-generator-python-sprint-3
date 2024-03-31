from enum import Enum
from functools import reduce


class InputTypes(Enum):
    TEXTO = str
    NUMERO_INTEIRO = int
    NUMERO_REAL = float
    VERDADEIRO_FALSO = bool


def safe_input(message: str, input_type: InputTypes = InputTypes.TEXTO):
    """
    input() function which only returns if the user input is the type of provided input_type.
    It will keep prompting user to enter a value until it is valid.
    :param message: message to display to the user
    :param input_type: expected input type
    :return: a value of type input_type
    """
    result: input_type.value

    _continue = 1
    while _continue == 1:
        try:
            result = input_type.value(input(message))
            _continue = 0
        except ValueError as e:
            print(f"Esperava a entrada de um {input_type.name}. Erro: {e}")

    return result


def deseja_continuar(message: str = "Deseja continuar?") -> bool:
    _continue = 1
    while _continue == 1:
        opcao = safe_input(message + " (1-SIM;0-NÃO) ", InputTypes.NUMERO_INTEIRO)

        if opcao != 1 and opcao != 0:
            print("Número digitado inválido!")
        else:
            return opcao == 1
