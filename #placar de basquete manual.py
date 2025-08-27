# placar de basquete manual

import PySimpleGUI as ag

# Layouts e janelas
def janela_times():
    ag.theme('reddit')
    layout = [
        [ag.Text('Insira o nome do time da casa')],
        [ag.Input(key='time_casa')],
        [ag.Text('Insira o nome do time visitante')],
        [ag.Input(key='time_visitante')],
        [ag.Button('continuar')]
    ]
    return ag.Window('times', layout=layout, finalize=True)

def janela_placar(nome_casa, nome_visitante):
    ag.theme('reddit')
    layout = [
        [ag.Radio('1° quarto', 'GENERO', key='masculino'),
        ag.Radio('2° quarto', 'GENERO', key='masculino'),
        ag.Radio('3° quarto', 'GENERO', key='masculino'),
        ag.Radio('4° quarto', 'GENERO', key='masculino')],
        [ag.Text("placar",)],
        [ag.Text(nome_casa, key='nome_casa'), ag.Text(nome_visitante, key='nome_visitante')],
        [ag.Text('0 ', key='placar_casa'), ag.Text('0', key='placar_visitante')],
        [ag.Text('Adicionar os pontos aos times:')],
        [ag.Button('casa.1'), ag.Button('vis.1')],
        [ag.Button('casa.2'), ag.Button('vis.2')],
        [ag.Button('casa.3'), ag.Button('vis.3')],
        [ag.Button('voltar')],[ag.Button('resetar')]
    ]
    return ag.Window('placar manual', layout=layout, finalize=True)

# Criar janelas iniciais
janela_1, janela2 = janela_times(), None

# Pontuação inicial
pontos_casa = 0
pontos_visitante = 0

# Criar um loop de leitura de eventos
while True:
    window, event, values = ag.read_all_windows()

    # Janela fechada
    if event == ag.WIN_CLOSED:
        window.close()
        if window == janela2:
            janela_1.close()
        elif window == janela_1:
            if janela2:
                janela2.close()
        break

    # Ir para próxima janela
    if window == janela_1 and event == 'continuar':
        nome_casa = values['time_casa']
        nome_visitante = values['time_visitante']
        pontos_casa = 0
        pontos_visitante = 0
        janela2 = janela_placar(nome_casa, nome_visitante)
        janela_1.hide()

    # Voltar para janela anterior
    if window == janela2 and event == 'voltar':
        janela2.hide()
        janela_1.un_hide()

    # Adição dos pontos e atualização do placar
    if window == janela2:
        if event == 'casa.1':
            pontos_casa += 1
        elif event == 'casa.2':
            pontos_casa += 2
        elif event == 'casa.3':
            pontos_casa += 3
        elif event == 'vis.1':
            pontos_visitante += 1
        elif event == 'vis.2':
            pontos_visitante += 2
        elif event == 'vis.3':
            pontos_visitante += 3
        elif event == 'resetar':
             pontos_visitante *= 0
             pontos_casa  *= 0
        # Atualizar o placar na tela
        janela2['placar_casa'].update(str(pontos_casa))
        janela2['placar_visitante'].update(str(pontos_visitante))
