import PySimpleGUI as sg

layout_principal = [
    [sg.Button('Cadastrar aluno', key='cadastrar', size=(40, 2), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10))],
    [sg.Button('Editar aluno', key='editar', size=(40, 2), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10))],
    [sg.Button('Excluir aluno', key='excluir', size=(40, 2), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10))],
    [sg.Button('Resumo estatístico da turma', key='resumo', size=(40, 2), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10))],
    [sg.Button('Importar informações', key='importar', size=(40, 2), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10))],
    [sg.Button('Exportar informações', key='exportar', size=(40, 2), font=('Mrs Eaves', 12), button_color=('black', 'crimson'), pad=(40,10),)]
]
