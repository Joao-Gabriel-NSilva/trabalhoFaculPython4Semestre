import PySimpleGUI as sg

layout_cadastro = [
    [sg.Text('RA do aluno:', background_color="#2c2825",expand_x=True), sg.InputText(key='ra', size=(60,1), tooltip='RA do aluno.')],
    [sg.Text('Nome do aluno:', background_color="#2c2825",expand_x=True), sg.InputText(key='nome', size=(60,1), tooltip='Nome do aluno.')],
    [sg.Text('Nota do aluno:', background_color="#2c2825",expand_x=True), sg.InputText(key='nota', size=(60,1), tooltip='Nota do aluno.')],
    [sg.Button('Confirmar', key='confirmar_cad', size=(20, 2), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10)),
     sg.Button('Cancelar', key='cancelar_cad', size=(20, 2), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10))]
]

layout_edicao = [
    [sg.Text('RA do aluno:', background_color="#2c2825",expand_x=True), sg.InputText(key='ra', size=(60,1), tooltip='RA do aluno.')],
    [sg.T(' ', background_color="#2c2825",expand_x=True)],
    [sg.Text('Novo nome do aluno:', background_color="#2c2825",expand_x=True), sg.InputText(key='nome', size=(60,1), tooltip='Nome do aluno.')],
    [sg.Text('Nova nota do aluno:', background_color="#2c2825",expand_x=True), sg.InputText(key='nota', size=(60,1), tooltip='Nota do aluno.')],
    [sg.Button('Confirmar', key='confirmar_edi', size=(20, 2), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10)),
     sg.Button('Cancelar', key='cancelar_edi', size=(20, 2), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10))]
]

layout_exclusao = [
    [sg.Text('RA do aluno:', background_color="#2c2825",expand_x=True), sg.InputText(key='ra', size=(60,1), tooltip='RA do aluno.')],
    [sg.T(' ', background_color="#2c2825",expand_x=True)],
    [sg.Button('Confirmar', key='confirmar_exc', size=(20, 2), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10)),
     sg.Button('Cancelar', key='cancelar_exc', size=(20, 2), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10))]
]

layout_resumo = [
    [sg.Text('Quantidade de alunos:', background_color="#2c2825",expand_x=True, pad=(40,5)), sg.Text('Sem alunos.', key='qtde', background_color="#2c2825",expand_x=True)],
    [sg.Text('Maior nota:', background_color="#2c2825",expand_x=True, pad=(40,5)), sg.Text('Sem alunos.', key='maior_nota', background_color="#2c2825",expand_x=True)],
    [sg.Text('Menor nota:', background_color="#2c2825",expand_x=True, pad=(40,5)), sg.Text('Sem alunos.', key='menor_nota', background_color="#2c2825",expand_x=True)],
    [sg.Text('Média das notas:', background_color="#2c2825",expand_x=True, pad=(40,5)), sg.Text('Sem alunos.', key='media', background_color="#2c2825",expand_x=True)],
]

layout_exportacao = [
    [sg.Text('Local:                        ', background_color="#2c2825", expand_x=True), sg.Text('', background_color="#2c2825", expand_x=True, key='local_exp'), sg.FileSaveAs(button_text='Salvar como', button_color=('black', 'crimson'), key='local_salvar', file_types=[('csv', '.csv')], target='local_exp')],
    [sg.Button('Confirmar', key='confirmar_exp', size=(10, 1), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10))]
]

layout_importacao = [
    [sg.Text('Arquivo:                        ', background_color="#2c2825", expand_x=True), sg.Text('', background_color="#2c2825", expand_x=True, key='arquivo_imp'), sg.FileBrowse(button_text='Escolher arquivo', button_color=('black', 'crimson'), key='arquivo', file_types=[('csv', '.csv')], target='arquivo_imp')],
    [sg.Button('Confirmar', key='confirmar_imp', size=(10, 1), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10))]
]
