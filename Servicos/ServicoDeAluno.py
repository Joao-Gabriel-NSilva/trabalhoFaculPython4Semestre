from Model.Aluno import *
import csv

def adicionar_aluno(ra, nome, nota, alunos):
    ra_existe_com_excecao(ra, alunos, True)
    aluno = Aluno(ra, nome, nota)
    alunos.append(aluno)


def editar_aluno(ra, nome, nota, alunos):
    ra_existe_com_excecao(ra, alunos, False)

    aluno = Aluno(ra, nome, nota)
    for index, item in enumerate(alunos):
        if item.ra == aluno.ra:
            item.nome = aluno.nome
            item.nota = aluno.nota
            break


def excluir_aluno(ra, alunos):
    ra_existe_com_excecao(ra, alunos, False)

    i = -1
    for index, item in enumerate(alunos):
        if str(item.ra) == ra.strip():
            i = index
    alunos.remove(alunos[i])


def ra_existe_com_excecao(ra, alunos, verifica_duplicado):
    if verifica_duplicado:
        if ra.strip() in [str(aluno.ra) for aluno in alunos]:
            ras = [str(aluno.ra) for aluno in alunos]
            ras.sort()
            raise AttributeError(f'O aluno com o RA informado ja existe. Use outro RA. Sugerido: {int(ras[-1]) + 1}')
    else:
        if not ra.strip() in [str(aluno.ra) for aluno in alunos]:
            raise AttributeError('RA não encontrado. Verifique o valor e tente novamente!')


def obtem_resumo(alunos):
    qtde = len(alunos)
    if qtde == 0:
        return None
    elif qtde == 1:
        return {'maior': alunos[0], 'menor': alunos[0], 'qtde': qtde, 'media': alunos[0].nota}
    maior = None
    menor = None
    soma = 0

    for a in alunos:
        soma += a.nota
        if maior is None:
            maior = a
        else:
            if a.nota >= maior.nota:
                maior = a
        if menor is None:
            menor = a
        else:
            if a.nota <= menor.nota:
                menor = a

    media = soma / qtde
    return {'maior': maior, 'menor': menor, 'qtde': len(alunos), 'media': media}


def exportar_alunos(alunos, caminho):
    lista_dicts = [a.__dict__ for a in alunos]

    with open(caminho, encoding='UTF-8', mode='w', newline='') as arquivo:
        writer = csv.DictWriter(arquivo, delimiter=';', fieldnames=['_nome', '_ra', '_nota'])
        writer.writeheader()
        writer.writerows(lista_dicts)


def importar_alunos(alunos, caminho):
    with open(caminho, encoding='UTF-8') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        i = 1
        for linha in leitor:
            if i == 1:
                i +=1
                continue
            nome, ra, nota = linha
            aluno = Aluno(ra, nome, nota)
            alunos.append(aluno)