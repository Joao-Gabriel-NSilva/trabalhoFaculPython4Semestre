from StrUtil import *


class Aluno:

    def __init__(self, ra: str, nome: str, nota: str):
        if self.valida_valores(ra, nome, nota):
            self._nome = nome.strip()
            self._ra = int(ra.strip())
            self._nota = float(nota.strip().replace(',', '.'))

    @property
    def ra(self):
        return self._ra

    @ra.setter
    def ra(self, value):
        self._ra = int(value)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, value):
        self._nota = float(value)

    def valida_valores(self, ra: str, nome: str, nota: str) -> bool:
        if ra.strip() == '' or nome.strip() == '' or nota.strip() == '':
            raise AttributeError('Todas as informações devem ser preenchidas!')
        if not ra.strip().isdigit():
            raise AttributeError('RA não pode conter letras!')
        if contem_numero(nome):
            raise AttributeError('Nome não pode conter números!')
        if not nota.strip().replace(',','').replace('.','').replace('-','').isdigit():
            raise AttributeError('Nota não pode conter letras ou outros caracteres!')
        if not 0.0 < float(nota.strip().replace(',','.')) < 100.0:
            raise AttributeError('Nota inválida. Valores validos: 0 à 100')

        return True

    def __str__(self):
        return f"{str(self._ra)};{str(self._nome)};{str(self._nota)}"

