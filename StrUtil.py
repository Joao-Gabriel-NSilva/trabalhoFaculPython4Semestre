def contem_numero(string: str) -> bool:
    return True in [x in '1234567890' for x in string]

