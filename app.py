import PySimpleGUI as sg
import View.TelaInicial as view_inicial
import View.ViewsCrudAluno as view_cadastro
import copy
from Servicos.ServicoDeAluno import *


class App:
    def __init__(self):
        self._exportou = False
        self._alunos = []
        sg.theme('darkAmber')
        self._janela = sg.Window('Gerenciador de turma', view_inicial.layout_principal, use_default_focus=False,
                                 border_depth=5, finalize=True)

    def run(self):

        while True:
            eventos, valores = self._janela.read()
            if eventos == sg.WIN_CLOSED:
                self.exporta_antes_de_fechar()
                break
            elif eventos == "cadastrar":
                self.cadastrar()
            elif eventos == "editar":
                self.editar()
            elif eventos == "excluir":
                self.excluir()
            elif eventos == "resumo":
                self.resumo()
            elif eventos == "exportar":
                self.exportar()
            elif eventos == "importar":
                self.importar()

    def exportar(self):
        layout = copy.deepcopy(
            view_cadastro.layout_exportacao)  # gambi pra resolver um erro do pysimplegui q tava dando
        nova_janela = sg.Window('Escolha um local', layout, element_justification='c', finalize=True)
        while True:
            novo_evento, novo_valor = nova_janela.read()
            if novo_evento == sg.WIN_CLOSED:
                break
            elif novo_evento == 'confirmar_exp':
                if novo_valor['local_salvar'] == '':
                    sg.popup_auto_close('Escolha um local para salvar o arquivo!!', title='Aviso',
                                        button_color=('black', 'crimson'), auto_close_duration=5)
                else:
                    try:
                        exportar_alunos(self._alunos, novo_valor['local_salvar'])
                        sg.popup_auto_close('Alunos exportados com sucesso', title='Status',
                                            button_color=('black', 'crimson'),
                                            auto_close_duration=2)
                        nova_janela.close()
                        self._exportou = True
                        break
                    except Exception as e:
                        sg.popup_auto_close(e.args[0], title='Erro ao exportar alunos',
                                            button_color=('black', 'crimson'))

    def cadastrar(self):
        layout = copy.deepcopy(
            view_cadastro.layout_cadastro)  # gambi pra resolver um erro do pysimplegui q tava dando
        nova_janela = sg.Window('Cadastro de alunos', layout, element_justification='c')

        while True:
            novo_evento, novo_valor = nova_janela.read()
            if novo_evento == sg.WIN_CLOSED:
                break
            elif novo_evento == "confirmar_cad":
                try:
                    adicionar_aluno(novo_valor["ra"], novo_valor["nome"], novo_valor["nota"], self._alunos)
                    sg.popup_auto_close('Aluno cadastrado com sucesso', title='Status',
                                        button_color=('black', 'crimson'),
                                        auto_close_duration=2)
                    nova_janela.close()
                    break
                except AttributeError as e:
                    sg.popup_auto_close(e.args[0], title='Erro ao salvar aluno',
                                        button_color=('black', 'crimson'),
                                        auto_close_duration=5)
            elif novo_evento == "cancelar_cad":
                nova_janela.close()
                break

    def editar(self):
        layout = copy.deepcopy(
            view_cadastro.layout_edicao)  # gambi pra resolver um erro do pysimplegui q tava dando
        nova_janela = sg.Window('Cadastro de alunos', layout, element_justification='c')

        while True:
            novo_evento, novo_valor = nova_janela.read()
            if novo_evento == sg.WIN_CLOSED:
                break
            elif novo_evento == "confirmar_edi":
                try:
                    editar_aluno(novo_valor["ra"], novo_valor["nome"], novo_valor["nota"], self._alunos)
                    nova_janela.close()
                    sg.popup_auto_close('Aluno cadastrado com sucesso', title='Status',
                                        button_color=('black', 'crimson'),
                                        auto_close_duration=2)
                    break
                except AttributeError as e:
                    sg.popup_auto_close(e.args[0], title='Erro ao editar aluno',
                                        button_color=('black', 'crimson'),
                                        auto_close_duration=5)
            elif novo_evento == "cancelar_edi":
                nova_janela.close()
                break

    def excluir(self):
        layout = copy.deepcopy(
            view_cadastro.layout_exclusao)  # gambi pra resolver um erro do pysimplegui q tava dando
        nova_janela = sg.Window('Exclusão de alunos', layout, element_justification='c')

        while True:
            novo_evento, novo_valor = nova_janela.read()
            if novo_evento == sg.WIN_CLOSED:
                break
            elif novo_evento == "confirmar_exc":
                try:
                    excluir_aluno(novo_valor["ra"], self._alunos)
                    sg.popup_auto_close('Aluno excluido com sucesso', title='Status',
                                        button_color=('black', 'crimson'),
                                        auto_close_duration=2)
                    nova_janela.close()
                    for a in self._alunos:
                        print(a)
                    break
                except AttributeError as e:
                    sg.popup_auto_close(e.args[0], title='Erro ao excluir aluno',
                                        button_color=('black', 'crimson'),
                                        auto_close_duration=5)
            elif novo_evento == "cancelar_exc":
                nova_janela.close()
                break

    def resumo(self):
        layout = copy.deepcopy(
            view_cadastro.layout_resumo)  # gambi pra resolver um erro do pysimplegui q tava dando
        nova_janela = sg.Window('Resumo', layout, element_justification='c', finalize=True)
        resumo = obtem_resumo(self._alunos)
        if resumo is not None:
            nova_janela['qtde'].update(resumo['qtde'])
            nova_janela['menor_nota'].update(f'{resumo["menor"].nome} - {resumo["menor"].nota}')
            nova_janela['maior_nota'].update(f'{resumo["maior"].nome} - {resumo["maior"].nota}')
            nova_janela['media'].update(resumo["media"])

    def importar(self):
        layout = copy.deepcopy(
            view_cadastro.layout_importacao)  # gambi pra resolver um erro do pysimplegui q tava dando
        nova_janela = sg.Window('Escolha um arquivo', layout, element_justification='c', finalize=True)
        while True:
            novo_evento, novo_valor = nova_janela.read()
            if novo_evento == sg.WIN_CLOSED:
                break
            elif novo_evento == 'confirmar_imp':
                if novo_valor['arquivo'] == '':
                    sg.popup_auto_close('Escolha um arquivo para importar!!', title='Aviso',
                                        button_color=('black', 'crimson'), auto_close_duration=5)
                else:
                    try:
                        importar_alunos(self._alunos, novo_valor['arquivo'])
                        sg.popup_auto_close('Alunos importados com sucesso', title='Status',
                                            button_color=('black', 'crimson'),
                                            auto_close_duration=2)
                        nova_janela.close()
                        break
                    except Exception as e:
                        sg.popup_auto_close(
                            'Erro ao importar. Verifique o arquivo, o mesmo deve estar no formato _nome;_ra;_nota com os respectivos valores de cada aluno abaixo das colunas. Exceção: ' +
                            e.args[0], title='Erro ao importar alunos',
                            button_color=('black', 'crimson'))

    def exporta_antes_de_fechar(self):
        if not self._exportou:
            if len(self._alunos) > 0:
                result = sg.popup_yes_no('Deseja exportar os alunos', no_titlebar=True,
                                         button_color=('black', 'crimson'))
                if result == 'Yes':
                    self.exportar()